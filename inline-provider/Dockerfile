FROM python:3.10-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app
COPY app.py app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
