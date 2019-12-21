FROM python:3.4
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install uwsgi
CMD ["python", "app.py"]

