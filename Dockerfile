FROM python:3.10-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY recipy/ .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]