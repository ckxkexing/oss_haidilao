FROM python:3.8-slim-buster

WORKDIR /oss_haidilao

RUN pip3 install flask Flask-SQLAlchemy pymysql
RUN pip3 install cryptography
RUN pip3 install flask-marshmallow
COPY . .

EXPOSE 5000

CMD [ "flask", "--app" , "main", "--debug", "run", "--host=0.0.0.0"]
