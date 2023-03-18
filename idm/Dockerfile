FROM python:3.6
RUN apt-get update
RUN mkdir /server
WORKDIR /server
COPY ./idm /server
COPY ./lib/* /server/lib/
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
CMD python3 idm-server.py
