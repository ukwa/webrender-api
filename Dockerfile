FROM python:3.7-slim

COPY requirements.txt /webrender/requirements.txt

WORKDIR webrender

RUN \
  pip install -r requirements.txt

COPY . .

EXPOSE 8010

CMD gunicorn -c gunicorn.ini webrender.wrengine:app
