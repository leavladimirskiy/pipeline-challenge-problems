FROM python:3.11-slim

WORKDIR /src

COPY main.py .

CMD ["python", "main.py"]