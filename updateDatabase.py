import mysql.connector as c
con = c.connect(host= 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'xyz')

cursor = con.cursor()

name = input("Enter the name ")
age = int(input("Enter the age"))

query = "Update abc set name = '{}' where age = {}".format(name,age)
query = "Delete from abc where age = {}".format(age)
cursor.execute(query)
con.commit()
print("Data Updated!!")
