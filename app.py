#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "fdaadverseevents":
        return {}
    baseurl = "https://api.fda.gov/drug/event.json?"
    event.json_query = makeEvent.jsonQuery(req)
    if event.json_query is None:
        return {}
    event.json_url = baseurl + urlencode({'q': event.json_query}) + "&format=json"
    result = urlopen(event.json_url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


def makeEvent.jsonQuery(req):
    result = req.get("result")
    


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    
    # print(json.dumps(item, indent=4))

    speech = "Total adverse event count is " + query.get('result') 

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "test"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
