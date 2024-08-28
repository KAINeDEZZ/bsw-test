import enum
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Uuid, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)

    coefficient: Mapped[float] = mapped_column(Float())
    deadline: Mapped[int] = mapped_column(Integer())
    state: Mapped[EventState] = mapped_column(Integer())


class Bet(Base):
    __tablename__ = "bet"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float] = mapped_column(Float())

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    event: Mapped["Event"] = relationship()
