from app import app
from flask import flash, request
from config import connect
import datetime
import json

def converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.timestamp()

@app.route('/unites', methods=['GET'])
def get_unites():
	connection = connect()
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `unite`"
			cursor.execute(sql)
			return json.dumps(cursor.fetchall(), default=converter)
	finally:
		if cursor != None:
			cursor.close()
		if connection != None:
			connection.close()
	
	return json.dumps({})