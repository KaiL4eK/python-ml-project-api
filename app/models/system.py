from pydantic import BaseModel


class StatusResponse(BaseModel):
    healthy: bool
