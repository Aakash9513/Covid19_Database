import  mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Covid19_Death_DB"
 )

mycursor=mydb.cursor()


def View_Data_death():
    
    query = "SELECT * FROM death_db"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def View_Data_Affected():
    
    query = "SELECT * FROM affected_db"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def Main():

    print("###Welcome to Covid19 Database###")
    print('1->View Death Database')
    print('2->View Affected Database')

    user = int(input("Enter Your Choice :"))
    if user==1:
        View_Data_death()
    elif user==2:
        View_Data_Affected()

Main()