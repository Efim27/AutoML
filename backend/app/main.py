from app.controller.api_controller import controller
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://0.0.0.0:8080",
    "http://localhost:8080"
]

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs", redoc_url="/api/v1/redoc")
app.include_router(controller)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
