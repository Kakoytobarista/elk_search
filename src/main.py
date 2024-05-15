import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from config.project_config import app_config
from controllers.v1.search_controller import router as search_router
from controllers.v1.swagger_controller import router as swagger_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_application() -> FastAPI:
    try:
        application = FastAPI(
            title=app_config.service_name,
            debug=app_config.debug,
            version=app_config.version
        )
        application.include_router(search_router)
        application.include_router(swagger_router)

        application.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            allow_headers=["*"],
        )
        return application
    except Exception as e:
        logger.error(f"Error while construct app, Error: {e}")


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)

# curl -X GET "localhost:9200/documents_index/_search?q=Aslan"
# curl -X DELETE "localhost:9200/simple_index/_doc/3cfc5e97-0de2-40e5-9cd3-a1c097f743fc"
# curl -X DELETE "http://localhost:9200/test_index/_delete_by_query" -H 'Content-Type: application/json' -d'
# {
#   "query": {
#     "match_all": {}
#   }
# }'
