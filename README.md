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