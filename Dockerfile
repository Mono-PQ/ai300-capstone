FROM python:3.9-slim

WORKDIR /flask-app 

COPY ./requirements.txt /flask-app/requirements.txt
COPY ./src /flask-app/src
COPY ./artifact /flask-app/artifact

ENV PYTHONPATH /flask-app/src

RUN apt-get update
RUN apt-get -y install gcc
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 80

CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]