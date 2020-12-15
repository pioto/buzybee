from flask import Flask, request
app = Flask(__name__)


class Status:
    def __init__(self, code, color):
        self.code = code
        self.color = color


VALID_STATUS = {
    'unknown': Status('unknown', b'\x00\x00'),
    'available': Status('available', b'\x00\x00'),
    'busy': Status('busy', b'\x00\x00'),
    'away': Status('away', b'\x00\x00')
}
STATUS = VALID_STATUS['unknown']


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
        return get_status()
    else:
        return {"error": "Invalid Status"}


def valid_status(status):
    return status in VALID_STATUS


