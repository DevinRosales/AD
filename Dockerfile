#Dockerfile for autodesk technical assessment
FROM ubuntu:18.04
MAINTAINER Devin Rosales "devinrosales@gmail.com"
RUN apt-get update -y && apt-get install -y python3-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD [ "python3", "./autodesk_homework.py" ]
