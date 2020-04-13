from app import app
from flask import jsonify, flash, request
from config import connect

@app.route('/unites', methods=['GET'])
def get_unites():
	connection = connect()
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `unite`"
			cursor.execute(sql)
			res = {
				'data' : cursor.fetchall(),
				'status' : 200
			}
			return jsonify(res)
	finally:
		if cursor != None:
			cursor.close()
		if connection != None:
			connection.close()
	
	res = {
		'data' : [],
		'status' : 204
	}
	return jsonify(res)