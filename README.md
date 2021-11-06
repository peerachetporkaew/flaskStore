# flaskStore

# Dependencies
- Flask
- Peewee
- Fire

# Installation

```
pip install flask peewee fire
```

# Usage

To create your new DB.

```
rm product.db
python3 product.py create
python3 product.py add --id 0001 --name XiaoMi --price 12000
```

To run web server

```
export FLASK_APP=app
flask run
```

# Docker

To build docker image (flaskstore)

```
docker build -t flaskstore:latest .
```

To run docker

```
docker run -d -p 5000:5000 flaskstore
```

# Heroku

```
heroku login
heroku container:login
heroku create {appname}
heroku container:push web --app {appname}
heroku container:release web --app {appname}
heroku open --app {appname}
heroku logs --tail --app {appname}
```
