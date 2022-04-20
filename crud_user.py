import sqlite3
import main


def crud():
    try:
        option = int(input("\n"
                           "\n"
                           "*****          USERS OPERATION              *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Users Create          Press 1     *****\n"
                           "*****     Users Read            Press 2     *****\n"
                           "*****     Users Update          Press 3     *****\n"
                           "*****     Users Delete          Press 4     *****\n"
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
            user_create()
        elif option == 2:
            user_read()
        elif option == 3:
            user_update()
        elif option == 4:
            user_delete()
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
            print("        Please Select Again       ")
            print("----------------------------------")
            print("")
            print("")
            crud()


if __name__ == "__main__":
    crud()


def user_create():
    print("")
    print("")
    print("*****        USER CREATE         *****")
    user_name = input("Please Input User Name:   ")
    tup_user_name = (user_name,)

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT UserName FROM Users;")
    db_user_name = cursor.fetchall()
    if tup_user_name in db_user_name:       # User already exist
        print("")
        print("")
        print("*****        User Already EXIST         *****")
        print("*****        Please Input Again         *****")
        print("")
        print("")
        user_create()
    else:          # If user not exist, then create
        user_password = input("Please Input User Password:   ")

        try:
            user_type = int(input("Please Choose User Type:     (1)  Admin    (2) Staff       "))

        except ValueError:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Not A Number   ")
            print("         Please Input Again       ")
            print("----------------------------------")
            print("")
            print("")
            user_create()

        else:
            if user_type == 1:
                cursor.execute("INSERT INTO Users (UserID, UserName, UserPassword, UserType)\
                    values (NULL,'%s','%s','Admin')" % (user_name, user_password))
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Admin User : %s          " % user_name)
                print("         Create Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USER CREATE    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_create()
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
                        print("InputError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()

            elif user_type == 2:
                cursor.execute("INSERT INTO Users (UserID, UserName, UserPassword, UserType)\
                    values (NULL,'%s','%s','Stuff')" % (user_name, user_password))
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Stuff User : %s          " % user_name)
                print("         Create Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USER CREATE    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_create()
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
                        print("InputError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()

            else:
                print("")
                print("")
                print("----------------------------------")
                print("     Input Error : Wrong Number   ")
                print("         Please Input Again       ")
                print("----------------------------------")
                print("")
                print("")
                user_create()
    connection.close()


def user_read():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****                 USERS READ                *****\n"
                           "\n"
                           "*****         Please Select Your Action         *****\n"
                           "\n"
                           "*****     Search By User Name       Press 1     *****\n"
                           "*****     Show All Users            Press 2     *****\n"
                           "*****     Back To USERS OPERATION   Press 3     *****\n"
                           "*****     Back To User Login        Press 4     *****\n"
                           "*****     End and Exit              Press 5     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        user_read()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Search By User Name         *****")
            print("")
            print("")
            user_name = input("Please Input User Name:   ")
            tup_user_name = (user_name,)
            cursor.execute("SELECT UserName FROM Users;")
            db_user_name = cursor.fetchall()
            if tup_user_name in db_user_name:
                cursor.execute("SELECT * FROM Users WHERE UserName = '%s';" % user_name)
                db_user_info = cursor.fetchall()
                for r in db_user_info:
                    print("")
                    print("")
                    print("UserID: %-10s UserName: %-10s Password: %-10s UserType: %-10s" % (r[0], r[1], r[2], r[3]))
                    print("")
                    print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USERS READ    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_read()
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
                        print("ValueError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Search UN-Successfully     *****")
                print("*****        User %s Not Exist          *****" % user_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USERS READ    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_read()
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
                        print("ValueError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()

        elif option == 2:
            print("")
            print("")
            print("*****        Show All Users         *****")
            print("")
            print("")
            cursor.execute("SELECT * FROM Users")
            db_user_info = cursor.fetchall()
            for r in db_user_info:
                print("UserID: %-10s UserName: %-30s Password: %-30s UserType: %-10s" % (r[0], r[1], r[2], r[3]))
            print("")

            try:
                back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USERS READ    (3) End and Exit       "))
            except ValueError:
                print("")
                print("")
                print("----------------------------------")
                print("ValueError : Go Back To USERS OPERATION")
                print("----------------------------------")
                print("")
                print("")
                crud()
            else:
                if back == 1:
                    crud()
                elif back == 2:
                    user_read()
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
                    print("ValueError : Go Back To USERS OPERATION")
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
            user_read()
    connection.close()


def user_update():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****               USERS UPDATE                *****\n"
                           "\n"
                           "*****         Please Select Your Action         *****\n"
                           "\n"
                           "*****     Modify Password           Press 1     *****\n"
                           "*****     Back To USERS OPERATION   Press 2     *****\n"
                           "*****     Back To User Login        Press 3     *****\n"
                           "*****     End and Exit              Press 4     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        user_update()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Modify Password         *****")
            print("")
            print("")
            user_name = input("Please Input User Name:   ")
            tup_user_name = (user_name,)
            cursor.execute("SELECT UserName FROM Users;")
            db_user_name = cursor.fetchall()
            if tup_user_name in db_user_name:
                user_password = input("Please Input User New Password:   ")
                cursor.execute("UPDATE Users SET UserPassword ='%s' WHERE Username = '%s'" % (user_password, user_name))
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         User :  %s               " % user_name)
                print("         Modify Successfully      ")
                print("         New Password:   %s       " % user_password)
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USER UPDATE    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_update()
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
                        print("InputError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        User %s Not Exist          *****" % user_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USERS UPDATE    (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_update()
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
                        print("ValueError : Go Back To USERS OPERATION")
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
            user_update()
    connection.close()


def user_delete():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****               USERS DELETE                *****\n"
                           "\n"
                           "*****         Please Select Your Action         *****\n"
                           "\n"
                           "*****     Delete User               Press 1     *****\n"
                           "*****     Back To USERS OPERATION   Press 2     *****\n"
                           "*****     Back To User Login        Press 3     *****\n"
                           "*****     End and Exit              Press 4     *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        user_delete()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Delete User         *****")
            print("")
            print("")
            user_name = input("Please Input User Name:   ")
            tup_user_name = (user_name,)
            cursor.execute("SELECT UserName FROM Users;")
            db_user_name = cursor.fetchall()
            if tup_user_name in db_user_name:
                cursor.execute("DELETE FROM Users WHERE Username = '%s'" % user_name)
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         User :  %s               " % user_name)
                print("         Delete Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USER DELETE    (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_delete()
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
                        print("InputError : Go Back To USERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        User %s Not Exist          *****" % user_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) USERS OPERATION    (2) USERS DELETE    (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To USERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        user_delete()
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
                        print("ValueError : Go Back To USERS OPERATION")
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
            user_delete()
    connection.close()
