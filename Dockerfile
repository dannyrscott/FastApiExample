# Dockerfile for FastAPI service
FROM python:3.9-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
