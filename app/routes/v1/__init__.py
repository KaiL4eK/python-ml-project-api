from fastapi import FastAPI

from . import hello, prediction, system

api = FastAPI()
api.include_router(hello.router, tags=["greetings"], prefix="/hello")
api.include_router(prediction.router, tags=["prediction"], prefix="/predict")
api.include_router(system.router, tags=["system"])
