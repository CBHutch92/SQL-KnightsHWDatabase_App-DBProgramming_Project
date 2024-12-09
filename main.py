# Casey Hutchinson
# ITEC 4244 Final Project
# Due by 12/07/2024

import pyodbc
from prettytable import PrettyTable

SERVER = 'cbhutch_laptop\\SQLEXPRESS'
DATABASE = 'KnightHardwareDB'
USERNAME = 'sa'
PASSWORD = 'password'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

def KnightHardware():
    while True:
        print("\n")
        print("Welcome to the Knight Hardware Database App")
        print("This is a beta version of the app meant to demonstrate what a full app could do.")
        print("Please select from the following options below")
        print("1. SELECT all of the entries from the Customers table")
        print("2. INSERT an Air Fryer entry to the Parts table, and show the new table")
        print("3. UPDATE the Order Date for OrderNumber 21608 in the Orders table")
        print("4. DELETE OrderNumber 21623 from the OrderDetails table")
        print("5. Exit the app")
        print("\n")
        choice = input("Please enter a 1-5 for your choice from the menu above: ")
        print("\n")
        if choice == "1":
            select = '''Select * From Customers'''
            cursor.execute(select)
            records = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Customer Number", "Customer Name", "City", "State"]
            for r in records:
                table.add_row([r.CustomerNumber, r.CustomerName, r.City, r.State])
            print(table)
        elif choice == "2":
            insert = '''Insert INTO Parts (
            PartNumber,
            PartDescription,
            InventoryOnHand,
            Price)
            VALUES (?, ?, ?, ?)'''
            data = ("AF36", "Air Fryer", "20", "99.99")
            cursor.execute(insert, data)
            conn.commit()

            print("Success. Here is the updated table:")
            cursor.execute("SELECT * FROM Parts")
            records = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Part Number", "Part Description", "Inventory On Hand", "Price"]
            for r in records:
                table.add_row([r.PartNumber, r.PartDescription, r.InventoryOnHand, r.Price])
            print(table)
        elif choice == "3":
            update = "UPDATE Orders SET OrderDate = '2017-10-18' WHERE OrderNumber = 21608"
            cursor.execute(update)
            conn.commit()

            print("Success. Here is the updated table:")
            cursor.execute("SELECT * FROM Orders")
            records = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Order Number", "Customer Number", "Order Date"]
            for r in records:
                table.add_row([r.OrderNumber, r.CustomerNumber, r.OrderDate])
            print(table)
        elif choice == "4":
            delete = "DELETE FROM OrderDetails WHERE OrderNumber = 21623"
            cursor.execute(delete)
            conn.commit()

            print("Success. Here is the updated table:")
            cursor.execute("SELECT * FROM OrderDetails")
            records = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Order Number", "Part Number", "Number Ordered"]
            for r in records:
                table.add_row([r.OrderNumber, r.PartNumber, r.NumberOrdered])
            print(table)
        elif choice == "5":
            print("\n")
            print("Thank you for using the Knight Hardware Database app.")
            exit()
        else:
            print("Invalid input. Please enter a 1-5.")

def main():
    KnightHardware()

if __name__ == "__main__":
    main()

cursor.close()
conn.close()
