#!/usr/bin/python
from w2k203dpi import Printer

p = Printer()

p.println('test')

p.bold(True)
p.println('test')
p.bold(False)

p.underline(True)
p.println('test')
p.underline(False)

p.qrcode('test')

p.fullcut()
