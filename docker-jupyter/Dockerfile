FROM jupyter/minimal-notebook

USER root
RUN mkdir -p /home/notebook

WORKDIR /home/notebook

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt