#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoDesk programming assessment
@author: drosales
"""
import requests
from flask import Flask, request
import logging
import json

#Add config for url, Debug mode and logfile
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
url = data['url']
debug = data['DEBUG']
logfile = data['logfile']
    
app = Flask(__name__)

#setup logging settings before the first request
@app.before_first_request
def before_first_request():
    
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
        
    if debug == 1:
        logsetting=logging.DEBUG
    else:
        logsetting=logging.CRITICAL
        
    handler = logging.FileHandler(logfile)
    handler.setLevel(logsetting)
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(module)s: %(message)s",
                          datefmt="%H:%M:%S")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logsetting)

#Route GET request to endpoint
@app.route("/", methods = ['GET'])
def endpointRequest():
   
    app.logger.info('Get Request INITIATED')
    
    if request.method == 'GET':
        try:
            r = requests.get(url)
            app.logger.info('Get request SUCCEEDED.')
            d = r.json()
            return d
        except:
            app.logger.error('Get request FAILED.')

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
