from employee import Employee
import sqlite3

connection = sqlite3.connect("novacorp.db")
cursor = connection.cursor()

def login():
    print("=" * 36)
    print("  NovaCorp Management Suite")
    print("=" * 36)
    
    emp_id = input("Enter Employee ID : ")
    password = input("Enter Password    : ")
    
    cursor.execute("SELECT * FROM employees WHERE emp_id = ? AND password = ?", (emp_id, password))
    result = cursor.fetchone()
    
    if result:
        print("\nLogin successful!")
        if result[9] == "admin":
            print(f"Welcome, {result[1]}! (Admin)")
            show_admin_menu()
        else:
            print(f"Welcome, {result[1]}! (Employee)")
            show_employee_menu()
    else:
        print("Invalid ID or Password. Please try again.")


def add_employee():
    print("=" * 36)
    print("      Add New Employee")
    print("=" * 36)
    
    name = input("Enter Name           : ")
    phonenumber = input("Enter Phone          : ")
    emailaddress = input("Enter Email          : ")
    department = input("Enter Department     : ")
    designation = input("Enter Designation    : ")
    salary = int(input("Enter Salary         : "))
    bonus = int(input("Enter Bonus          : "))
    password = "welcome123"
    print("Default password set: welcome123")
    user_type = input("User Type(admin/employee): ")
    address = input("Enter Address        : ")
    joining_date = input("Enter Joining Date   : ")

    emp = Employee(name, phonenumber, emailaddress,
                   department, designation, salary, bonus,
                   password, user_type, address, joining_date)

    cursor.execute("""
        INSERT INTO employees 
        (name, phonenumber, emailaddress, department,
        designation, salary, bonus, password, 
        user_type, address, joining_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (emp.name, emp.phonenumber, emp.emailaddress,
          emp.department, emp.designation, emp.salary,
          emp.bonus, emp.password, emp.user_type,
          emp.address, emp.joining_date))

    connection.commit()
    cursor.execute("SELECT emp_id FROM employees WHERE emailaddress = ?", (emp.emailaddress,))
    new_emp = cursor.fetchone()
    print(f"Employee ID assigned: {new_emp[0]}")
    print("Please share this ID with the employee for login!")
    print("\nEmployee added successfully!")
    emp.display()


def view_all_employees():
    print("=" * 36)
    print("  View All Employees")
    print("=" * 36)
    
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            emp = Employee(row[1], row[2], row[3], row[4], row[5],
                          row[6], row[7], row[8], row[9], row[10], row[11])
            emp.display()
    else:
        print("No employees found!")


def delete_employee():
    print("=" * 36)
    print("    Delete Employee")
    print("=" * 36)
    
    deletion = int(input("Enter Employee ID to delete: "))
    
    cursor.execute("DELETE FROM employees WHERE emp_id = ?", (deletion,))
    connection.commit()
    
    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee ID not found. Please recheck.")


def update_salary():
    print("=" * 36)
    print("   Update Employee Salary")
    print("=" * 36)
    
    upd = int(input("Enter Employee ID : "))
    
    cursor.execute("SELECT salary FROM employees WHERE emp_id = ?", (upd,))
    row = cursor.fetchone()
    
    if row:
        old_salary = row[0]
        new_sal = int(input("Enter New Salary  : "))
        
        cursor.execute("UPDATE employees SET salary = ? WHERE emp_id = ?", (new_sal, upd))
        connection.commit()
        
        print(f"Salary updated successfully!")
        print(f"Old Salary : Rs.{old_salary}")
        print(f"New Salary : Rs.{new_sal}")
    else:
        print("Employee ID not found!")


def update_bonus():
    print("=" * 36)
    print("   Update Employee Bonus")
    print("=" * 36)

    bon = int(input("Enter Employee ID : "))
    
    cursor.execute("SELECT bonus FROM employees WHERE emp_id = ?", (bon,))
    row = cursor.fetchone()

    if row:
        old_bonus = row[0]
        new_bon = int(input("Enter New Bonus   : "))
        
        cursor.execute("UPDATE employees SET bonus = ? WHERE emp_id = ?", (new_bon, bon))
        connection.commit()
        
        cursor.execute("SELECT salary, bonus FROM employees WHERE emp_id = ?", (bon,))
        current = cursor.fetchone()
        
        total = current[0] + current[1]
        print(f"Bonus updated successfully!")
        print(f"New Bonus          : Rs.{new_bon}")
        print(f"Total Compensation : Rs.{total}")
    else:
        print("Employee ID not found!")


def view_profile():
    print("=" * 36)
    print("   View Profile Section")
    print("=" * 36)

    em_id = int(input("Enter Employee ID : "))
    
    cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (em_id,))
    row = cursor.fetchone()

    if row:
        emp = Employee(row[1], row[2], row[3], row[4], row[5],
                      row[6], row[7], row[8], row[9], row[10], row[11])
        emp.display()
    else:
        print("Employee ID not found!")


def apply_leave():
    print("=" * 36)
    print("      Apply for Leave")
    print("=" * 36)

    em_id = int(input("Enter Your Employee ID : "))

    cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (em_id,))
    check = cursor.fetchone()

    if not check:
        print("Employee ID not found!")
        return

    print("Select Leave Type:")
    print("1. Personal")
    print("2. Medical")
    print("3. Official")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        leave_type = "Personal"
    elif choice == 2:
        leave_type = "Medical"
    elif choice == 3:
        leave_type = "Official"
    else:
        print("Invalid choice!")
        return

    num_days = int(input("How many days leave : "))

    from datetime import date, timedelta
    today = str(date.today())
    end_date = str(date.today() + timedelta(days=num_days))

    cursor.execute("""
        INSERT INTO leave_records (emp_id, leave_type, days, date)
        VALUES (?, ?, ?, ?)
    """, (em_id, leave_type, num_days, today))

    connection.commit()
    print("Leave applied successfully!")
    print(f"Leave Type  : {leave_type}")
    print(f"Days        : {num_days}")
    print(f"Leave From  : {today}")
    print(f"Leave Until : {end_date}")


def view_leave_records():
    print("=" * 36)
    print("    Leave Records")
    print("=" * 36)
    
    cursor.execute("SELECT * FROM leave_records")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print("=" * 36)
            print(f"  Employee ID : {row[1]}")
            print(f"  Leave Type  : {row[2]}")
            print(f"  Days        : {row[3]}")
            print(f"  Date        : {row[4]}")
    else:
        print("No leave records found!")


def change_password():
    print("=" * 36)
    print("     Change Password")
    print("=" * 36)
    
    em_id = int(input("Enter Your Employee ID : "))
    old_pass = input("Enter Current Password : ")
    
    cursor.execute("SELECT * FROM employees WHERE emp_id = ? AND password = ?", (em_id, old_pass))
    check = cursor.fetchone()
    
    if check:
        new_pass = input("Enter New Password     : ")
        confirm = input("Confirm New Password   : ")
        
        if new_pass == confirm:
            cursor.execute("UPDATE employees SET password = ? WHERE emp_id = ?", (new_pass, em_id))
            connection.commit()
            print("Password changed successfully!")
        else:
            print("Passwords don't match! Try again.")
    else:
        print("Invalid ID or Password!")


def show_admin_menu():
    while True:
        print("=" * 36)
        print("       Admin Menu")
        print("=" * 36)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. View Single Employee")
        print("4. Delete Employee")
        print("5. Update Salary")
        print("6. Update Bonus")
        print("7. View Leave Records")
        print("8. Exit")
        print("=" * 36)
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_all_employees()
        elif choice == 3:
            view_profile()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            update_salary()
        elif choice == 6:
            update_bonus()
        elif choice == 7:
            view_leave_records()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


def show_employee_menu():
    while True:
        print("=" * 36)
        print("     Employee Menu")
        print("=" * 36)
        print("1. View My Profile")
        print("2. Apply Leave")
        print("3. Change Password")
        print("4. Exit")
        print("=" * 36)
        
        choice = int(input("Enter your choice : "))

        if choice == 1:
            view_profile()
        elif choice == 2:
            apply_leave()
        elif choice == 3:
            change_password()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# Check existing users
cursor.execute("SELECT emp_id, name, password, user_type FROM employees")
rows = cursor.fetchall()
print("Current users in database:")
for row in rows:
    print(row)

login()