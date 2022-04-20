import sqlite3
import main


def crud():
    try:
        option = int(input("\n"
                           "\n"
                           "*****        Customers Operation            *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Customers Create      Press 1     *****\n"
                           "*****     Customers Read        Press 2     *****\n"
                           "*****     Customers Update      Press 3     *****\n"
                           "*****     Customers Delete      Press 4     *****\n"
                           "*****     Back To User Login    Press 5     *****\n"
                           "*****     End and Exit          Press 6     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        crud()
    else:
        if option == 1:
            customer_create()
        elif option == 2:
            customer_read()
        elif option == 3:
            customer_update()
        elif option == 4:
            customer_delete()
        elif option == 5:
            main.user_login()
        elif option == 6:
            print("")
            print("")
            print("*****    Bye!    Welcome back!     *****")
            print("")
            print("")
        else:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Wrong Number   ")
            print("        Please Select Again       ")
            print("----------------------------------")
            print("")
            print("")
            crud()


if __name__ == "__main__":
    crud()


def customer_create():
    print("")
    print("")
    print("*****        CUSTOMER CREATE         *****")
    customer_name = input("Please Input Customer Name:   ")
    tup_customer_name = (customer_name,)

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM Customers;")
    db_customer_name = cursor.fetchall()
    if tup_customer_name in db_customer_name:
        print("")
        print("")
        print("*****      Customer Already EXIST       *****")
        print("*****        Please Input Again         *****")
        print("")
        print("")
        customer_create()
    else:
        customer_address = input("Please Input Customer Address:    ")
        customer_email = input("Please Input Customer Email     ")
        cursor.execute("INSERT INTO Customers (CustomerID, Name, Address, Email)\
                            values (NULL,'%s','%s','%s')" % (customer_name, customer_address, customer_email))
        cursor.execute("COMMIT;")
        print("")
        print("")
        print("----------------------------------")
        print("         Customer : %s            " % customer_name)
        print("         Create Successfully      ")
        print("----------------------------------")
        print("")
        print("")
        try:
            back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS CREATE    (3) End and Exit      "))
        except ValueError:
            print("")
            print("")
            print("----------------------------------")
            print("ValueError : Go Back To CUSTOMERS OPERATION")
            print("----------------------------------")
            print("")
            print("")
            crud()
        else:
            if back == 1:
                crud()
            elif back == 2:
                customer_create()
            elif back == 3:
                print("")
                print("")
                print("*****    Bye!    Welcome Again!     *****")
                print("")
                print("")
            else:
                print("")
                print("")
                print("----------------------------------")
                print("InputError : Go Back To CUSTOMERS OPERATION")
                print("----------------------------------")
                print("")
                print("")
                crud()
    connection.close()


def customer_read():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****                CUSTOMERS READ                 *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Search By Customer Name       Press 1     *****\n"
                           "*****     Show All Customers            Press 2     *****\n"
                           "*****     Back To CUSTOMERS OPERATION   Press 3     *****\n"
                           "*****     Back To User Login            Press 4     *****\n"
                           "*****     End and Exit                  Press 5     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        customer_read()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Search By Customer Name         *****")
            print("")
            print("")
            customer_name = input("Please Input Customer Name:   ")
            tup_customer_name = (customer_name,)
            cursor.execute("SELECT Name FROM Customers;")
            db_customer_name = cursor.fetchall()
            if tup_customer_name in db_customer_name:
                cursor.execute("SELECT * FROM Customers WHERE Name = '%s';" % customer_name)
                db_customer_info = cursor.fetchall()
                for r in db_customer_info:
                    print("")
                    print("")
                    print("CustomerID: %-10s Name: %-20s Address: %-20s Email: %-20s" % (r[0], r[1], r[2], r[3]))
                    print("")
                    print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS READ\
                        (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_read()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Search UN-Successfully     *****")
                print("*****        Customer %s Not Exist      *****" % customer_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS READ\
                        (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_read()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
        elif option == 2:
            print("")
            print("")
            print("*****        Show All Customers         *****")
            print("")
            print("")
            cursor.execute("SELECT * FROM Customers")
            db_customer_info = cursor.fetchall()
            for r in db_customer_info:
                print("CustomerID: %-10s Name: %-20s Address: %-20s Email: %-20s" % (r[0], r[1], r[2], r[3]))
            print("")
            try:
                back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS READ\
                    (3) End and Exit       "))
            except ValueError:
                print("")
                print("")
                print("----------------------------------")
                print("ValueError : Go Back To CUSTOMERS OPERATION")
                print("----------------------------------")
                print("")
                print("")
                crud()
            else:
                if back == 1:
                    crud()
                elif back == 2:
                    customer_read()
                elif back == 3:
                    print("")
                    print("")
                    print("*****    Bye!    Welcome Again!     *****")
                    print("")
                    print("")
                else:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
        elif option == 3:
            crud()
        elif option == 4:
            main.user_login()
        elif option == 5:
            print("")
            print("")
            print("*****    Bye!    Welcome Again!     *****")
            print("")
            print("")
        else:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Wrong Number   ")
            print("        Please Select Again       ")
            print("----------------------------------")
            print("")
            print("")
            customer_read()
    connection.close()


def customer_update():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              CUSTOMERS UPDATE                 *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Modify Customer Address       Press 1     *****\n"
                           "*****     Back To CUSTOMERS OPERATION   Press 2     *****\n"
                           "*****     Back To User Login            Press 3     *****\n"
                           "*****     End and Exit                  Press 4     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        customer_update()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Modify Customer Address        *****")
            print("")
            print("")
            customer_name = input("Please Input Customer Name:   ")
            tup_customer_name = (customer_name,)
            cursor.execute("SELECT Name FROM Customers;")
            db_customer_name = cursor.fetchall()
            if tup_customer_name in db_customer_name:
                user_address = input("Please Input User New Address:   ")
                cursor.execute("UPDATE Customers SET Address ='%s' WHERE Name = '%s'" % (user_address, customer_name))
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Customer :  %s           " % customer_name)
                print("         Modify Successfully      ")
                print("         New Address:   %s        " % user_address)
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS UPDATE\
                            (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_update()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Customer %s Not Exist          *****" % customer_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS UPDATE\
                            (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_update()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
        elif option == 2:
            crud()
        elif option == 3:
            main.user_login()
        elif option == 4:
            print("")
            print("")
            print("*****    Bye!    Welcome Again!     *****")
            print("")
            print("")
        else:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Wrong Number   ")
            print("        Please Select Again       ")
            print("----------------------------------")
            print("")
            print("")
            customer_update()
    connection.close()


def customer_delete():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              CUSTOMERS DELETE                 *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Delete Customer               Press 1     *****\n"
                           "*****     Back To CUSTOMERS OPERATION   Press 2     *****\n"
                           "*****     Back To User Login            Press 3     *****\n"
                           "*****     End and Exit                  Press 4     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        customer_delete()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Delete Customer         *****")
            print("")
            print("")
            customer_name = input("Please Input Customer Name:   ")
            tup_customer_name = (customer_name,)
            cursor.execute("SELECT Name FROM Customers;")
            db_customer_name = cursor.fetchall()
            if tup_customer_name in db_customer_name:
                cursor.execute("DELETE FROM Customers WHERE Name = '%s'" % customer_name)
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Customer :  %s           " % customer_name)
                print("         Delete Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS DELETE\
                                (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_delete()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Customer %s Not Exist          *****" % customer_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) CUSTOMERS OPERATION    (2) CUSTOMERS DELETE\
                                (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To CUSTOMERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        customer_delete()
                    elif back == 3:
                        print("")
                        print("")
                        print("*****    Bye!    Welcome Again!     *****")
                        print("")
                        print("")
                    else:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To CUSTOMERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
        elif option == 2:
            crud()
        elif option == 3:
            main.user_login()
        elif option == 4:
            print("")
            print("")
            print("*****    Bye!    Welcome Again!     *****")
            print("")
            print("")
        else:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Wrong Number   ")
            print("        Please Select Again       ")
            print("----------------------------------")
            print("")
            print("")
            customer_delete()
    connection.close()
