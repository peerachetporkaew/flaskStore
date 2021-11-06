FROM ubuntu:18.04
MAINTAINER Peerachet Porkaew "peerachet.porkaew@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN export FLASK_APP=app
ENTRYPOINT [ "flask" ]
CMD ["run","--host","0.0.0.0"]

