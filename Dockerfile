FROM python:2.7

LABEL description="PanOS - Dynamic Updates Content Downloader"
LABEL version="0.7"
LABEL maintainer="btorres-gil@paloaltonetworks.com"

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /var/tmp/content_updates/
COPY . /app/content_downloader/

EXPOSE 5003

ENV FLASK_APP=/app/content_downloader/service.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]
