FROM ubuntu:latest

WORKDIR /opt/unpack

COPY unpack.py .

RUN apt update \
    && apt-get install software-properties-common -y \
    && add-apt-repository multiverse -y \
    && apt install rar -y

ENTRYPOINT ["python3", "unpack.py"]
CMD ["."]