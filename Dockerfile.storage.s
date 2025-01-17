FROM python:3.9-slim

WORKDIR /app

COPY storage_server.py /app/

RUN pip install flask

CMD ["python", "storage_server.py"]
