DJANGO_CMD = ''

link:
	ln -s /home/vagrant/dev/workScheder/nginx/gunicorn.conf        /etc/nginx/conf.d/gunicorn.conf
	ln -s /home/vagrant/dev/workScheder/Scheduler/gunicorn.service /etc/systemd/system/gunicorn.service
	ln -s /home/vagrant/dev/workScheder/Scheduler/gunicorn.socket  /etc/systemd/system/gunicorn.socket

unlink:
	unlink /etc/nginx/conf.d/gunicorn.conf
	unlink /etc/systemd/system/gunicorn.service
	unlink /etc/systemd/system/gunicorn.socket

restart-services:
	systemctl restart nginx.service
	systemctl restart gunicorn.service
	systemctl restart gunicorn.socket

collectstatic:
	cd Scheduler/; \
	python3 manage.py collectstatic --noinput --clear > /dev/null; \
	python3 manage.py collectstatic --noinput > /dev/null

manage.py:
	env DJANGO_READ_ENV_FILE=true DJANGO_ENVIRONMENT='development' python3 Scheduler/manage.py $(DJANGO_CMD)
