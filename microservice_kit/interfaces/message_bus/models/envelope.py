from pydantic import BaseModel
from microservice_kit.interfaces.message_bus.models.message import Message
from microservice_kit.interfaces.message_bus.models.routing import Routing


class Envelope(BaseModel):
    message: Message
    routing: Routing