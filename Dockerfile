FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask pandas matplotlib requests pygal flask_sqlalchemy

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run"]
