FROM ubuntu:18.04

RUN apt update &&\
    apt upgrade -y

RUN apt install -y build-essential python3

WORKDIR /app
COPY ./py3software_0.1-1_amd64.deb ./myapp.deb

RUN apt install -y ./myapp.deb

RUN sayhello

CMD ["/bin/bash"]
