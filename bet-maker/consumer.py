import json
import os
import signal
import time

import redis
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

import models

QUEUE_NAME = 'line-provider-events'
RUNNING = True


# signal handler helps to stop container to avoid error exit code
def signal_handler(self, *args, **kwargs):
    global RUNNING
    RUNNING = False


def main():
    connection = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, db=0)

    signal.signal(signal.SIGTERM, signal_handler)
    while RUNNING:
        event = connection.lpop(QUEUE_NAME)

        if event is not None:
            try:
                stmt = insert(models.Event).values(json.loads(event))
                stmt = stmt.on_conflict_do_update(
                    index_elements=['id'],
                    set_={
                        "coefficient": stmt.excluded.coefficient,
                        "deadline": stmt.excluded.deadline,
                        "state": stmt.excluded.state,
                    }
                )

                with Session(models.engine) as session:
                    session.execute(stmt)
                    session.commit()

            except Exception as e:
                # This is for example, i prefer to use sentry in production
                print(e)

        time.sleep(0.1)


if __name__ == '__main__':
    print('starting consumer')
    main()
