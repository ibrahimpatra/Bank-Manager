import sqlite3


def delaccount():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    cursor.execute(sql, (account_no,))
    data = cursor.fetchall()
    if data:
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ACCOUNT WHERE ACCOUNT_NO = ?", (account_no,))
        connection.commit()
        connection.close()
    else:
        print("Sorry ! Account Information NOT Found , Please Try Again ! ")


def admin():
    global adid
    global pwd
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    adid = input("Please Enter Admin ID : ")
    pwd = input("Please Enter Password: ")
    sql = "SELECT * FROM ADMIN WHERE ADMINID = ? AND PASSWORD = ?"
    values = (adid, pwd,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        return 1
    else:
        return 0


def newadmin():
    global adid
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    createTable = """   CREATE TABLE IF NOT EXISTS ADMIN( ADMINID VARCHAR(10) PRIMARY KEY  ,PASSWORD VARCHAR(10) NOT NULL , 
                        ADMNAME VARCHAR(30) NOT NULL,DESIGNATION VARCHAR(30)NOT NULL ,PHONE INT NOT NULL)  """
    cursor.execute(createTable)
    print("\nPlease Fill All The Information Carefully !")
    adid = input("Please Enter Admin ID u want : ")
    pwd = input("Please Enter password ")
    admname = input("Please Enter Admin Name : ")
    desig = input("Please Enter Admin Desig: ")
    phone = int(input("Please Enter Admin Contact No. : "))
    sql = f'INSERT INTO ADMIN VALUES(?,?,?,?,?) '
    values = (adid, pwd, admname, desig, phone, )
    cursor.execute(sql, values)
    cursor.execute("COMMIT")
    cursor.close()
    print("\nNew Admin Added Successfully !")


def alladmins():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    cursor.execute("SELECT * FROM ADMIN")
    data = cursor.fetchall()
    if data:
        print("\n*****DETAILS OF ALL ADMINS*****")
        print(data)
    else:
        print("Sorry ! No Admin Information , Please Try Again ! ")


def displayAllCustomer():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    data = cursor.fetchall()
    if data:
        print("\n*****DETAILS OF ALL NET BANKING CUSTOMERS*****")
        print("[{ACCOUNT_NO,CUSTOMER_ID,PASSWORD}]")
        print(data)
    else:
        print("Sorry ! No Record Found , Please Try Again ! ")


def searchCustomer():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    cid = input("Please Enter Net Banking Customer ID : ")
    sql = "SELECT * FROM CUSTOMER WHERE CID = ?"
    values = (cid,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        print("\n*****CUSTOMER DETAILS*****")
        print("[{ACCOUNT_NO,CUSTOMER_ID,PASSWORD}]")
        print(data)
    else:
        print("Sorry ! Customer NOT Found , Please Try Again ! ")


def newAccount():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    createTable = """CREATE TABLE IF NOT EXISTS ACCOUNT(ACCOUNT_NO INT PRIMARY KEY UNIQUE, 
                        ACCOUNT_TYPE VARCHAR(20) NOT NULL ,CNAME VARCHAR(30) NOT NULL ,ADDRESS VARCHAR(30)NOT NULL ,
                        PHONE INT NOT NULL,AMOUNT INT NOT NULL , PIN INT NOT NULL ) """
    cursor.execute(createTable)
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    account_type = input("PLEASE ENTER THE ACCOUNT TYPE [ S-SAVING / C - CURRENT : ")
    cname = input("Please Enter Customer Name : ")
    address = input("Please Enter Customer Address : ")
    phone = int(input("Please Enter Customer Contact No. : "))
    amount = int(input("PLEASE ENTER THE AMOUNT TO DEPOSIT : "))
    ATM_pin = int(input("PLEASE ENTER THE ATM PIN [ FOUR DIGITS ONLY ] : "))
    sql = 'INSERT INTO ACCOUNT (account_no,account_type,cname, address, phone, amount ,pin) VALUES(?,?,?,?,?,?,?)'
    values1 = (account_no, account_type, cname, address, phone,  amount, ATM_pin,)
    cursor.execute(sql, values1)
    cursor.execute("COMMIT")
    print("\nNew Account Opened Successfully !")


def displayAllAccounts():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    cursor.execute("SELECT * FROM ACCOUNT")
    data = cursor.fetchall()
    if data:
        print("\n*****DETAILS OF ALL CUSTOMER ACCOUNTS*****")
        print("[{ACCOUNT_NO,ACCOUNT_TYPE,NAME,ADDRESS,PHONE,AMOUNT,PIN}]")
        print(data, '\n')
    else:
        print("Sorry ! No Account Information , Please Try Again ! ")


def searchAccount():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    cursor.execute(sql, (account_no,))
    data = cursor.fetchall()
    if data:
        print("\n*****CUSTOMER ACCOUNT DETAILS*****")
        print("[{ACCOUNT_NO,ACCOUNT_TYPE,NAME,ADDRESS,PHONE,AMOUNT,PIN}]")
        print(data)
    else:
        print("Sorry ! Account Information NOT Found , Please Try Again ! ")


def update(ch, new):
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    cursor.execute(sql, (account_no,))
    data = cursor.fetchall()
    if data:
        if ch == 1:
            Connection = sqlite3.connect('data.db')
            cursor = Connection.cursor()
            sql = "UPDATE ACCOUNT SET CNAME = ? WHERE ACCOUNT_NO = ?"
            values = (new, account_no,)
            cursor.execute(sql, values)
            Connection.commit()
            Connection.close()
            print("Update Successful.")
        elif ch == 2:
            Connection = sqlite3.connect('data.db')
            cursor = Connection.cursor()
            sql = "UPDATE ACCOUNT SET ADDRESS = ? WHERE ACCOUNT_NO = ?"
            values = (new, account_no,)
            cursor.execute(sql, values)
            Connection.commit()
            Connection.close()
            print("Update Successful.")
        elif ch == 3:
            Connection = sqlite3.connect('data.db')
            cursor = Connection.cursor()
            sql = "UPDATE ACCOUNT SET PHONE = ? WHERE ACCOUNT_NO = ?"
            values = (new, account_no,)
            cursor.execute(sql, values)
            Connection.commit()
            Connection.close()
            print("Update Successful.")
        else:
            print("Sorry ! Account Information NOT Found , Please Try Again ! ")


def details():
    global cid
    global pwd
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    sql = """SELECT * FROM ACCOUNT, CUSTOMER 
            WHERE CID = ? AND PASSWORD = ? AND ACCOUNT.ACCOUNT_NO = CUSTOMER.ACCOUNT_NO"""
    values = (cid, pwd,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        print("[{ACCOUNT_NO,ACCOUNT_TYPE,NAME,ADDRESS,PHONE,AMOUNT,PIN,ACCOUNT_NO,CUSTOMER_ID,PASSWORD}]")
        print(data)
    else:
        return 0


def showbalance():
    global cid
    global pwd
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    sql = """SELECT AMOUNT FROM ACCOUNT, CUSTOMER WHERE CID = ? AND PASSWORD = ? 
            AND ACCOUNT.ACCOUNT_NO = CUSTOMER.ACCOUNT_NO"""
    values = (cid, pwd,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        print("Available Balance is - ")
        print(data)
    else:
        return 0



def customer():
    global cid
    global pwd
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    cid = input("Please Enter Customer ID : ")
    pwd = input("Please Enter Password: ")
    sql = "SELECT * FROM CUSTOMER WHERE CID = ? AND PASSWORD = ?"
    values = (cid, pwd,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        return 1
    else:
        return 0


def newCustomer():
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    values = (account_no,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        createTable = """  CREATE TABLE IF NOT EXISTS CUSTOMER(ACCOUNT_NO INT PRIMARY KEY UNIQUE , CID VARCHAR(10) UNIQUE,
                            PASSWORD VARCHAR(10) NOT NULL )  """
        cursor.execute(createTable)
        print("\nPlease Fill All The Information Carefully !")
        cid = input("Please Enter Customer ID u want : ")
        pwd = input("Enter password for net banking id : ")
        sql = f'INSERT INTO CUSTOMER VALUES(?,?,?) '
        values = (account_no, cid, pwd,)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nNew Customer Added Successfully !")
    else:
        exit("""Sorry you dont have account with us, please visit nearest branch or use admin menu to create your account. 
                Thankyou. 
                Visit Again.""")


def withdraw():
    count = 3
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    values = (account_no,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        while True:
             ATM_PIN = int(input("PLEASE ENTER THE ATM PIN - ONLY 3 ATTEMPTS ARE ALLOWED : "))
             sql = 'SELECT * FROM ACCOUNT WHERE PIN = ?'
             values = (ATM_PIN,)
             cursor.execute(sql, values)
             data = cursor.fetchall()
             if data:
                 amount=int(input("PLEASE ENTER AMOUNT TO WITHDRAW : "))
                 sql='UPDATE ACCOUNT SET AMOUNT = AMOUNT - ?'
                 cursor.execute(sql, (amount,))
                 cursor.execute("COMMIT")
                 print("******* TRANSACTION SUCCESSFULLY COMPLETED ! *******")
                 print("***** PLEASE TAKE MONEY AND REMOVE YOUR CARD ! *****")
                 break
             else:
                 print("Wrong Pin ! Please enter a Valid PIN")
                 count=count-1
                 print("You are left with only ", count, " Attempts")
                 if count == 0:
                    print("Your Card has been Blocked , Please Visit the Branch to activate it")
                 break
    else:
        print("Sorry ! Account Information NOT Found , Please Try Again ! ")


def show_balance():
    count = 3
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    values = (account_no,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        while True:
            ATM_PIN = int(input("PLEASE ENTER THE ATM PIN - ONLY 3 ATTEMPTS ARE ALLOWED : "))
            sql = 'SELECT * FROM ACCOUNT WHERE PIN = ?'
            values = (ATM_PIN,)
            cursor.execute(sql, values)
            data = cursor.fetchall()
            if data:
                myConnection = sqlite3.connect('data.db')
                cursor = myConnection.cursor()
                sql = "SELECT AMOUNT FROM ACCOUNT WHERE ACCOUNT_NO = ? AND PIN = ?"
                values = (account_no, ATM_PIN,)
                cursor.execute(sql, values)
                data = cursor.fetchall()
                if data:
                    print("Available Balance is - ")
                    print(data)
                break
            else:
                print("Wrong Pin ! Please enter a Valid PIN")
                count = count - 1
                print("You are left with only ", count, " Attempts")
                if count == 0:
                    print("Your Card has been Blocked , Please Visit the Branch to activate it")
                break
    else:
        print("Sorry ! Account Information NOT Found , Please Try Again ! ")


def deposit():
    count = 3
    myConnection = sqlite3.connect('data.db')
    cursor = myConnection.cursor()
    account_no = int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
    sql = "SELECT * FROM ACCOUNT WHERE ACCOUNT_NO = ?"
    values = (account_no,)
    cursor.execute(sql, values)
    data = cursor.fetchall()
    if data:
        while True:
            ATM_PIN = int(input("PLEASE ENTER THE ATM PIN - ONLY 3 ATTEMPTS ARE ALLOWED : "))
            sql = 'SELECT * FROM ACCOUNT WHERE PIN = ?'
            values = (ATM_PIN,)
            cursor.execute(sql, values)
            data = cursor.fetchall()
            if data:
                amount = int(input("PLEASE ENTER AMOUNT TO DEPOSIT : "))
                sql = 'UPDATE ACCOUNT SET AMOUNT = AMOUNT + ?'
                cursor.execute(sql, (amount,))
                cursor.execute("COMMIT")
                print("******* TRANSACTION SUCCESSFULLY COMPLETED ! *******")
                break
            else:
                print("Wrong Pin ! Please enter a Valid PIN")
                count = count - 1
                print("You are left with only ", count, " Attempts")
                if count == 0:
                    print("Your Card has been Blocked , Please Visit the Branch to activate it")
                break
    else:
        print("Sorry ! Account Information NOT Found , Please Try Again ! ")


intro = """==================================================================\n    
                \t\tIT-PYTHON INTERNATIONAL BANK\n 
        =====================================================================\n
        """


def adminmenu():
    ch = 0
    print(intro)
    if admin():
        while ch < 10:
            print(intro)
            print("==========================================")
            print("\tWELCOME, ADMINISTRATOR !")
            print("==========================================")
            print("ENTER 1 TO OPEN NEW ACCOUNT !")
            print("ENTER 2 TO DISPLAY ALL NET BANKING CUSTOMERS !")
            print("ENTER 3 TO SEARCH A NET BANKING CUSTOMER !")
            print("ENTER 4 TO DISPLAY ALL ACCOUNTS !")
            print("ENTER 5 TO SEARCH AN ACCOUNT !")
            print("ENTER 6 TO DELETE AN ACCOUNT !")
            print("ENTER 7 TO CREATE NEW ADMIN !")
            print("ENTER 8 TO SHOW ALL ADMINS !")
            print("ENTER 9 TO OPEN CUSTOMER MENU !")
            print("ENTER 10 TO EXIT !")
            ch = int(input("Your Choice- "))
            if ch == 1:
                newAccount()
            elif ch == 2:
                displayAllCustomer()
            elif ch == 3:
                searchCustomer()
            elif ch == 4:
                displayAllAccounts()
            elif ch == 5:
                searchAccount()
            elif ch == 6:
                delaccount()
            elif ch == 7:
                newadmin()
            elif ch == 8:
                alladmins()
            elif ch == 9:
                custmenu()
            elif ch == 10:
                exit("THANK YOU, VISIT AGAIN.")
            else:
                print("Invalid option. Please Try Again ")
                adminmenu()
    else:
        print("Wrong id/password. Press 1 to Try Again, Press 2 to use Customer Menu, Press 3 to Exit.")
        ch = int(input("Your Choice- "))
        if ch == 1:
            adminmenu()
        elif ch == 2:
            custmenu()
        elif ch == 3:
            exit("THANK YOU, VISIT AGAIN.")


def custmenu():
    ch = 0
    print(intro)
    while ch < 4:
        print(intro)
        print("==========================================")
        print("\tWELCOME, CUSTOMER !")
        print("==========================================")
        print("ENTER 1 FOR NEW NET BANKING USER !")
        print("ENTER 2 FOR EXISTING USER !")
        print("ENTER 3 TO GO TO MAIN MENU !")
        print("ENTER 4 TO EXIT !")
        ch = int(input("Your Choice- "))
        if ch == 1:
            newCustomer()
        elif ch == 2:
            user()
        elif ch == 3:
            netbanking()
        elif ch == 4:
            exit("THANK YOU, VISIT AGAIN.")
        else:
            print("Invalid option. Please Try Again ")
            custmenu()


def update_menu():
    print("==========================================")
    print("\tWELCOME, CUSTOMER !")
    print("==========================================")
    print("ENTER 1 TO Update Name !")
    print("ENTER 2 TO Update Address !")
    print("ENTER 3 TO Update phone !")
    print("ENTER 4 TO go back !")
    ch = int(input("Your Choice- "))
    if ch == 1:
        new = input("Enter New Name")
        update(ch, new)
    elif ch == 2:
        new = input("Enter New Address")
        update(ch, new)
    elif ch == 3:
        new = int(input("Enter New Phone"))
        update(ch, new)
    elif ch == 4:
        user()
    else:
        print("Invalid Input. Try Again")
        user()


def user():
    op = 0
    if customer():
        while op < 5:
            print(intro)
            print("==========================================")
            print("\tWELCOME, CUSTOMER !")
            print("==========================================")
            print("ENTER 1 TO CHECK YOUR DETAILS !")
            print("ENTER 2 TO UPDATE DETAILS !")
            print("ENTER 3 TO CHECK BALANCE !")
            print("ENTER 4 TO LOGOUT !")
            print("ENTER 5 FOR MAIN MENU !")
            print("ENTER 6 TO EXIT !")
            op = int(input("Your Choice- "))
            if op == 1:
                details()
            elif op == 2:
                update_menu()
            elif op == 3:
                showbalance()
            elif op == 4:
                custmenu()
            elif op == 5:
                netbanking()
            elif op == 6:
                exit("THANK YOU, VISIT AGAIN.")
            else:
                print("Invalid option. Please Try Again ")
                user()


def atm():
    op = 0
    while op < 5:
         print(intro)
         print("==========================================")
         print("\tWELCOME TO THE ATM !")
         print("==========================================")
         print("ENTER 1 TO WITHDRAW AMOUNT !")
         print("ENTER 2 TO DEPOSIT AMOUNT !")
         print("ENTER 3 TO CHECK BALANCE !")
         print("ENTER 4 TO EXIT !")
         op = int(input("Your Choice- "))
         if op == 1:
             withdraw()
         elif op == 2:
             deposit()
         elif op == 3:
             show_balance()
         elif op == 4:
             exit("THANK YOU, VISIT AGAIN.")
         else:
             print("Invalid option ")
             atm()


def netbanking():
    print(intro)
    print("==========================================")
    print("\tWELCOME TO THE NET BANKING FACILITY")
    print("==========================================")
    print("Press 1 for Admin")
    print("Press 2 for Customer")
    print("ENTER 3 TO EXIT !")
    ch = int(input("Your Choice- "))
    if ch == 1:
        adminmenu()
    elif ch == 2:
        custmenu()
    elif ch == 3:
        exit("THANK YOU, VISIT AGAIN.")
    else:
        print("Invalid option ")
        netbanking()


def defmenu():
    ch = 0
    while ch < 4:
        print(intro)
        print("ENTER 1 FOR NET BANKING !")
        print("ENTER 2 TO USE ATM !")
        print("ENTER 3 TO EXIT!")
        ch = int(input("Your Choice- "))
        if ch == 1:
            netbanking()
        elif ch == 2:
            atm()
        elif ch == 3:
            exit("THANK YOU, VISIT AGAIN.")
        else:
            print("Invalid option. Please Try Again ")
            defmenu()


defmenu()