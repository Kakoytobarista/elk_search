import asyncio
import logging
from typing import Union, List
from uuid import uuid4

from ai import LLMManager
from config.project_config import app_config
from exceptions import QueryNotFoundException
from schemas.v1.search_schema import StoreDocumentResponse, Document, SearchDocumentsResponse, SearchResult

from config.elk.elk_helper import create_es_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SearchService:
    def __init__(self, es_generator: Union[create_es_client]):
        self.es_generator = es_generator

    async def store_document(self, data: Document) -> StoreDocumentResponse:
        async with self.es_generator() as es:
            document_id = str(uuid4())
            await es.index(index=app_config.elk.index_name, id=document_id, body={"text": data.text})
            logger.info(f"Successfully stored document with text: {data.text}")
            return StoreDocumentResponse(document_id=document_id)

    async def _get_documents(self, query: str) -> List[SearchResult]:
        if not query:
            raise QueryNotFoundException("Query not provided")

        async with self.es_generator() as es:
            search_results = await es.search(
                index=app_config.elk.index_name, body={"query": {"match": {"text": query}}}
            )
            hits = search_results["hits"]["hits"]

            results = [
                SearchResult(document_id=hit["_id"], text=hit["_source"]["text"])
                for hit in hits
            ]
            logger.info(f"Got {len(results)}")
            logger.info(results)

            return results

    async def search_documents(self, query: str) -> SearchDocumentsResponse:
        results = await self._get_documents(query=query)
        if not results:
            generated_text = LLMManager().generate(prompt=query)
            await self.store_document(Document(text=generated_text))
            await asyncio.sleep(1)
            results = await self._get_documents(query=query)

        sorted_results = sorted(results, key=lambda x: len(x.text), reverse=True)
        return SearchDocumentsResponse(results=sorted_results)


search_service = SearchService(es_generator=create_es_client)
