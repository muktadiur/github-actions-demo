from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s, /%(funcName)s  %(message)s', filemode='w')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    data = {
        "result": "OK - healthy"
    }
    resp = jsonify(data)
    resp.status_code = 200
    logging.debug('endpoint was reached')
    return resp

@app.route("/metrics")
def metrics():
    data = {
        'data': {
            'UserCount': 140, 
            'UserCountActive': 23
        }
    }
    resp = jsonify(data)
    resp.status_code = 200
    logging.debug('endpoint was reached')
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')

