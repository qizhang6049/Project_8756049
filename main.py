import login_admin
import login_stuff


def user_login():

    print("")
    print("")
    print("    ***************************")
    print("              Welcome          ")
    print("            User Login         ")
    print("    ***************************")
    print("")
    print("")

    try:
        option = int(input("    Admin User Login    Press 1    \n"
                           "    Stuff User Login    Press 2    \n"
                           "    End and Exit        Press 3    \n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("         Please Input Again       ")
        print("----------------------------------")
        print("")
        print("")
        user_login()
    else:
        if option == 1:
            login_admin.login()
        elif option == 2:
            login_stuff.login()
        elif option == 3:
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
            print("         Please Input Again       ")
            print("----------------------------------")
            print("")
            print("")
            user_login()


if __name__ == "__main__":
    user_login()
