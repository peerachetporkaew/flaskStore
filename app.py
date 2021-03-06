from flask import Flask, jsonify
from product import *
import os 

app = Flask(__name__)

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect():
    db.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

@app.route("/product")
def product_list():
    results = Product.select().dicts()

    for r in list(results):
        print(r)

    #return "HELLO"
    return jsonify({'rows':list(results)})

@app.route("/")
def index():
    return "HELLO WORLD"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))
