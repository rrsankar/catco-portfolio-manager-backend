FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"

# BEGIN: INSTALL BASIC PYTHON PACKAGES.
RUN apt-get update && apt-get install -y pkg-config \
                                        build-essential \
                                        python3-pip \
                                        python3-dev \
                                        python3-distutils \
                                        python3-pkg-resources \
                                        python3-tk \
                                        libmariadb-dev




COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 7000
EXPOSE 80
EXPOSE 3306

WORKDIR /app
COPY src/ .

CMD exec gunicorn --bind 0.0.0.0:80 --timeout=300 main:app