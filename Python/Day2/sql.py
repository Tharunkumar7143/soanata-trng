import  pyodbc
mydb = pyodbc.connect(host="localhost",user="SONATA\hydtrng",passwd="Son@trng1",database="python")
mycursor =pyodbc.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("gdsgdfgfdg", "Hyd")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
print("Name |  Address")
for x in myresult:
  print(x[0] +" | " + x[1])
  print(type(x))