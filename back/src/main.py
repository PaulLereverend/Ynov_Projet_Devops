# import pymysql
from app import app
from config import connection
from flask import jsonify, flash, request
from flask_restful import Resource, Api

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

@app.route('/automate', methods=['GET'])
def get_automate():
	# try:
		# with connection.cursor() as cursor:
		# 	# Create a new record
		# 	sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
		# 	cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

		# # connection is not autocommit by default. So you must commit to save
		# # your changes.
		# connection.commit()

		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `automate`"
			cursor.execute(sql)
			result = cursor.fetchone()
			print(result)
			return jsonify(result)
	# finally:
		# connection.close()
		
if __name__ == "__main__":
    app.run(debug=True)
