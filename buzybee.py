import mmap

from flask import Flask, request
app = Flask(__name__)


class Status:
    def __init__(self, code, color):
        self.code = code
        self.color = color


class Screen:
    def __init__(self, fbdev, xsize, ysize, bytes_per_pixel):
        self.fbdev = fbdev
        self.xsize = xsize
        self.ysize = ysize
        self.bytes_per_pixel = bytes_per_pixel
        self.fbsize = xsize * ysize * bytes_per_pixel

    def fill(self, pixel_bytes):
        screenbuf = pixel_bytes * self.xsize * self.ysize
        with open(self.fbdev, 'r+b') as f:
            mm = mmap.mmap(f.fileno(), self.fbsize)
            mm.write(screenbuf)


# status choices
VALID_STATUS = {
    'unknown': Status('unknown', b'\x00\x00'), # black
    'available': Status('available', b'\xe0\x07'), # green
    'busy': Status('busy', b'\x00\xf8'), # red
    'away': Status('away', b'\xe0\xff') # yellow
}
# Current presence status (global variable)
STATUS = VALID_STATUS['unknown']

SCREEN = Screen('/dev/fb1', 240, 320, 2) # hard coded values for my Adafruit PiTFT 2.8"
SCREEN.fill(STATUS.color)


@app.route('/api/v1/status', methods=['GET', 'POST'])
def status():
    if request.method == 'POST':
        return update_status()
    else:
        return get_status()


def get_status():
    global STATUS
    return {"status": STATUS.code}


def update_status():
    global STATUS
    if valid_status(request.form['status']):
        STATUS = VALID_STATUS[request.form['status']]
        fill_screen(STATUS.color)
        return get_status()
    else:
        return {"error": "Invalid Status"}

def fill_screen(color):
    global SCREEN
    SCREEN.fill(color)


def valid_status(status):
    return status in VALID_STATUS


