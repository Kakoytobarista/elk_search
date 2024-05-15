import asyncio

import pytest
from http import HTTPStatus
from faker import Faker
from main import app
from fastapi.testclient import TestClient

from schemas.v1.search_schema import Document


client = TestClient(app)


class TestSearchControllers:

    @staticmethod
    @pytest.mark.asyncio
    async def create_record(text):
        data = dict(Document(text=text))
        response = client.post("/search/", json=data)
        await asyncio.sleep(1)
        return response

    @pytest.mark.asyncio
    async def test_store_document(self):
        text = Faker().text(max_nb_chars=10)
        response = await self.create_record(text=text)
        assert response.status_code == HTTPStatus.OK
        assert response.json()["document_id"]

    @pytest.mark.parametrize(
        'text, expected_status_code', [
            (Faker().text(max_nb_chars=10), HTTPStatus.OK),
            ("", HTTPStatus.BAD_REQUEST),
        ]
    )
    @pytest.mark.asyncio
    async def test_search_documents(self, text, expected_status_code):
        await self.create_record(text=text)
        response = client.get(f"/search/?query={text}")
        assert response.status_code == expected_status_code
        if text:
            assert response.json().get("results")[0].get("text") == text
