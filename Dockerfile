# Please consider using the -alpine or -slim versions of the python image for smaller
# footprints, this is only provided as an initial template.
FROM python:3.8-alpine as base

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV DISPLAY=0

COPY src/ /app

CMD [ "python3", "/app/main.py" ]
