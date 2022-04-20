import sqlite3
import main


def crud():
    try:
        option = int(input("\n"
                           "\n"
                           "*****         Products Operation            *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Products Create       Press 1     *****\n"
                           "*****     Products Read         Press 2     *****\n"
                           "*****     Products Update       Press 3     *****\n"
                           "*****     Products Delete       Press 4     *****\n"
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
            product_create()
        elif option == 2:
            product_read()
        elif option == 3:
            product_update()
        elif option == 4:
            product_delete()
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


def product_create():
    print("")
    print("")
    print("*****        PRODUCTS CREATE         *****")
    product_name = input("Please Input Product Name:   ")
    tup_product_name = (product_name,)

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT ProductName FROM Products;")
    db_product_name = cursor.fetchall()
    if tup_product_name in db_product_name:
        print("")
        print("")
        print("*****       Product Already EXIST       *****")
        print("*****        Please Input Again         *****")
        print("")
        print("")
        product_create()
    else:
        try:
            product_price = float(input("Please Input Product Unit Price        "))
        except ValueError:
            print("")
            print("")
            print("----------------------------------")
            print("     Input Error : Not A Number   ")
            print("         Please Input Again       ")
            print("----------------------------------")
            print("")
            print("")
            product_create()
        else:
            if product_price < 0:
                print("")
                print("")
                print("----------------------------------")
                print("   Input Error : Price Can not < 0")
                print("         Please Input Again       ")
                print("----------------------------------")
                print("")
                print("")
                product_create()
            else:
                cursor.execute("INSERT INTO Products (ProductID, ProductName, UnitPrice)\
                                                values (NULL,'%s','%f')" % (product_name, product_price))
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Product : %s            " % product_name)
                print("         Create Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCT OPERATION    (2) PRODUCT CREATE\
                        (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCT OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_create()
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
                        print("InputError : Go Back To PRODUCT OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
    connection.close()


def product_read():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****                PRODUCTS READ                 *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Search By Product Name        Press 1     *****\n"
                           "*****     Show All Products             Press 2     *****\n"
                           "*****     Back To PRODUCTS OPERATION    Press 3     *****\n"
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
        product_read()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Search By Product Name         *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT ProductName FROM Products;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                cursor.execute("SELECT * FROM Products WHERE ProductName = '%s';" % product_name)
                db_product_info = cursor.fetchall()
                for r in db_product_info:
                    print("")
                    print("")
                    print("ProductID: %-10s Name: %-20s UnitPrice: %-20s" % (r[0], r[1], r[2]))
                    print("")
                    print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCTS OPERATION    (2) PRODUCTS READ\
                        (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCTS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_read()
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
                        print("ValueError : Go Back To PRODUCTS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Search UN-Successfully     *****")
                print("*****        Product %s Not Exist       *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCTS OPERATION    (2) PRODUCTS READ\
                        (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCTS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_read()
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
                        print("ValueError : Go Back To PRODUCTS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
        elif option == 2:
            print("")
            print("")
            print("*****        Show All Products         *****")
            print("")
            print("")
            cursor.execute("SELECT * FROM Products;")
            db_product_info = cursor.fetchall()
            for r in db_product_info:
                print("ProductID: %-10s Name: %-20s UnitPrice: %-20s" % (r[0], r[1], r[2]))
            print("")
            try:
                back = int(input("Go Back To ?  (1) PRODUCTS OPERATION    (2) PRODUCTS READ\
                    (3) End and Exit       "))
            except ValueError:
                print("")
                print("")
                print("----------------------------------")
                print("ValueError : Go Back To PRODUCTS OPERATION")
                print("----------------------------------")
                print("")
                print("")
                crud()
            else:
                if back == 1:
                    crud()
                elif back == 2:
                    product_read()
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
                    print("ValueError : Go Back To PRODUCTS OPERATION")
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
            product_read()
    connection.close()


def product_update():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              PRODUCTS UPDATE                  *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Modify Product Unit Price     Press 1     *****\n"
                           "*****     Back To PRODUCTS OPERATION    Press 2     *****\n"
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
        product_update()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Modify Product Unit Price        *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT ProductName FROM Products;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                try:
                    product_price = float(input("Please Input Product New Unit Price        "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("     Input Error : Not A Number   ")
                    print("         Please Input Again       ")
                    print("----------------------------------")
                    print("")
                    print("")
                    product_update()
                else:
                    if product_price < 0:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("   Input Error : Price Can not < 0")
                        print("         Please Input Again       ")
                        print("----------------------------------")
                        print("")
                        print("")
                        product_update()
                    else:
                        cursor.execute("UPDATE Products SET UnitPrice ='%f' WHERE \
                            ProductName = '%s'" % (product_price, product_name))
                        cursor.execute("COMMIT;")
                        print("")
                        print("")
                        print("----------------------------------")
                        print("         Product : %s             " % product_name)
                        print("         Modify Successfully      ")
                        print("         New Unit Price: %f       " % product_price)
                        print("----------------------------------")
                        print("")
                        print("")
                        try:
                            back = int(input("Go Back To ?  (1) PRODUCT OPERATION    (2) PRODUCT UPDATE\
                                (3) End and Exit      "))
                        except ValueError:
                            print("")
                            print("")
                            print("----------------------------------")
                            print("ValueError : Go Back To PRODUCT OPERATION")
                            print("----------------------------------")
                            print("")
                            print("")
                            crud()
                        else:
                            if back == 1:
                                crud()
                            elif back == 2:
                                product_update()
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
                                print("InputError : Go Back To PRODUCT OPERATION")
                                print("----------------------------------")
                                print("")
                                print("")
                                crud()
            else:
                print("")
                print("")
                print("*****        Product %s Not Exist          *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCT OPERATION    (2) PRODUCT UPDATE\
                        (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCT OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_update()
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
                        print("InputError : Go Back To PRODUCT OPERATION")
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
            product_update()
    connection.close()


def product_delete():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              PRODUCTS DELETE                  *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Delete Product                Press 1     *****\n"
                           "*****     Back To PRODUCTS OPERATION    Press 2     *****\n"
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
        product_delete()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Delete Product         *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT ProductName FROM Products;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                cursor.execute("DELETE FROM Products WHERE ProductName = '%s'" % product_name)
                cursor.execute("COMMIT;")
                print("")
                print("")
                print("----------------------------------")
                print("         Product :  %s           " % product_name)
                print("         Delete Successfully      ")
                print("----------------------------------")
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCT OPERATION    (2) PRODUCT DELETE\
                        (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCT OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_delete()
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
                        print("InputError : Go Back To PRODUCT OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Product %s Not Exist          *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) PRODUCT OPERATION    (2) PRODUCT DELETE\
                        (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To PRODUCT OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        product_delete()
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
                        print("InputError : Go Back To PRODUCT OPERATION")
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
            product_delete()
    connection.close()
