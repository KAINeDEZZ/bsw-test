from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session

from models import engine, Event


class RequestBet(BaseModel):
    event_id: int
    value: float

    @field_validator('value')
    def validate_bet_value(cls, value):
        if value <= 0:
            raise ValueError('Bet value must be strictly positive.')
        if round(value, 2) != value:
            raise ValueError('Bet value must have exactly two decimal places.')
        return value

    @field_validator('event_id')
    def validate_event(cls, value):
        with Session(engine) as session:
            if session.query(Event.id).where(Event.id == value).first() is not None:
                return value

            raise ValueError('Invalid event id.')
