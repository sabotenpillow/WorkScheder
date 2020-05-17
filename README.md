## init
<hr>

### set file & directory
- Scheduler/.env
- mariadb/django_scheduler_init.sql
- `mkdir mariadb/mariadb_data`

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
make manage.py collectstatic
```

## dependencies
<hr>

- npm
- docker
- docker-compose
