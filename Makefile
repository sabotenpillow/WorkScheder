link:
	ln -s /home/vagrant/dev/workScheder/gunicorn.conf    /etc/nginx/conf.d/gunicorn.conf
	ln -s /home/vagrant/dev/workScheder/gunicorn.service /etc/systemd/system/gunicorn.service
	ln -s /home/vagrant/dev/workScheder/gunicorn.socket  /etc/systemd/system/gunicorn.socket

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
	python manage.py collectstatic --noinput --clear > /dev/null; \
	python manage.py collectstatic --noinput > /dev/null

runserver:
	env DJANGO_READ_ENV_FILE=true python Scheduler/manage.py runserver 0:8800

