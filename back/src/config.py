from app import app
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='cloudnantespaul.freeboxos.fr', port=3390, user='ynov_devops', password='ynov_devops', db='ynov_devops')