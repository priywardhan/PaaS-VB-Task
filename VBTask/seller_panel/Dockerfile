FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install flask-restful requests
COPY server.py /tmp/server.py
COPY template tmp/template
CMD python3 /tmp/server.py