from fastapi import APIRouter

from app.models.system import StatusResponse

router = APIRouter()


@router.get("/status")
def health() -> StatusResponse:
    return StatusResponse(healthy=True)
