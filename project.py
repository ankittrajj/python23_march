# connection

import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'hdfcbank' )

cursor = con.cursor()

# create a menu
# 1 open acc
# 2 cash depo
# 3 cash withdrwal
# 4. Acc details
# 5.Exit

choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5 Exit")


# code for open account---->
# name
# age
# contact
# print("Account open successfully!!)

if choice == '1':
    name = input("Enter the name")
    age = int(input("enter the age"))
    mobile = int(input("Enter the phone number"))
    query = "Insert into cust2 values('{}',{},{})".format(name,age,mobile)
    cursor.execute(query)
    con.commit()

    print("Account Open Successfully")

# cash deposit
# name
# deposit amount
# print(amount deposited!!)

# try to write the code for the next options.