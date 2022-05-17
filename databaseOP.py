import mysql.connector as c
con = c.connect(host= 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'xyz')

cursor = con.cursor()

# if con.is_connected():
#     print("Connection Successfully!!")
while True:
# name,age,salary
    name = input("Enter the name ")
    age = int(input("Enter the age"))
    salary = int(input("Enter the salary"))


    query = "Insert into abc values('{}',{},{})".format(name,age,salary)
    # query = "Upadate abc set name={} where age = {}".format(name,age)
    cursor.execute(query)
    con.commit()

    print("Data Created Successfully!!")

    choice = input("1. Enter more data\n2. Exit")
    if choice == "2":
        break


