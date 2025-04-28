import mysql.connector
import tkinter as tk
from tkinter import messagebox
import csv

import mysql.connector
import tkinter as tk
from tkinter import messagebox
import csv

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="Mysql2025!", 
    database="school"
)
cursor = db.cursor()

# Functions
def add_student():
    name = name_entry.get()
    student_id = student_id_entry.get()
    reason = reason_entry.get()

    if name and student_id and reason:
        sql = "INSERT INTO students (name, student_id, reason) VALUES (%s, %s, %s)"
        values = (name, student_id, reason)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", f"Student {name} added!")
        name_entry.delete(0, tk.END)
        student_id_entry.delete(0, tk.END)
        reason_entry.delete(0, tk.END)
        show_students()
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

def update_student():
    try:
        selected = listbox.get(listbox.curselection())
        db_id = selected.split("|")[0].split(":")[1].strip()

        new_name = name_entry.get()
        new_student_id = student_id_entry.get()
        new_reason = reason_entry.get()

        if new_name and new_student_id and new_reason:
            sql = "UPDATE students SET name=%s, student_id=%s, reason=%s WHERE id=%s"
            values = (new_name, new_student_id, new_reason, db_id)
            cursor.execute(sql, values)
            db.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
            name_entry.delete(0, tk.END)
            student_id_entry.delete(0, tk.END)
            reason_entry.delete(0, tk.END)
            show_students()
        else:
            messagebox.showerror("Error", "Please fill out all fields.")
    except:
        messagebox.showerror("Error", "Please select a student to update.")

def delete_student():
    try:
        selected = listbox.get(listbox.curselection())
        db_id = selected.split("|")[0].split(":")[1].strip()

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
        if confirm:
            sql = "DELETE FROM students WHERE id=%s"
            cursor.execute(sql, (db_id,))
            db.commit()
            messagebox.showinfo("Success", "Student deleted successfully!")
            show_students()
    except:
        messagebox.showerror("Error", "Please select a student to delete.")

def search_by_id():
    student_id = search_id_entry.get()
    if student_id:
        sql = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        results = cursor.fetchall()
        listbox.delete(0, tk.END)
        for (id, name, student_id, reason) in results:
            listbox.insert(tk.END, f"DB_ID: {id} | Student ID: {student_id} | Name: {name} | Reason: {reason}")
    else:
        show_students()

def filter_by_reason():
    reason = filter_reason_entry.get()
    if reason:
        sql = "SELECT * FROM students WHERE reason LIKE %s"
        cursor.execute(sql, (f"%{reason}%",))
        results = cursor.fetchall()
        listbox.delete(0, tk.END)
        for (id, name, student_id, reason) in results:
            listbox.insert(tk.END, f"DB_ID: {id} | Student ID: {student_id} | Name: {name} | Reason: {reason}")
    else:
        show_students()

def clear_search_filter():
    search_id_entry.delete(0, tk.END)
    filter_reason_entry.delete(0, tk.END)
    show_students()

def sort_by_name():
    sql = "SELECT * FROM students ORDER BY name ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    listbox.delete(0, tk.END)
    for (id, name, student_id, reason) in results:
        listbox.insert(tk.END, f"DB_ID: {id} | Student ID: {student_id} | Name: {name} | Reason: {reason}")

def export_to_csv():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    with open("students.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Database ID", "Student Name", "Student ID Number", "Reason for Visit"])

        for (id, name, student_id, reason) in results:
            writer.writerow([id, name, student_id, reason])

    messagebox.showinfo("Export Complete", "Student list has been exported to students.csv successfully!")



def show_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    listbox.delete(0, tk.END)
    for (id, name, student_id, reason) in results:
        listbox.insert(tk.END, f"DB_ID: {id} | {name} | ID: {student_id} | Reason: {reason}")


# GUI
root = tk.Tk()
root.title("Student Advising Registration System")
root.geometry("800x700")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(root, text="Student Advising Registration System", font=("Helvetica", 20, "bold"), bg="#f0f8ff")
title_label.pack(pady=20)

# Form Frame
form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Student Name:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(form_frame, text="Student ID:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
student_id_entry = tk.Entry(form_frame, width=30)
student_id_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(form_frame, text="Reason for Visit:", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=10, sticky="e")
reason_entry = tk.Entry(form_frame, width=30)
reason_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Button
add_button = tk.Button(root, text="Add Student", bg="#4CAF50", fg="white", command=add_student)
add_button.pack(pady=10)
# update Button
update_button = tk.Button(root, text="Update Student", bg="#2196F3", fg="white", command=update_student)
update_button.pack(pady=10)

#delete Button
delete_button = tk.Button(root, text="Delete Student", bg="#f44336", fg="white", command=delete_student)
delete_button.pack(pady=10)


# Listbox
listbox = tk.Listbox(root, width=80, font=("Helvetica", 10))
listbox.pack(pady=20)

# Search/Filter Frame
search_frame = tk.Frame(root, bg="#f0f8ff")
search_frame.pack(pady=10)

# Clear and Sort Buttons
action_frame = tk.Frame(root, bg="#f0f8ff")
action_frame.pack(pady=10)

clear_button = tk.Button(action_frame, text="Clear Results", bg="#9E9E9E", fg="white", command=clear_search_filter)
clear_button.grid(row=0, column=0, padx=10, pady=5)

sort_button = tk.Button(action_frame, text="Sort by Name", bg="#3F51B5", fg="white", command=sort_by_name)
sort_button.grid(row=0, column=1, padx=10, pady=5)

# Search by ID
tk.Label(search_frame, text="Search by Student ID:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
search_id_entry = tk.Entry(search_frame, width=20)
search_id_entry.grid(row=0, column=1, padx=10, pady=5)
search_button = tk.Button(search_frame, text="Search", bg="#673AB7", fg="white", command=search_by_id)
search_button.grid(row=0, column=2, padx=10, pady=5)

# Filter by Reason
tk.Label(search_frame, text="Filter by Reason:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
filter_reason_entry = tk.Entry(search_frame, width=20)
filter_reason_entry.grid(row=1, column=1, padx=10, pady=5)
filter_button = tk.Button(search_frame, text="Filter", bg="#FF9800", fg="white", command=filter_by_reason)
filter_button.grid(row=1, column=2, padx=10, pady=5)

export_button = tk.Button(action_frame, text="Export to CSV", bg="#009688", fg="white", command=export_to_csv)
export_button.grid(row=0, column=2, padx=10, pady=5)


# Initial load
show_students()

# Main Loop
root.mainloop()

# Close Database
db.close()
