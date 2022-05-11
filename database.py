import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285')
cursor = con.cursor()

if con.is_connected():
    print("Connect successfully!!")