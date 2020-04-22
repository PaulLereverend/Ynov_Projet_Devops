FROM python:3.7

ADD . /

RUN pip install -r requirements.txt
RUN ["chmod", "+x", "/start.sh"]
CMD [ "python", "./src/main.py" ]
