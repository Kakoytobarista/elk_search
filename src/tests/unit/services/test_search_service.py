import asyncio

import pytest
from faker import Faker

from exceptions import QueryNotFoundException
from schemas.v1.search_schema import Document, StoreDocumentResponse, SearchDocumentsResponse
from services.v1.search_service import search_service


class TestSearchService:

    @staticmethod
    @pytest.mark.asyncio
    async def create_record(text):
        data = Document(text=text)
        result = await search_service.store_document(data=data)
        await asyncio.sleep(1)
        return result

    @pytest.mark.asyncio
    async def test_store_document(self):
        data = await self.create_record(Faker().text(max_nb_chars=5))
        assert isinstance(data, StoreDocumentResponse)
        assert data.document_id

    @pytest.mark.asyncio
    async def test_search_documents(self):
        text = Faker().text(max_nb_chars=5)
        await self.create_record(text)
        result = await search_service.search_documents(query=text)
        assert isinstance(result, SearchDocumentsResponse)
        assert result

    @pytest.mark.asyncio
    async def test_un_exists_search_documents(self):
        text = Faker().name()
        result = await search_service.search_documents(query=text)
        assert isinstance(result, SearchDocumentsResponse)
        assert result

    @pytest.mark.asyncio
    async def test_search_documents_without_query(self):
        with pytest.raises(QueryNotFoundException):
            await search_service.search_documents(query="")
