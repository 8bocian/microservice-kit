from typing import TypeVar
from pydantic import BaseModel

Event = TypeVar("Event", bound=BaseModel)
