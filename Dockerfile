FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements/common.txt /app/common.txt
RUN pip install --no-cache-dir -r common.txt
COPY . /app
