import logging
from fastapi import HTTPException, APIRouter

from exceptions import QueryNotFoundException
from schemas.v1.search_schema import StoreDocumentResponse, Document, SearchDocumentsResponse, SearchResult

from services.v1.search_service import search_service

router = APIRouter(prefix="/search", tags=["search"])


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/", response_model=StoreDocumentResponse)
async def store_document(document: Document):
    try:
        response = await search_service.store_document(data=document)
        return response

    except Exception as e:
        logger.error(f"Error while stored document, error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=SearchDocumentsResponse)
async def search_documents(query: str):
    try:
        response = await search_service.search_documents(query=query)
        return response

    except QueryNotFoundException as e:
        logger.error(f"Error while getting document, error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"Error while getting document, error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
