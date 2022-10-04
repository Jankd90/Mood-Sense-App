import time
from datetime import datetime
from flask import Flask, escape, request, render_template
from influxdb import InfluxDBClient
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

HOST = os.environ.get("HOST")
INFLUXDB = os.environ.get("INFLUXDB")
print(INFLUXDB)
app = Flask(__name__)

@app.route('/')
def annotate():
    return render_template("annotate.html", hostname=HOST)
@app.route('/en')
def annotate_en():
    return render_template("annotate-en.html", hostname=HOST)

@app.route('/post')
def post():
    value = request.args.get('button')
    #print(value)

    timestamp = int(time.time()*1000000000)
    #dt_object = datetime.fromtimestamp(timestamp)
    json_body = [
    {
        "measurement": "annotation-{}".format(request.remote_addr),
        "tags": {
            "host": "server01",
            "region": "assen"
        },
        "time": timestamp,
        "fields": {
            "value": value
        }
    }
    ]
    #print(timestamp)
    #print(value)
    client = InfluxDBClient(INFLUXDB, 8086, 'moodsense', 'MoodSense-Group2', 'homeassistant')
    client.write_points(json_body)
    return f'Hello!'

@app.route('/recording',methods = ['POST'])
def record():
    #print(request.data)
    name = '{}-assesment.wav'.format(int(time.time()))
    f = open(name, 'wb')
    f.write(request.data)
    f.close()
    return f'Hello!'

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8100, ssl_context=('server.crt', 'server.key'))
    #app.run('0.0.0.0', debug=True, port=8100, ssl_context=('host.cert', 'host.key'))
