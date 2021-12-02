FROM python:3
ADD alerting_api.py /
RUN pip install flask
RUN pip install flask-restful
RUN pip install pandas

CMD ["python", "./alerting_api.py"]


