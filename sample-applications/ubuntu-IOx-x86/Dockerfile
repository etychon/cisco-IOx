FROM ubuntu:20.04

RUN apt-get update && apt-get install -y openssh-server curl libcurl4-openssl-dev build-essential cmake git python2.7-dev libboost-python-dev joe python3-pip
RUN pip3 install azure-iot-device

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /root/.ssh

RUN git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
