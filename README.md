# Office Management System
### Designed & Developed by Bhavana Kalyan

A console-based HR Management System built using Python OOP and SQLite3.
This project was conceptualized and designed entirely by me, based on 
real office workflows and HR pain points I identified independently.

---

## 💡 My Idea & Design Thinking

## 💡 Project Origin — My Own Idea

This project was NOT built from a tutorial or copied from anywhere.

The entire concept came from a real problem I identified:
> "Small and medium companies still manage employees using Excel sheets. 
> HR loses track of attendance, leaves are noted manually, and salary 
> calculations are done by hand every month. There had to be a better way."

I sat down and asked myself:
- What does an HR manager actually need daily?
- What should an employee be able to do themselves?
- What data should be private and what should be shared?
- What happens if someone enters wrong information?

Every answer to these questions became a feature in this system.
Nobody gave me these requirements — I identified them myself by 
thinking like both an HR manager AND an employee.

**The role-based access idea** — mine.
**The leave categories** — mine.  
**The end date calculation for leaves** — mine.
**Total compensation display** — mine.
**Default password with change password feature** — mine.
**Employee existence validation before any operation** — mine.

The code syntax was learned through practice and guidance.
The product thinking and feature design — entirely mine.

---

## ✨ Features I Designed

- **Role-Based Login** — Admin sees everything, Employee sees only their profile
- **Leave Management** — Categories (Personal, Medical, Official) with automatic date tracking and end-date calculation
- **Salary & Bonus Tracking** — Total compensation display per employee
- **Change Password** — With confirmation validation for security
- **Employee ID Auto-Assignment** — System generates unique IDs, no manual entry
- **Data Validation** — Employee must exist before any operation is allowed

---

## 🛠️ Technologies Used
- Python 3
- SQLite3
- OOP Concepts (Classes, Methods, Encapsulation)

---

## 📁 Project Structure
- `employee.py` — Employee class with display method (OOP)
- `database.py` — Database setup and table creation
- `app.py` — Complete application with all features

---

## 🚀 How to Run
1. Setup database: `python database.py`
2. Run application: `python app.py`
3. Default password for new employees: `welcome123`

---

## 👩‍💻 About Me
I am Bhavana Kalyan, a fresher developer with a strong focus on 
user-friendly design and practical problem solving. I believe good 
software starts with understanding real people's needs, not just 
writing code.