import requests
from flask import Flask, request
import main

app = Flask(__name__)
@app.route('/', methods = ['post'])

def post():
    t = request.get_json()
    main.process_msg(t)
    return 'OK'

app.run(host = '192.168.0.100', port = '5701', debug = 'Ture') #接收post的地址

