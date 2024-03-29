FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt update -y && apt install awscli -y

CMD ["python3",'app.py']
