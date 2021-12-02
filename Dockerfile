FROM python:3.8-slim-buster

MAINTAINER ke.co.austinstevesk

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "alerting_api.py"]