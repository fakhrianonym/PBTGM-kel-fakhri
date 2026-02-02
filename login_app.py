import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_login"
)
cursor = db.cursor()

def halaman_index(nama_user):
    root.withdraw()
    
    index = tk.Toplevel()
    index.title("Halaman Index")
    index.geometry("300x200")

    tk.Label(index, text=f"Selamat Datang, {nama_user}", font=("Arial", 14)).pack(pady=20)

    def logout():
        messagebox.showinfo("Logout", "Anda telah keluar dari sistem")
        index.destroy()
        root.deiconify()

    tk.Button(index, text="Logout", command=logout, bg="red", fg="white").pack()

def login():
    username_input = entry_username.get()
    password_input = entry_password.get()

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    data = (username_input, password_input)
    cursor.execute(sql, data)

    hasil = cursor.fetchone()

    if hasil:
        messagebox.showinfo("Login", "Login berhasil!")
        halaman_index(username_input)
    else:
        messagebox.showerror("Login", "Username atau Password salah!")

root = tk.Tk()
root.title("Aplikasi Login")
root.geometry("300x250")

tk.Label(root, text="LOGIN SYSTEM", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login, bg="blue", fg="white").pack(pady=20)

root.mainloop()