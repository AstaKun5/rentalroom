import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
import main_page  # استيراد الصفحة الرئيسية

def login():
    username = username_entry.get()
    password = password_entry.get()
    # هنا يمكن إضافة التحقق من بيانات تسجيل الدخول من قاعدة البيانات
    if username == "admin" and password == "admin":  # This is just a placeholder for testing
        root.destroy()  # إغلاق نافذة تسجيل الدخول
        main_page.open_main_page()  # فتح الصفحة الرئيسية
    else:
        messagebox.showerror("Error", "Invalid username or password")

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("تسجيل الدخول")
root.geometry("400x300")
root.resizable(False, False)

# تطبيق نمط TTKBootstrap
style = Style(theme="flatly")

# إطار تسجيل الدخول
login_frame = ttk.Frame(root, padding="20 20 20 20")
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# حقل اسم المستخدم
username_label = ttk.Label(login_frame, text=":اسم المستخدم", anchor='e', justify='right')
username_label.grid(row=1, column=0, pady=(0, 5), sticky=tk.E)
username_entry = ttk.Entry(login_frame, width=30)
username_entry.grid(row=2, column=0, columnspan=2, pady=(0, 10))

# حقل كلمة المرور
password_label = ttk.Label(login_frame, text=":ادخل كلمة المرور", anchor='e', justify='right')
password_label.grid(row=3, column=0, pady=(0, 5), sticky=tk.E)
password_entry = ttk.Entry(login_frame, width=30, show="*")
password_entry.grid(row=4, column=0, columnspan=2, pady=(0, 10))

# زر تسجيل الدخول
login_button = ttk.Button(login_frame, text="تسجيل الدخول", command=login)
login_button.grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()