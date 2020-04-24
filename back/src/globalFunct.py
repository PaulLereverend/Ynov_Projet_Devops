import datetime
import json
from app import app

def converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return int(round(o.timestamp()))

def makeResponse(data):
    response = app.response_class(
        response=json.dumps(data, default=converter),
        status=200,
        mimetype='application/json'
    )
    return response