import requests
import json
from flask import Flask, request
import main

with open("./config.json")as config:
    config_data = json.load(config)
    get_host = config_data["get_address"]["host"]
    get_port = config_data["get_address"]["port"]

app = Flask(__name__)
@app.route('/', methods = ['post'])

def post():
    t = request.get_json()
    main.process_msg(t)
    return 'OK'

app.run(host = get_host, port = get_port, debug = 'Ture') #接收post的地址

