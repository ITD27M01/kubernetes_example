FROM python:latest

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

EXPOSE 8080