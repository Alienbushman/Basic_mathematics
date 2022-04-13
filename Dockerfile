FROM python:3
ADD basic_math.py /
ADD requirements.txt /
ADD restful_api.py /
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["restful_api.py"]
#CMD [ "python", "./restful_api.py" ]



#More thorough way of doing it
#https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
#FROM ubuntu:18.04
#RUN apt-get update -y && \    apt-get install -y python-pip python-dev
#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#COPY . /app
#ENTRYPOINT [ "python" ]
#CMD [ "restful_api.py" ]

