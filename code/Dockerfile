FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN apt-get update && pip install --upgrade pip && pip install -r requirements.txt

COPY  . .

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:8000",  "config.wsgi"]