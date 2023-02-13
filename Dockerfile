
FROM python:3.9-bullseye

RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt  ./
RUN pip install -r requirements.txt
ADD . /app

ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "--port=5001", "--call", "index:create_app"]
