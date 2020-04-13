from app import app
from flask import flash, request
from config import connect
import json

@app.route('/automates', methods=['GET'])
def get_automates():
	if request.args.__len__() > 0:
		num_unite = request.args.get('num_unite')
		print(num_unite)
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM `automate` where unite_id = %s"
				cursor.execute(sql, num_unite)
				return json.dumps(cursor.fetchall())
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return json.dumps({})

@app.route('/automate/data', methods=['GET'])
def get_data():
	if request.args.__len__() > 0:
		num_automate = request.args.get('num_automate')
		date_fin = request.args.get('date_fin')
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM `automate` where automate_id = %s AND date < now() AND date > %s"
				cursor.execute(sql, (num_automate, date_fin))
				return json.dumps(cursor.fetchall())
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return json.dumps({})