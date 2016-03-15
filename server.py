#!/usr/bin/python
from datetime import datetime
from w2k203dpi import Printer
from flask import Flask, request

app = Flask(__name__)
p = Printer()

@app.route('/')
def root_get():
    return '<form method="post">\n<textarea name="txt" rows="10" cols="32"></textarea>\n<br>\n<input type="submit" value="Send"></form>\n'

@app.route('/', methods=['POST'])
def root_post():
    data = request.form
    txt = data['txt']
    print 'Received text:'
    print txt
    p.println(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    p.println()
    p.println(txt)
    p.println()
    p.println('-' * 32)
    return '<h1>Yummy!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
