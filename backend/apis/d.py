from fastapi.openapi.docs import get_redoc_html
from fastapi.responses import HTMLResponse

from . import *


@router.get(summary="redoc接口文档页")
async def redoc() -> HTMLResponse:
    from backend.app import app
    return get_redoc_html(
        openapi_url="/openapi.json",
        title=f"{app.title} - 接口文档",
        redoc_js_url="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js",
        redoc_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
        with_google_fonts=True
    )
