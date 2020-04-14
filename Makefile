link:
	ln -s /home/vagrant/dev/workScheder/gunicorn.conf    /etc/nginx/conf.d/gunicorn.conf
	ln -s /home/vagrant/dev/workScheder/gunicorn.service /etc/systemd/system/gunicorn.service
	ln -s /home/vagrant/dev/workScheder/gunicorn.socket  /etc/systemd/system/gunicorn.socket

unlink:
	unlink /etc/nginx/conf.d/gunicorn.conf
	unlink /etc/systemd/system/gunicorn.service
	unlink /etc/systemd/system/gunicorn.socket
