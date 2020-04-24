import pymysql


def connect():
    return pymysql.connect(host='db', port=3306, user='user', password='password', db='devops', cursorclass=pymysql.cursors.DictCursor)
