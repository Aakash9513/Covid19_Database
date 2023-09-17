import  mysql.connector
import sys
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Covid19_Death_DB"
 )

mycursor=mydb.cursor()


def authenticateion_admin():
    admin_id = int(input("Enter your Admin ID: "))
    pin = int(input("Enter your PIN: "))

    sql = "SELECT * FROM Admin_db WHERE admin_ID = %s AND pin = %s"
    mycursor.execute(sql, (admin_id, pin))
    user = mycursor.fetchone()

    if user:
        return user
    else:
        print("Authentication failed. Please try again.")
        return None


# Death

def View_Data_death():
    
    query = "SELECT * FROM death_db"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)


def Add_Data_Dead():

    sql="insert into death_db (S_No,ID_NO,Name,Status,symptoms,Date_of_Death) values (%s,%s,%s,%s,%s,%s)"
    print("****Add Death Data****")
    S_No=int(input("Enter the S.No"))
    ID_NO=int(input("Enter the ID_NO"))
    Name=input("Enter the Name")
    Status=input("Enter the Status")
    symptoms=input("Enter the symptoms")
    Date_of_Death=input("Enter the Date_of_Death")
    values=(S_No,ID_NO,Name,Status,symptoms,Date_of_Death)
    mycursor=mydb.cursor(sql,values)      
    mycursor.execute(sql,values)
    mydb.commit()
    print("********filesave*********")

    mycursor.execute("select * from death_db")

    myresult=mycursor.fetchall()

    for i in myresult:
        print(i)


def Remove_Data_Dead():
    sql="delete from death_db WHERE ID_NO = %s"
    ID_NO=int(input("Enter the ID_NO"))
    values=(ID_NO,)     
    mycursor.execute(sql,values)
    mydb.commit()
    print("********filesave*********")

    mycursor.execute("select * from death_db")

    myresult=mycursor.fetchall()

    for i in myresult:
        print(i)


def Data_Dead():
    print("1->Add Data Dead")
    print("2->Remove Data Dead")
    print("3->View Data Dead")
    print("4->EXIT")
    user_choice = int(input("Enter your choice number: "))
    if user_choice == 1:  
        Add_Data_Dead()    
    elif user_choice == 2:
        Remove_Data_Dead()
    elif user_choice == 3:
        View_Data_death()
    else:
        sys.exit()


# Affected

def View_Data_Affected():
    
    query = "SELECT * FROM affected_db"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)


def Add_Data_Affected():

    sql="insert into affected_db (S_No,ID_NO,Name,Status,symptoms,Date_of_Admission) values (%s,%s,%s,%s,%s,%s)"
    print("****Add Death Data****")
    S_No=(input("Enter the S.No"))
    ID_NO=(input("Enter the ID_NO"))
    Name=input("Enter the Name")
    Status=input("Enter the Status")
    symptoms=input("Enter the symptoms")
    Date_of_Admission=input("Enter the Date_of_Admission")
    values=(S_No,ID_NO,Name,Status,symptoms,Date_of_Admission)
    mycursor=mydb.cursor(sql,values)      
    mycursor.execute(sql,values)
    mydb.commit()
    print("********filesave*********")

    mycursor.execute("select * from affected_db")

    myresult=mycursor.fetchall()

    for i in myresult:
        print(i)


def Remove_Data_Affected():
    sql="delete from affected_db WHERE ID_NO = %s"
    ID_NO=int(input("Enter the ID_NO"))
    values=(ID_NO,)    
    mycursor.execute(sql,values)
    mydb.commit()
    print("********filesave*********")

    mycursor.execute("select * from affected_db")

    myresult=mycursor.fetchall()

    for i in myresult:
        print(i)


def Data_Affected():
    print("1->AddData Affected")
    print("2->Remove Data Affected")
    print("3->View Data Affected")
    print("4->EXIT")
    user_choice = int(input("Enter your choice number: "))
    if user_choice == 1:  
        Add_Data_Dead()    
    elif user_choice == 2:
        Remove_Data_Dead()
    elif user_choice == 3:
        View_Data_death()
    else:
        sys.exit()

def main_function():
    print("Covid19 Data Base")
    user = None

    while not user:
        user = authenticateion_admin()

    while True:
        print("1->Data Dead")
        print("2->Data Affected")
        print("3->Exit")

        try:
            user_choice = int(input("Enter your choice number: "))
            if user_choice == 1:  
                Data_Dead()    
            elif user_choice == 2:
                Data_Affected()
            elif user_choice == 3:
                sys.exit()
            else:
                print("Type only 1, 2, 3.")
        except ValueError:
            print("Please type a number only.")

if __name__ == "__main__":
    main_function()