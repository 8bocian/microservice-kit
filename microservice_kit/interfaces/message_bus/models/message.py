from datetime import datetime
from uuid import uuid4, UUID

from pydantic import BaseModel, Field

from microservice_kit.interfaces.message_bus.models.routing import Routing


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.timestamp)
    ...





