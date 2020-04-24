import pymysql

def connect():
	return pymysql.connect(host='cloudnantespaul.freeboxos.fr', port=3390, user='ynov_devops', password='ynov_devops', db='ynov_devops', cursorclass=pymysql.cursors.DictCursor)

address = ""
port = 1111