# import socket
#
#
# sock = socket()
#
# sock.bind(('localhost', 9091))
# sock.listen(1)
# conn, addr = sock.accept()
# print('point')
#
# while True:
#     data = conn.recv(1024)
#     if not data:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/123')
def hello_123():
    return '<p>123!</p>'