FROM python:3.6.1

LABEL MAINTAINER="Jama Noor (jamawadi@gmail.com)"

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev


# Copy files from actual computer to a folder named django
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django
RUN pip install -r requirements.txt

COPY . /django

