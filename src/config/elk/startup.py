import asyncio

from config.elk.elk_helper import create_es_client


async def create_index_if_not_exists():
    async with create_es_client() as es:
        if not await es.indices.exists(index='simple_index'):
            await es.indices.create(index='simple_index')
            await es.indices.create(index='test_index')

async def main():
    await create_index_if_not_exists()

if __name__ == "__main__":
    asyncio.run(main())
