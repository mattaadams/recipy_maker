FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# COPY recipy/ .

# # RUN git clone https://github.com/mattaadams/recipy_maker.git && cd example
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]