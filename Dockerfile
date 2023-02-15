FROM python:3.9.15-slim as builder
RUN apt-get update && \
    apt-get install -y gcc
ADD requirements.txt  ./
RUN mkdir -p /install
RUN pip3 install --prefix=/install -r requirements.txt

FROM python:3.9.15-slim
COPY --from=builder /install /usr/local
RUN mkdir -p /app
WORKDIR /app
ADD . /app

ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "--port=5001", "--call", "index:create_app"]
