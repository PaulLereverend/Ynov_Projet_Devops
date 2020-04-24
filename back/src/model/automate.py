from app import app
from flask import request
from config import connect
from globalFunct import makeResponse

@app.route('/automates', methods=['GET'])
def get_automates():
	if request.args.__len__() > 0:
		num_unite = request.args.get('num_unite')
		print(num_unite)
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT DISTINCT automate_id FROM data where unite_id = %s"
				cursor.execute(sql, num_unite)
				return makeResponse(cursor.fetchall())
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return makeResponse({})


@app.route('/automate/data', methods=['GET'])
def get_data():
	if request.args.__len__() > 0:
		num_automate = request.args.get('num_automate')
		date_fin = request.args.get('date_fin')
		unite_id = request.args.get('unite_id')
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM data where unite_id = %s AND automate_id = %s AND date_prise > CONVERT_TZ(FROM_UNIXTIME(%s),'+00:00','-02:00')"
				cursor.execute(sql, (unite_id, num_automate, date_fin))
				data = cursor.fetchall()
				for i in range(len(data)):
					if i-1 >= 0:
						data[i]['poids_prod_fini'] = data[i]['poids_lait']-data[i-1]['poids_lait']
					else:
						data[i]['poids_prod_fini'] = 0
				return makeResponse(data)
		finally:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
	return makeResponse({})