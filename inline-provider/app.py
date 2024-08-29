import enum
import time

from fastapi import FastAPI, Path, HTTPException
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


events: dict[str, Event] = {
    '1': Event(id=1, coefficient=1.2, deadline=int(time.time()) + 600, state=EventState.NEW),
    '2': Event(id=2, coefficient=1.15, deadline=int(time.time()) + 60, state=EventState.NEW),
    '3': Event(id=3, coefficient=1.67, deadline=int(time.time()) + 90, state=EventState.NEW)
}

app = FastAPI()


@app.put('/event')
async def create_event(event: Event):
    if event.event_id not in events:
        events[event.event_id] = event
        return {}

    for p_name, p_value in event.dict(exclude_unset=True).items():
        setattr(events[event.event_id], p_name, p_value)

    return {}


@app.get('/event/{event_id}')
async def get_event(event_id: str = Path()):
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@app.get('/events')
async def get_events():
    return list(e for e in events.values())
