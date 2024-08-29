import requests
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from models import engine, Event


# In this implementation of line-provider we dont need this command,
# but if line-provider will be uses database it will be helpful
def main():
    events = requests.get('http://line-provider:8080/events').json()
    print(f'Adding {len(events)} events')

    stmt = insert(Event).values(events)
    stmt = stmt.on_conflict_do_update(
        index_elements=['id'],
        set_={
            "coefficient": stmt.excluded.coefficient,
            "deadline": stmt.excluded.deadline,
            "state": stmt.excluded.state,
        }
    )

    with Session(engine) as session:
        session.execute(stmt)
        session.commit()


if __name__ == '__main__':
    main()
