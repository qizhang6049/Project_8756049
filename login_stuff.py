import sqlite3
import main
import crud_product
import crud_customer
import crud_order
import extract_report


def login():
    print("")
    print("")
    print("*****     Stuff User Login       *****")
    input_username = input("Please Input Stuff Username    :   ")
    tup_username = (input_username,)

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT UserName FROM Users WHERE UserType = 'Stuff'")
    db_username = cursor.fetchall()

    if tup_username in db_username:      # verify username  in database
        input_password = input("Please Input Stuff Password    :   ")
        tup_password = (input_password,)

        cursor.execute("SELECT UserPassword FROM Users WHERE UserName = '%s'" % input_username)
        db_password = cursor.fetchall()

        if tup_password in db_password:  # verify password in database

            login_succeed()

        else:
            print("")
            print("")
            print("----------------------------------")
            print("           Wrong Password         ")
            print("         Please Login Again       ")
            print("----------------------------------")
            print("")
            print("")
            login()

    else:
        print("")
        print("")
        print("*****    Stuff User Not Exist       *****")
        print("*****    Or User Is Not Stuff       *****")
        print("*****    Back To User Login         *****")
        print("")
        print("")
        main.user_login()

    connection.close()


if __name__ == "__main__":
    login()


def login_succeed():
    try:
        option = int(input("\n"
                           "\n"
                           "*****     Stuff User Login Successfully     *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Reports Operation     Press 1     *****\n"
                           "*****     Products Operation    Press 2     *****\n"
                           "*****     Customers Operation   Press 3     *****\n"
                           "*****     Orders Operation      Press 4     *****\n"
                           "*****     Back To User Login    Press 5     *****\n"
                           "*****     End and Exit          Press 6     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("         Please Select Again      ")
        print("----------------------------------")
        print("")
        print("")
        login_succeed()
    else:
        if option == 1:
            extract_report.extract()
        elif option == 2:
            crud_product.crud()
        elif option == 3:
            crud_customer.crud()
        elif option == 4:
            crud_order.crud()
        elif option == 5:
            main.user_login()
        elif option == 6:
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
            print("         Please Select Again      ")
            print("----------------------------------")
            print("")
            print("")
            login_succeed()
