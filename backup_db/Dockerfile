FROM python:3.7

ADD . /

ENV TZ=Europe/Paris

RUN apt-get update \
    && apt-get install -y cron \
    && apt-get install -y mariadb-client \
    && apt-get autoremove -y

RUN touch /var/log/backup.log

COPY ./job /etc/cron.d/job
RUN chmod 0644 /etc/cron.d/job
RUN crontab /etc/cron.d/job

CMD cron -f