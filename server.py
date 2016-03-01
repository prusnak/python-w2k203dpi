#!/usr/bin/python
from w2k203dpi import Printer
from flask import Flask, request

app = Flask(__name__)
p = Printer()

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        data = request.form
        txt = '\n\n' + data['txt'] + '\n\n'
        p.println(txt)
        p.fullcut()
    return '<form method="post">\n<textarea name="txt" rows="5" cols="40"></textarea>\n<br>\n<input type="submit" value="Send"></form>\n'

if __name__ == '__main__':
    app.run()
