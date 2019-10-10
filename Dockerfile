#FROM tiangolo/#uwsgi-nginx-flask:python3.6-alpine3.7
#ADD BasicMath.py /
#ADD request.py /
#ADD requirements.txt /
#ADD restful_api.py /
#RUN pip install -r requirements.txt
#CMD [ "python", "./restful_api.py" ]
#CMD [ "python", "./request.py" ]
#https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
FROM ubuntu:18.04

#MAINTANER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "restful_api.py" ]

