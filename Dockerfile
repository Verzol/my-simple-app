FROM python:3.9-slim

RUN pip install Flask

COPY app.py /app/
WORKDIR /app

EXPOSE 80

CMD ["python", "app.py"]