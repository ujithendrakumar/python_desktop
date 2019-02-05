import connection as db
from connection import connect

connec = connect
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jithendra Kumar", "Highway 21")
connec.mycursor.execute(sql, val)
connec.commit()
print(connec.rowcount, "record inserted.")