from datetime import datetime
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.timestamp)
    ...

class Routing(BaseModel):
    ...

class Envelope(BaseModel):
    event: Event
    routing: Routing