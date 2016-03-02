#!/usr/bin/python
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
    p.println(txt)
    p.fullcut()
    return '<h1>Yummy!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
