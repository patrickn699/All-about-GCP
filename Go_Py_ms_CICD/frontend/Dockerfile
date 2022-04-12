FROM python:alpine

#RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install Flask
RUN pip install requests
CMD ["python", "front_end.py"]