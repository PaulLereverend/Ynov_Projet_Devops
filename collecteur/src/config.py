import pymysql


def connect():
    return pymysql.connect(host='db', port=306, user='user', password='password', db='devops', cursorclass=pymysql.cursors.DictCursor)


address = ""
port = 1111
