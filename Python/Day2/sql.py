import  mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("INSERT INTO custmers(name,age) VALUES (%s,%s)",("Jack",20))
mydb.commit()
mycursor.execute("SELECT * FROM customers")
mydb close
