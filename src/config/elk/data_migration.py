import asyncio

from faker import Faker
import random

from config.elk.elk_helper import create_es_client
from config.project_config import app_config

fake = Faker()

texts = [
    "We are searching text hello",
    "We are searching text bye",
    "We are searching text hi",
    "We are searching text hey",
    "We are searching text bye bye",
]

async def mock_data():
    for _ in range(5):
        text = " ".join(random.sample(texts, random.randint(2, 5)))
        doc = {"text": text}
        async with create_es_client() as es:
            await es.index(index=app_config.elk.index_name, body=doc)


async def main():
    await mock_data()

if __name__ == "__main__":
    asyncio.run(main())
