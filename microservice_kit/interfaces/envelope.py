from pydantic import BaseModel


class Envelope(BaseModel):
    event: Event
    routing: Routing