FROM debian

COPY server.py /opt/server.py
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install flask-restful jsonify requests
COPY server.py /tmp/server.py
COPY template /tmp/template
CMD python3 /tmp/server.py