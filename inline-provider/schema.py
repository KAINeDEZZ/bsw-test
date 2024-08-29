import enum
from pydantic import BaseModel


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(BaseModel):
    id: int
    coefficient: float = None
    deadline: int = None
    state: EventState = None
