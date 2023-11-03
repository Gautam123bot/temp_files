import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gautam@123@mysql'
)

cursorObject = dataBase.cursor()

cursorObject.execute("SHOW DATABASES")

for x in cursorObject:
    print(x)
