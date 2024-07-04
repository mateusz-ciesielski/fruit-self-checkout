FROM python:3.11

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt

COPY main.py /opt/app/
COPY frontend.py /opt/app/
COPY start.sh /opt/app/
COPY static /opt/app/static


ENTRYPOINT /opt/app/start.sh prod