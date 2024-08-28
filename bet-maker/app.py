from fastapi import FastAPI



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
