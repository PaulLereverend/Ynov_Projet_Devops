from app import app
from config import connect
from globalFunct import toJSON

@app.route('/unites', methods=['GET'])
def get_unites():
	connection = connect()
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `unite`"
			cursor.execute(sql)
			return toJSON(cursor.fetchall())
	finally:
		if cursor != None:
			cursor.close()
		if connection != None:
			connection.close()
	
	return toJSON({})