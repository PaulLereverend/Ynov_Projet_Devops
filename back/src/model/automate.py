from app import app
from flask import request
from config import connect
from globalFunct import toJSON

@app.route('/automates', methods=['GET'])
def get_automates():
	if request.args.__len__() > 0:
		num_unite = request.args.get('num_unite')
		print(num_unite)
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT DISTINCT automate_id FROM `automate` where unite_id = %s"
				cursor.execute(sql, num_unite)
				return toJSON(cursor.fetchall())
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return toJSON({})


@app.route('/automate/data', methods=['GET'])
def get_data():
	if request.args.__len__() > 0:
		num_automate = request.args.get('num_automate')
		date_fin = request.args.get('date_fin')
		unite_id = request.args.get('unite_id')
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM `automate` where unite_id = %s AND automate_id = %s AND date > %s"
				cursor.execute(sql, (unite_id, num_automate, date_fin))
				return toJSON(cursor.fetchall())
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return toJSON({})