import json
import os
import urllib2

from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('message_form.html')


@app.route('/send', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':
        message = request.form['message']

        headers = {
            'Content-type': "application/json"
        }

        data = json.dumps({
            "text": message
        })

        # specific for slackbot
        webhook_url = os.env['WEBHOOK_URL']

        req = urllib2.Request(webhook_url, headers=headers, data=data)
        resp = urllib2.urlopen(req)
        print resp.read()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
