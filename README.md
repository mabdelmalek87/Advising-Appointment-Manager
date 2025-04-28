# Advising-Appointment-Manager
A complete CRUD desktop application built with Python, Tkinter, MySQL, and CSV Export.


A complete CRUD desktop application built with Python, Tkinter, MySQL, and CSV Export.

## Features
- Add Student
- Update Student
- Delete Student
- Search Student by ID
- Filter Students by Reason
- Sort Students by Name
- Export Student List to CSV file

## Technologies Used
- Python 3.x
- MySQL Server
- Tkinter GUI
- CSV File Handling

## Setup Instructions
1. Install Python packages:

2. Create MySQL Database:
```sql
CREATE DATABASE school;
USE school;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    student_id VARCHAR(20),
    reason VARCHAR(255)
);

Run this:
python student_gui.py


---



