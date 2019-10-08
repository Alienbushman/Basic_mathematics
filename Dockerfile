FROM python:3
ADD BasicMath.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./BasicMath.py" ]
