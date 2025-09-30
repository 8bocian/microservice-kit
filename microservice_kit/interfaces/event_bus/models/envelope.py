from pydantic import BaseModel
from microservice_kit.interfaces.event_bus.models.event import Event
from microservice_kit.interfaces.event_bus.models.routing import Routing


class Envelope(BaseModel):
    event: Event
    routing: Routing