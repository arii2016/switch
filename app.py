# -*- coding: utf-8 -*-

from bottle import route, run, view, static_file
import os, time
import serial
import threading


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
    device.write(data)
    line = ""
    timeout = time.time()
    while True:
        if (time.time() - timeout) > 2.0:
            return False
        chars = device.read()
        if chars == "\n":
            break
        line += chars

    if line != "OK":
        return False

    return True


def f():
    time.sleep(600)
    send_serial("OFF\n")
    lock.release()

@route('/on', method='GET')
def on():
    if send_serial("ON\n") == False:
        return 1

    if lock.acquire(False):
        th = threading.Thread(target=f)
        th.start()

    return 0

@route('/off', method='GET')
def off():
    if send_serial("OFF\n") == False:
        return 1

    return 0


device = serial.Serial("/dev/ttyUSB0", 115200, timeout=1, writeTimeout=0.1)
# device = serial.Serial("/dev/cu.usbserial-14210", 115200, timeout=1, writeTimeout=0.1)

lock = threading.Lock()

run(host='0.0.0.0', port=80, debug=False, reloader=False)

device.close()
