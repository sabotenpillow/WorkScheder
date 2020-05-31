## Init
<hr>

### set file & directory
- Scheduler/.env
- Scheduler/accounts/fixtures/init_users.json

<!--
### install Python library
```
pip install -r Scheduler/requirements.txt
```
-->

### install Node modules
```
cd Scheduler/WorkScheder/; npm install
```

### collect static
```
make manage.py DJANGO_CMD=collectstatic
```

## Start

```
docker-compose up -d
```

## Dependencies
<hr>

- python3
- libmysqlclient-dev (Ubuntu)
- npm
- docker
- docker-compose

execute the followings (on ubuntu):
```
sudo apt install python3 libmysqlclient-dev npm docker docker-compose
```
