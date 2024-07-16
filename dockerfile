FROM ubuntu:latest

WORKDIR /opt/unpack

COPY --link unpack.py /opt/unpack

RUN apt update \
    && apt-get install software-properties-common -y \
    && add-apt-repository multiverse -y \
    && apt install rar -y \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3", "unpack.py"]
CMD ["."]