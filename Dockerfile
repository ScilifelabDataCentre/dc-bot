# Choose relevant Python version for the build
FROM python:3.10-alpine as base

# upgrade to latest packages
RUN apk update && apk upgrade

# install required modules
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# add the relevant code folder to the image
COPY . /code
WORKDIR /code
ENV PYTHONPATH /code

# parameters for gunicorn (as they would have been set in cli)
ENV GUNICORN_CMD_ARGS "--bind=0.0.0.0:8000 --workers=2 --thread=4 --worker-class=gthread --forwarded-allow-ips='*' --access-logfile -"

WORKDIR /code
CMD ["python", "app.py"]
