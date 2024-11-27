import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1993"
)

#prepare a cursor object
cursor = dataBase.cursor()

# Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS  elderco")

print("All Done")