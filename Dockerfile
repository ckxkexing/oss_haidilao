FROM python:3.8-slim-buster

WORKDIR /oss_haidilao

RUN pip3 install flask

COPY . .

CMD [ "flask", "--app" , "main", "run", "--host=0.0.0.0"]
