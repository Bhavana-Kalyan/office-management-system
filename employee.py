class Employee:
    def __init__(self, name, phonenumber, emailaddress, 
                 department, designation, salary, bonus, 
                 password, user_type, address, joining_date):
        
        self.name = name
        self.phonenumber = phonenumber
        self.emailaddress = emailaddress
        self.department = department
        self.designation = designation
        self.salary = salary
        self.bonus = bonus
        self.password = password
        self.user_type = user_type
        self.address = address
        self.joining_date = joining_date

    def display(self):
        print("=" * 40)
        print("         Employee Profile")
        print("=" * 40)
        print(f"  Name        : {self.name}")
        print(f"  Phone       : {self.phonenumber}")
        print(f"  Email       : {self.emailaddress}")
        print(f"  Department  : {self.department}")
        print(f"  Designation : {self.designation}")
        print(f"  Salary      : Rs.{self.salary}")
        print(f"  Bonus       : Rs.{self.bonus}")
        print(f"  Address     : {self.address}")
        print(f"  Joined      : {self.joining_date}")
        print("=" * 40)