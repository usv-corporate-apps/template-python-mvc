FROM python:3.10.12

LABEL maintainer=""

WORKDIR /app

ADD . /app

RUN pip install -r /app/requirements.txt 

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]