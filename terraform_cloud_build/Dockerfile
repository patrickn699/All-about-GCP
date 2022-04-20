FROM python:3.7-slim-buster

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]