FROM python:3.6
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www/app
COPY requirements.txt /var/www/app
RUN mkdir /var/www/logs/
RUN pip install -r requirements.txt