import mysql.connector

from configs.config import DB_HOST, DB_NAME, DB_PWD, DB_USER

def connectDB():
    db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PWD,
    database=DB_NAME
    )
    return db