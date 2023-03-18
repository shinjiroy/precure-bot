ARG MODULE_DIR="/function"

FROM python:3.9-buster

RUN apt update && \
    apt install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev

RUN mkdir /modules
ENV PYTHONPATH=/modules
RUN pip install --target /modules awslambdaric

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
RUN chmod 775 /usr/bin/aws-lambda-rie
