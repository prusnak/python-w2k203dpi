class Printer:

    def __init__(self):
        DEVPATH = '/dev/usb/lp0'
        self.f = open(DEVPATH, 'w')
        self.mode = 0x00

    def raw(self, data):
        for i in data:
           self.f.write(i)
        self.f.flush()

    def esc(self, data):
        self.raw('\x1b' + data)

    def font(self, value):
        if value:
            self.mode |= (1 << 0)
        else:
            self.mode &= ~(1 << 0)
        self.esc('!' + chr(self.mode))

    def bold(self, value):
        if value:
            self.mode |= (1 << 3)
        else:
            self.mode &= ~(1 << 3)
        self.esc('!' + chr(self.mode))

    def dblheight(self, value):
        if value:
            self.mode |= (1 << 4)
        else:
            self.mode &= ~(1 << 4)
        self.esc('!' + chr(self.mode))

    def dblwidth(self, value):
        if value:
            self.mode |= (1 << 5)
        else:
            self.mode &= ~(1 << 5)
        self.esc('!' + chr(self.mode))

    def underline(self, value):
        if value:
            self.mode |= (1 << 7)
        else:
            self.mode &= ~(1 << 7)
        self.esc('!' + chr(self.mode))

    def partialcut(self):
        for i in range(3): self.println()
        self.esc('m')

    def fullcut(self):
        for i in range(3): self.println()
        self.esc('i')

    def println(self, s = ''):
        self.f.write(s + '\n')
        self.f.flush()

    def qrcode(self, data, pixelsize = 8):
        correction = 0   # 0 = L, 1 = M, 2 = Q, 3 = H
        version = 0      # model/version
        mask = 0         # mask pattern
        datalen = len(data)
        self.esc('\x71' + chr(pixelsize) + chr(correction) + chr(version) + chr(mask) + chr(datalen % 256) + chr(datalen / 256) + data)
        self.println()
