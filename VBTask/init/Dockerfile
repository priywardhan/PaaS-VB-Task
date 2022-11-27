FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip sshpass
ENV DEBIAN_FRONTEND=noninteractive
RUN apt install tzdata -y
RUN apt install  ansible -y
COPY init-playbook.yaml /tmp/init-playbook.yaml
COPY hosts /tmp/hosts
COPY run.sh /tmp/run.sh

CMD [ "sh /tmp/run.sh" ]