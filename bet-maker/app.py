import time

from fastapi import FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from models import Event, engine, Bet, EventState
from schema import RequestBet

app = FastAPI()


@app.get('/events')
async def get_events():
    with Session(engine) as session:
        events = session.query(Event).where(Event.deadline > time.time())

    return list(e for e in events)


@app.post('/bet')
async def set_bet(bet: RequestBet):
    with Session(engine) as session:
        bet = session.execute(insert(Bet).values(**bet.model_dump()).returning(Bet.id)).fetchone()
        session.commit()

    return {'id': bet.id}


@app.get('/bet/{bet_id}')
async def get_bet(bet_id: int):
    with Session(engine) as session:
        bet, state = session.execute(
            select(Bet, Event.state).join(Event, Bet.event_id == Event.id).where(Bet.id == bet_id)).first()

    if not bet:
        raise HTTPException(status_code=404, detail="Item not found")

    return {'event_id': bet.event_id, 'value': bet.value, 'state': EventState(state).name}


@app.get('/bets')
async def get_bets():
    with Session(engine) as session:
        bets = session.query(Bet, Event.state).join(Event, Bet.event_id == Event.id).all()

    return list(
        {'event_id': bet.event_id, 'value': bet.value, 'state': EventState(state).name} for bet, state in bets)
