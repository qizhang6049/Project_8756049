import sqlite3
import main
import time


def crud():

    try:
        option = int(input("\n"
                           "\n"
                           "*****          Orders Operation             *****\n"
                           "\n"
                           "*****     Please Select Your Action         *****\n"
                           "\n"
                           "*****     Orders Create         Press 1     *****\n"
                           "*****     Orders Read           Press 2     *****\n"
                           "*****     Orders Update         Press 3     *****\n"
                           "*****     Orders Delete         Press 4     *****\n"
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
            order_create()
        elif option == 2:
            order_read()
        elif option == 3:
            order_update()
        elif option == 4:
            order_delete()
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


def order_create():
    print("")
    print("")
    print("*****        ORDERS  CREATE         *****")
    product_name = input("Please Input Product Name:   ")
    tup_product_name = (product_name,)

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT ProductName FROM Products;")
    db_product_name = cursor.fetchall()
    if tup_product_name in db_product_name:
        print("")
        print("")
        print("*****        ORDERS  CREATE         *****")
        customer_name = input("Please Input Customer Name:   ")
        tup_customer_name = (customer_name,)

        cursor.execute("SELECT Name FROM Customers;")
        db_customer_name = cursor.fetchall()
        if tup_customer_name in db_customer_name:
            try:
                order_price = float(input("Please Input Order Price        "))
            except ValueError:
                print("")
                print("")
                print("----------------------------------")
                print("     Input Error : Not A Number   ")
                print("         Please Input Again       ")
                print("----------------------------------")
                print("")
                print("")
                order_create()
            else:
                if order_price < 0:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("   Input Error : Price Can not < 0")
                    print("         Please Input Again       ")
                    print("----------------------------------")
                    print("")
                    print("")
                    order_create()
                else:
                    order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    cursor.execute("INSERT INTO Orders (OrderID, Products, Customer, TotalPrice, Date)\
                        values (NULL,'%s','%s','%f','%s')" % (product_name, customer_name, order_price, order_time))
                    cursor.execute("COMMIT;")
                    print("")
                    print("")
                    print("------------------------------------------")
                    print("Product: %s  Customer: %s    Price: %f    " % (product_name, customer_name, order_price))
                    print("       Date: %s                           " % order_time)
                    print("       Order Create Successfully          ")
                    print("------------------------------------------")
                    print("")
                    print("")
                    try:
                        back = int(input("Go Back To ?  (1) ORDER OPERATION    (2) ORDER CREATE\
                            (3) End and Exit      "))
                    except ValueError:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To ORDER OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
                    else:
                        if back == 1:
                            crud()
                        elif back == 2:
                            order_create()
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
                            print("InputError : Go Back To ORDER OPERATION")
                            print("----------------------------------")
                            print("")
                            print("")
                            crud()
        else:
            print("")
            print("")
            print("*****        Customer Not EXIST       *****")
            print("*****        Please Input Again      *****")
            print("")
            print("")
            order_create()
    else:
        print("")
        print("")
        print("*****        Product Not EXIST       *****")
        print("*****        Please Input Again      *****")
        print("")
        print("")
        order_create()
    connection.close()


def order_read():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****                ORDERS READ                    *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Search By Product Name        Press 1     *****\n"
                           "*****     Show All Orders               Press 2     *****\n"
                           "*****     Back To ORDERS OPERATION      Press 3     *****\n"
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
        order_read()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Search By Product Name         *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT Products FROM Orders;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                cursor.execute("SELECT * FROM Orders WHERE Products = '%s'" % product_name)
                db_order_info = cursor.fetchall()
                for r in db_order_info:
                    print("OrderID: %-10s Product: %-15s Customer: %-15s Price: %-15f Date: %-15s" % (r[0], r[1], r[2], r[3], r[4]))
                    print("")
                try:
                    back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDERS READ\
                            (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To ORDERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        order_read()
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
                        print("ValueError : Go Back To ORDERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
            else:
                print("")
                print("")
                print("*****        Search UN-Successfully     *****")
                print("*****          Order %s Not Exist       *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDERS READ\
                            (3) End and Exit       "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To ORDERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        order_read()
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
                        print("ValueError : Go Back To ORDERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
        elif option == 2:
            print("")
            print("")
            print("*****        Show All Orders         *****")
            print("")
            print("")
            cursor.execute("SELECT * FROM Orders;")
            db_order_info = cursor.fetchall()
            for r in db_order_info:
                print("OrderID: %-10s Product: %-15s Customer: %-15s Price: %-15f Date: %-15s" % (r[0], r[1], r[2], r[3], r[4]))
            print("")
            try:
                back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDERS READ\
                        (3) End and Exit       "))
            except ValueError:
                print("")
                print("")
                print("----------------------------------")
                print("ValueError : Go Back To ORDERS OPERATION")
                print("----------------------------------")
                print("")
                print("")
                crud()
            else:
                if back == 1:
                    crud()
                elif back == 2:
                    order_read()
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
                    print("ValueError : Go Back To ORDERS OPERATION")
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
            order_read()
    connection.close()


def order_update():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              ORDERS UPDATE                    *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Modify Order Total Price      Press 1     *****\n"
                           "*****     Back To ORDERS OPERATION      Press 2     *****\n"
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
        order_update()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Modify Order Total Price        *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT Products FROM Orders;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                customer_name = input("Please Input Customer Name:   ")
                tup_customer_name = (customer_name,)

                cursor.execute("SELECT Customer FROM Orders WHERE Products = '%s'" % product_name)
                db_customer_name = cursor.fetchall()
                if tup_customer_name in db_customer_name:
                    try:
                        order_price = float(input("Please Input Order New Total Price        "))
                    except ValueError:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("     Input Error : Not A Number   ")
                        print("         Please Input Again       ")
                        print("----------------------------------")
                        print("")
                        print("")
                        order_update()
                    else:
                        if order_price < 0:
                            print("")
                            print("")
                            print("----------------------------------")
                            print("   Input Error : Price Can not < 0")
                            print("         Please Input Again       ")
                            print("----------------------------------")
                            print("")
                            print("")
                            order_update()
                        else:
                            cursor.execute("UPDATE Orders SET TotalPrice ='%f' WHERE \
                                    Products = '%s'" % (order_price, product_name))
                            cursor.execute("COMMIT;")
                            print("")
                            print("")
                            print("----------------------------------")
                            print("         Order : %s      %s       " % (product_name, customer_name))
                            print("         Modify Successfully      ")
                            print("         New Total Price: %f      " % order_price)
                            print("----------------------------------")
                            print("")
                            print("")
                            try:
                                back = int(input("Go Back To ?  (1) ORDER OPERATION    (2) ORDER UPDATE\
                                        (3) End and Exit      "))
                            except ValueError:
                                print("")
                                print("")
                                print("----------------------------------")
                                print("ValueError : Go Back To ORDER OPERATION")
                                print("----------------------------------")
                                print("")
                                print("")
                                crud()
                            else:
                                if back == 1:
                                    crud()
                                elif back == 2:
                                    order_update()
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
                                    print("InputError : Go Back To ORDER OPERATION")
                                    print("----------------------------------")
                                    print("")
                                    print("")
                                    crud()
                else:
                    print("")
                    print("")
                    print("*****        Order %s Not Exist          *****" % product_name)
                    print("")
                    print("")
                    try:
                        back = int(input("Go Back To ?  (1) ORDER OPERATION    (2) ORDER UPDATE\
                                                (3) End and Exit      "))
                    except ValueError:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To ORDER OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
                    else:
                        if back == 1:
                            crud()
                        elif back == 2:
                            order_update()
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
                            print("InputError : Go Back To ORDER OPERATION")
                            print("----------------------------------")
                            print("")
                            print("")
                            crud()
            else:
                print("")
                print("")
                print("*****        Order %s Not Exist          *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) ORDER OPERATION    (2) ORDER UPDATE\
                            (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To ORDER OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        order_update()
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
                        print("InputError : Go Back To ORDER OPERATION")
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
            order_update()
    connection.close()


def order_delete():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    try:
        option = int(input("\n"
                           "\n"
                           "*****              ORDERS DELETE                    *****\n"
                           "\n"
                           "*****          Please Select Your Action            *****\n"
                           "\n"
                           "*****     Delete Order                  Press 1     *****\n"
                           "*****     Back To ORDERS OPERATION      Press 2     *****\n"
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
        order_delete()
    else:
        if option == 1:
            print("")
            print("")
            print("*****        Delete Order         *****")
            print("")
            print("")
            product_name = input("Please Input Product Name:   ")
            tup_product_name = (product_name,)
            cursor.execute("SELECT Products FROM Orders;")
            db_product_name = cursor.fetchall()
            if tup_product_name in db_product_name:
                customer_name = input("Please Input Customer Name:   ")
                tup_customer_name = (customer_name,)

                cursor.execute("SELECT Customer FROM Orders WHERE Products = '%s'" % product_name)
                db_customer_name = cursor.fetchall()
                if tup_customer_name in db_customer_name:
                    cursor.execute("DELETE FROM Orders WHERE Products = '%s' and \
                                   Customer = '%s'" % (product_name, customer_name))
                    cursor.execute("COMMIT;")
                    print("")
                    print("")
                    print("----------------------------------")
                    print("         Order :  %s %s          " % (product_name, customer_name))
                    print("         Delete Successfully      ")
                    print("----------------------------------")
                    print("")
                    print("")
                    try:
                        back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDER DELETE\
                                                (3) End and Exit      "))
                    except ValueError:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To ORDERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
                    else:
                        if back == 1:
                            crud()
                        elif back == 2:
                            order_delete()
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
                            print("InputError : Go Back To ORDERS OPERATION")
                            print("----------------------------------")
                            print("")
                            print("")
                            crud()
                else:
                    print("")
                    print("")
                    print("*****        Order %s    %s Not Exist          *****" % (product_name, customer_name))
                    print("")
                    print("")
                    try:
                        back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDER DELETE\
                                                (3) End and Exit      "))
                    except ValueError:
                        print("")
                        print("")
                        print("----------------------------------")
                        print("ValueError : Go Back To ORDERS OPERATION")
                        print("----------------------------------")
                        print("")
                        print("")
                        crud()
                    else:
                        if back == 1:
                            crud()
                        elif back == 2:
                            order_delete()
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
                            print("InputError : Go Back To ORDERS OPERATION")
                            print("----------------------------------")
                            print("")
                            print("")
                            crud()
            else:
                print("")
                print("")
                print("*****        Order %s Not Exist          *****" % product_name)
                print("")
                print("")
                try:
                    back = int(input("Go Back To ?  (1) ORDERS OPERATION    (2) ORDER DELETE\
                            (3) End and Exit      "))
                except ValueError:
                    print("")
                    print("")
                    print("----------------------------------")
                    print("ValueError : Go Back To ORDERS OPERATION")
                    print("----------------------------------")
                    print("")
                    print("")
                    crud()
                else:
                    if back == 1:
                        crud()
                    elif back == 2:
                        order_delete()
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
                        print("InputError : Go Back To ORDERS OPERATION")
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
            order_delete()
    connection.close()
