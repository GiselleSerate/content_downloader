FROM python:2.7

LABEL description="PanOS - Dynamic Updates Content Downloader"
LABEL version="0.1"
LABEL maintainer="btorres-gil@paloaltonetworks.com"

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/content_downloader/

EXPOSE 5003

ENV FLASK_APP=/app/content_downloader/service.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]
