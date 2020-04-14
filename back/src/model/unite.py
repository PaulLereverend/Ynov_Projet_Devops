from app import app
from flask import flash, request
from config import connect
import json
from flask_cors import CORS, cross_origin

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/unites', methods=['GET'])
@cross_origin()
def get_unites():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `unite`"
            cursor.execute(sql)
            return json.dumps(cursor.fetchall())
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()

    return json.dumps({})
