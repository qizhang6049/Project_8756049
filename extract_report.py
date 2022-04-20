import sqlite3
import matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

import main


def extract():
    try:
        option = int(input("\n"
                           "\n"
                           "*****          REPORTS OPERATION                *****\n"
                           "\n"
                           "*****      Please Select Your Action            *****\n"
                           "\n"
                           "*****     User Table            Press 1         *****\n"
                           "*****     User Graph            Press 2         *****\n"
                           "*****     Product Table         Press 3         *****\n"
                           "*****     Product Graph         Press 4         *****\n"
                           "*****     Customer Table        Press 5         *****\n"
                           "*****     Customer Graph        Press 6         *****\n"
                           "*****     Order Table           Press 7         *****\n"
                           "*****     Order Graph           Press 8         *****\n"
                           "*****     Back To User Login    Press 9         *****\n"
                           "*****     End and Exit          Press 0         *****\n"))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("     Input Error : Not A Number   ")
        print("        Please Select Again       ")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if option == 1:
            user_table()
        elif option == 2:
            user_graph()
        elif option == 3:
            product_table()
        elif option == 4:
            product_graph()
        elif option == 5:
            customer_table()
        elif option == 6:
            customer_graph()
        elif option == 7:
            order_table()
        elif option == 8:
            order_graph()
        elif option == 9:
            main.user_login()
        elif option == 0:
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
            extract()


if __name__ == "__main__":
    extract()


def user_table():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    db_user_info = cursor.fetchall()

    users_table = pd.DataFrame(db_user_info, columns=['ID', 'UserName', 'Password', 'UserType'])
    del users_table['ID']
    del users_table['UserName']
    del users_table['Password']

    users_table = users_table['UserType'].value_counts().rename_axis('Type').reset_index(name='Count')
    print('*****     User Type Count Table   *****')
    print('')
    print(users_table)
    print('')

    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def user_graph():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    db_user_info = cursor.fetchall()

    users_table = pd.DataFrame(db_user_info, columns=['ID', 'UserName', 'Password', 'UserType'])
    del users_table['ID']
    del users_table['UserName']
    del users_table['Password']

    users_table = users_table['UserType'].value_counts().rename_axis('Type').reset_index(name='Count')
    users_table.plot(x='Type', y='Count', kind='bar', title='User Type Count')
    matplotlib.pyplot.show()
    matplotlib.pyplot.close(fig=None)

    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def product_table():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    db_product_info = cursor.fetchall()

    products_table = pd.DataFrame(db_product_info, columns=['ID', 'ProductName', 'UnitPrice'])

    products_table['Price-Range'] = products_table['UnitPrice'].apply(lambda x: 'Less than 30' if x < 30 else (
        'Between 30 - 80' if (30 <= x <= 80) else 'More than 80'))

    del products_table['ID']
    del products_table['ProductName']
    del products_table['UnitPrice']

    products_table = products_table['Price-Range'].value_counts().rename_axis('Price-Range').reset_index(name='Count')
    print('*****     Products UnitPrice Range Table   *****')
    print('')
    print(products_table)
    print('')
    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def product_graph():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    db_product_info = cursor.fetchall()

    products_table = pd.DataFrame(db_product_info, columns=['ID', 'ProductName', 'UnitPrice'])

    products_table['Price-Range'] = products_table['UnitPrice'].apply(lambda x: 'Less than 30' if x < 30 else (
        'Between 30 - 80' if (30 <= x <= 80) else 'More than 80'))

    del products_table['ID']
    del products_table['ProductName']
    del products_table['UnitPrice']

    products_table = products_table['Price-Range'].value_counts().rename_axis('Price-Range').reset_index(name='Count')

    plt.title('Products Price-Range Pct')
    plt.pie(x=products_table['Count'], labels=products_table['Price-Range'], autopct='%3.3f%%')
    matplotlib.pyplot.show()
    matplotlib.pyplot.close(fig=None)
    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def customer_table():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customers")
    db_customer_info = cursor.fetchall()

    customers_table = pd.DataFrame(db_customer_info, columns=['ID', 'CustomerName', 'Address', 'Email'])

    del customers_table['ID']
    del customers_table['CustomerName']
    del customers_table['Email']

    customers_table = customers_table['Address'].value_counts().rename_axis('City').reset_index(name='Count')
    print('*****     Customer Address Count Table   *****')
    print('')
    print(customers_table)
    print('')
    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def customer_graph():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customers")
    db_customer_info = cursor.fetchall()

    customers_table = pd.DataFrame(db_customer_info, columns=['ID', 'CustomerName', 'Address', 'Email'])

    del customers_table['ID']
    del customers_table['CustomerName']
    del customers_table['Email']

    customers_table = customers_table['Address'].value_counts().rename_axis('City').reset_index(name='Count')
    customers_table.plot(x='City', y='Count', kind='bar', title='Customers Address Count')
    matplotlib.pyplot.show()
    matplotlib.pyplot.close(fig=None)

    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def order_table():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders")
    db_order_info = cursor.fetchall()

    orders_table = pd.DataFrame(db_order_info, columns=['ID', 'Product', 'Customer', 'Price', 'Date'])

    del orders_table['ID']
    del orders_table['Date']
    order_count = pd.crosstab(orders_table.Customer, orders_table.Product)
    print('*****     Orders Count By Customers and Products   *****')
    print('')
    print(order_count)
    print('')

    order_amount = pd.crosstab(orders_table.Customer, orders_table.Product, orders_table.Price, aggfunc='sum').fillna(
        value=0)
    print('*****     Orders Amount By Customers and Products   *****')
    print('')
    print(order_amount)
    print('')

    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()


def order_graph():
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders")
    db_order_info = cursor.fetchall()

    orders_table = pd.DataFrame(db_order_info, columns=['ID', 'Product', 'Customer', 'Price', 'Date'])

    del orders_table['ID']
    del orders_table['Date']
    order_count = pd.crosstab(orders_table.Customer, orders_table.Product)

    order_amount = pd.crosstab(orders_table.Customer, orders_table.Product, orders_table.Price, aggfunc='sum').fillna(
        value=0)

    order_count.plot(kind='bar', title='Orders Count By Customers and Products')
    matplotlib.pyplot.show()
    matplotlib.pyplot.close(fig=None)

    order_amount.plot(kind='bar', title='Orders Amount By Customers and Products')
    matplotlib.pyplot.show()
    matplotlib.pyplot.close(fig=None)

    try:
        back = int(input("Go Back To ?  (1) REPORTS OPERATION   (2) USER LOGIN  (3) End and Exit        "))
    except ValueError:
        print("")
        print("")
        print("----------------------------------")
        print("ValueError : Go Back To REPORTS OPERATION")
        print("----------------------------------")
        print("")
        print("")
        extract()
    else:
        if back == 1:
            extract()
        elif back == 2:
            main.user_login()
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
            extract()
