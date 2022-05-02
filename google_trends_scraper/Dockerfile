FROM python:3.7-slim

WORKDIR /code

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY ./executors /code/executors
COPY ./interfaces /code/interfaces
COPY ./models /code/models


CMD [ "python", "./code/executors/main.py" ]
