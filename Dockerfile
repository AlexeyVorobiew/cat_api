FROM python:3.6-slim

MAINTAINER alexey.worobiew@gmail.com

COPY . /

WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "/tests", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null