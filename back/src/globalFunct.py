import datetime
import json

def converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.timestamp()

def toJSON(data):
    return json.dumps(data, default=converter)