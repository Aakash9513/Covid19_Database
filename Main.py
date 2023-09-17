#covid-19 data maintanance or survey software code 
import  mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Covid19_Death_DB"
 )

mycursor=mydb.cursor()

#       Table - admin_db
#       Table - death_db
#       Table - affected_db


def main():
    print("Welcome to Covid19 database")
    print("1->User")
    print("2->Admin")

    User=int(input("Enter Your Choice"))
    if User==1:
        import User
        User.Main
    elif User==2:
        import Admin
        Admin.main_function()
    else :
        print("Pls Enter the number only")
main()
    