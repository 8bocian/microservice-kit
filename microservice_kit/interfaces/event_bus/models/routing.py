from pydantic import BaseModel


class Routing(BaseModel):
    ...

class RabbitMQRouting(Routing):
    ...