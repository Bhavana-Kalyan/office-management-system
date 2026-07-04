welcome="SKYTECH INDUSTRIES Office Management System"
print(welcome)
print("Employee_Registration")
employee_id=int(input("Enter Employee ID : "))
employee_name=input("Enter your name: ")
department=input("Enter your department name:")
role=input("Enter your role: ")
employee={
    "ID":employee_id,
    "name":employee_name,
    "department":department,
    "role" : role
}
print(employee)

