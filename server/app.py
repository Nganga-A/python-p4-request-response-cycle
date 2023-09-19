#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g,make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# @app.route('/')
# def index():
#     host = request.headers.get('Host')
#     appname = current_app.name
#     return f''' <h1>The host for this page is {host}</h1>
#                 <h2>The name of this application is {appname}</h2>
#                 <h3>The path of this application on the user's device is {g.path}</h3>''', \
#                 202

# # There is a third, optional argument that can be added in to create headers for our response. This is simply a dictionary with keys for the header attributes mapped to their respective values.


@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

# Flask also provides us two unique objects that allow us to manipulate request data more effectively:
# - g is an object that can be used to store anything that you want to store globally for the lifetime of a request. It is reset with each new request.
# - session is a dictionary object that can be used to hold onto values between multiple requests.

