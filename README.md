# Office Management System
### Designed & Developed by Bhavana Kalyan

A console-based HR Management System built using Python OOP and SQLite3.
This project was conceptualized and designed entirely by me, based on 
real office workflows and HR pain points I identified independently.

---

## 💡 My Idea & Design Thinking

I designed this system thinking from an HR manager's perspective:
- Who uses this system? (Admins vs Employees)
- What data needs to stay private? (Employee shouldn't see others' profiles)
- What real problems does HR face? (Leave tracking, salary management)
- What edge cases could break the system? (Wrong ID, duplicate passwords)

Every feature in this project came from my own product thinking,
not from tutorials or templates.

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