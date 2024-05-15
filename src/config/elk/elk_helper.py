from contextlib import asynccontextmanager

from elasticsearch import AsyncElasticsearch

from config.project_config import app_config


@asynccontextmanager
async def create_es_client():
    es_client = AsyncElasticsearch(hosts=app_config.elk.hosts)
    try:
        yield es_client
    finally:
        await es_client.close()
