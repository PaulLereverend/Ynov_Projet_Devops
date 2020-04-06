from app import app
from flask import jsonify, flash, request
from config import connect

@app.route('/unites', methods=['GET'])
def get_unites():
	try:
		connection = connect()
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `unite`"
			cursor.execute(sql)
			result = cursor.fetchall()
			print(result)
			return jsonify(result)
	finally:
		if cursor != None:
			cursor.close()
		if connection != None:
			connection.close()