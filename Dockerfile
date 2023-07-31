FROM python:3.8-slim-buster

WORKDIR /oss_haidilao

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "--app" , "main", "--debug", "run", "--host=0.0.0.0"]
