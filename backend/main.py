from fastapi import FastAPI
from backend.controller.api_controller import controller

app = FastAPI()
app.include_router(controller)
