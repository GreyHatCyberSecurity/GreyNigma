FROM python:3.8-slim-buster

WORKDIR /GreyNigma
COPY ./requirements.txt /GreyNigma/requirements.txt
COPY ./core_local.py /GreyNigma/core_local.py
COPY ./GreyNigma_CLI.py /GreyNigma/GreyNigma_CLI.py

ENV PYTHONPATH "${PYTHONPATH}:/usr/bin/python3"

RUN pip3 install -r requirements.txt


CMD ["python3", "GreyNigma_CLI.py"]

