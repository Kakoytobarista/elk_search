from typing import List

from pydantic import BaseModel


class SearchResult(BaseModel):
    document_id: str
    text: str


class StoreDocumentResponse(BaseModel):
    document_id: str


class SearchDocumentsResponse(BaseModel):
    results: List[SearchResult]


class Document(BaseModel):
    text: str
