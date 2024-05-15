from fastapi.routing import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html


router = APIRouter(prefix="/docs", tags=["docs"])


@router.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger UI")
