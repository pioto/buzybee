# BuzyBee: A Raspberry Pi Office Status Indicator

This is a project to try to build out a simple little office status indicator
using my Raspberry Pi. I'm using a Raspberry Pi Model B+, with an Adafruiit
PiTFT as my display, mostly because that's what I have lying around.

## Setup

After cloning the repo:

```
python3 -m venv venv
. venv/bin/activate
pip install flask
export FLASK_APP=buzybee.py
export FLASK_ENV=development
flask run --host=0.0.0.0
```
