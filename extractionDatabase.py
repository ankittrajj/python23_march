import mysql.connector as c
con = c.connect(host= 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'xyz')

cursor = con.cursor()

query = "select * from abc"
cursor.execute(query)

# fetch one
# fetch many
# fetch all
# data = cursor.fetchone()
# data = cursor.fetchmany(3)
data = cursor.fetchall()
print(data)

