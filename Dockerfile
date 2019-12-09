FROM python:3
MAINTAINER Kikki Hiiri "kikki@kikki.fi"
ADD run.py /
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=application
COPY . /app
RUN flask-init-db
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
