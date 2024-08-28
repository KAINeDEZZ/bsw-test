FROM python:3.10-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app
COPY app.py app.py

COPY entrypoint.sh entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
