#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoDesk programming assessment
@author: drosales
"""
import requests
from flask import Flask, request
import logging
DEBUG = 0

log = logging.getLogger('werkzeug')
log.setLevel(logging.NOTSET)

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def endpointRequest():
   if request.method == 'GET':
       r = requests.get('https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases')
       d = r.json()
       return d

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
    if DEBUG == 1:
        app.debug=True
    app.run()