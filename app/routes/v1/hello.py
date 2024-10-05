from fastapi import APIRouter

from services.hello import say_hello

router = APIRouter()


@router.get("/{name}")
def greetings(name: str) -> str:
    return say_hello(name)
