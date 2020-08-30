# -*- coding: utf-8 -*-

from bottle import route, run, view, static_file
import os
import serial


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

@route('/static/<filepath:path>')
def server_static(filepath):
    """Handler for static files, used with the development server.
    When running under a production server such as IIS or Apache,
    the server should be configured to serve the static files."""
    return static_file(filepath, root=STATIC_ROOT)

@route('/')
@view('index')
def index():
    return dict(
        title='電波遮断'
    )

def send_serial(data):
    try:
        device = serial.Serial("/dev/ttyUSB0", 115200)
    except:
        return False

    device.write(data + "\n")
    line = ""
    while True:
        chars = device.read()
        if chars == "\n":
            break
        line += chars

    device.close()

    if line != "OK":
        return False

    return True

@route('/on', method='GET')
def on():
    if send_serial("ON") == False:
        return 1

    return 0

@route('/off', method='GET')
def off():
    if send_serial("OFF") == False:
        return 1

    return 0


run(host='0.0.0.0', port=80, debug=False, reloader=False)
