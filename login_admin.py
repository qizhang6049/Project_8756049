import sqlite3
import main
import crud_user
import crud_product
import crud_customer
import crud_order


def login():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT UserName FROM Users WHERE UserType = 'Admin'")
    db_username = cursor.fetchall()
    print("")
    print("")
    print("*****     Admin User Login       *****")
    input_username = input("Please Input Admin Username    :   ")
    tup_username = (input_username,)

    if tup_username in db_username:      # verify username  in database
        input_password = input("Please Input Admin Password    :   ")
        tup_password = (input_password,)

        cursor.execute("SELECT UserPassword FROM Users WHERE UserName = '%s'" % input_username)
        db_password = cursor.fetchall()

        if tup_password in db_password:     # verify password in database
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
        print("*****    Admin User Not Exist       *****")
        print("*****    Or User Is Not Admin       *****")
        print("*****    Back To Admin Login        *****")
        print("")
        print("")
        login()

    connection.close()


if __name__ == "__main__":
    login()


def login_succeed():
    try:
        option = int(input("\n"
                           "\n"
                           "*****     Admin User Login Successfully     *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Users Operation       Press 1     *****\n"
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
            crud_user.crud()
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
