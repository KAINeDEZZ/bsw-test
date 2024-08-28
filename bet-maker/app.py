from fastapi import FastAPI
import os

from sqlalchemy import create_engine

engine = create_engine(os.environ['DB_CONNECTION_STRING'])

app = FastAPI()


@app.get('/events')
async def get_events():
    pass


@app.post('/bet')
async def set_bet():
    pass


@app.get('/bet/{bet_id}')
async def create_event():
    pass
