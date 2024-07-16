## automatic docker variant
```bash
docker buildx build --platform linux/amd64 -t unpacker .
docker run -it --rm -v ./data:/data --platform linux/amd64 unpacker /data
```

## local docker setup variant
start up a docker ubuntu container (linux/amd64 only bc of rar package)
```bash
    docker run -it --rm -v ./$pwd:/opt/unpack -w /opt/unpack --platform linux/amd64 ubuntu:latest bash
```

simply install python3 and rar from multiverse repo with apt
```bash
    apt update && apt-get install software-properties-common -y && add-apt-repository multiverse -y && apt install rar -y
```

run the unpacker script on the appropriate folder
```bash
    chmod +x unpack.py
    python3 unpack <source-directory>
```