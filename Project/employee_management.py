# Emplyoee Management 
import mysql.connector

# Connect to MySQL Database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Employee_management"
        )
        if connection.is_connected():
            return connection
    except Exception as e:
        print("Error:", str(e))
    return None

# Create Employee Table
def create_employee_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(20)
        )
    """)
    connection.commit()

# Insert Employee
def insert_employee(connection, first_name, last_name, email, phone):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO employees (first_name, last_name, email, phone)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, email, phone))
    connection.commit()

# List All Employees
def list_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)

# Update Employee
def update_employee(connection, employee_id,new_phone,new_email):
    cursor = connection.cursor()
    cursor.execute("UPDATE employees SET phone = %s WHERE id = %s", (new_phone, employee_id))
    connection.commit()
    cursor.execute("UPDATE employees SET email = %s WHERE id = %s", (new_email, employee_id))
    connection.commit()
    

# Delete Employee
def delete_employee(connection, employee_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    connection.commit()

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        create_employee_table(connection)

        while True:
            print("\n                    WELCOME TO EMPLOYEE DATABASE SYSTEM         \n \n")
            
            print("Different Operations available in Database: \n")
            print("1. Add Employee Details")
            print("2. List Employees Details")
            print("3. Update Employee Email-ID")
            print("4. Delete Employee Details")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email-id: ")
                phone = input("Enter Phone number: ")
                insert_employee(connection, first_name, last_name, email, phone)
                print("\n Employee added successfully!")

            elif choice == "2":
                print("\nList of Employees:")
                list_employees(connection)

            elif choice == "3":
                employee_id = input("Enter Employee ID: ")
                new_phone = input("Enter New Phone number: ")
                update_employee(connection, employee_id, new_phone,new_email)
                print("\n Employee Phone number is update successfully!")
                new_email = input("Enter New Email-id: ")
                update_employee(connection, employee_id, new_email,new_phone )
                print("\n Employee email id is updated successfully!")

                

            elif choice == "4":
                employee_id = input("Enter Employee ID: ")
                delete_employee(connection, employee_id)
                print("\n Employee deleted successfully!")

            elif choice == "5":
                print("\n Exiting Employee Management System \n")
                print("Thank you for using our Management System!!")
                break
                
                

        connection.close()
