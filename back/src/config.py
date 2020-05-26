import pymysql


def connect():
    return pymysql.connect(host='db', port=3306, user='back', password='backpwd', db='devops', cursorclass=pymysql.cursors.DictCursor)
