import sqlite3

connection = sqlite3.connect("novacorp.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name         TEXT NOT NULL,
        phonenumber  INTEGER,
        emailaddress TEXT,
        department   TEXT,
        designation  TEXT,
        salary       INTEGER,
        bonus        INTEGER,
        password     TEXT,
        user_type    TEXT,
        address      TEXT,
        joining_date TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS leave_records (
        leave_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id       INTEGER,
        leave_type   TEXT,
        days         INTEGER,
        date         TEXT
    )
""")

connection.commit()
print("Database ready!")
# cursor.execute("""
#     INSERT INTO employees (name, phonenumber, emailaddress, department, 
#     designation, salary, bonus, password, user_type, address, joining_date)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """, ("Aradhya", 9999999999, "gh23435@gmail.com", "HR", 
#       "Recruiter", 50000, 6000, "admin123", "admin", 
#       "Yelahanka main town", "14-02-2024"))

connection.close()