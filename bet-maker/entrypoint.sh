#!/bin/bash -x


if [ "$*" == "" ]; then
  exec uvicorn app:app --host 0.0.0.0 --port 8000

elif [ "$1" = "load_events" ]; then
  exec python load_events.py

elif [ "$1" = "upgrade" ]; then
  exec alembic upgrade head

elif [ "$1" = "revision" ]; then
  exec alembic revision --autogenerate

elif [ "$1" = "consumer" ]; then
  exec python consumer.py

else
  echo "Custom command:"
  exec "$@"
fi
