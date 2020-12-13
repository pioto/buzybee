from flask import Flask, request
app = Flask(__name__)


VALID_STATUS = {
    'unknown',
    'available',
    'busy',
    'away'
}
STATUS = 'unknown'


@app.route('/api/v1/status', methods=['GET', 'POST'])
def status():
    if request.method == 'POST':
        return update_status()
    else:
        return get_status()


def get_status():
    global STATUS
    return {"status": STATUS}


def update_status():
    global STATUS
    if valid_status(request.form['status']):
        STATUS = request.form['status']
        return get_status()
    else:
        return {"error": "Invalid Status"}


def valid_status(status):
    return status in VALID_STATUS


