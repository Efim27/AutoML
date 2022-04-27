from app.controller.api_controller import controller
from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs", redoc_url="/api/v1/redoc")
app.include_router(controller)
