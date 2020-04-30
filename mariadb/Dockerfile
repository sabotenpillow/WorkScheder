FROM mariadb:10.4.12

MAINTAINER qtooone

EXPOSE 3306

ENV MYSQL_ROOT_PASSWORD mariadb
ENV MYSQL_USER          django
ENV MYSQL_PASSWORD      django
ENV MYSQL_DATABASE      django_scheduler

RUN users
#RUN service mysql status
#    && mariadb -e "create user django@localhost" \
#    && mariadb -e "set password for django@localhost=password('django')" \
#    && mariadb -e "create database django_scheduler" \
#    && mariadb -e "grant all privileges on django_scheduler.* to django@localhost"
