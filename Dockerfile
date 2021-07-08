FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requirenments.txt /app/requirenments.txt
RUN pip install -r requirenments.txt
COPY . /app

EXPOSE 8000
