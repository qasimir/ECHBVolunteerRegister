from tkinter import *
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm
from View.AdminWindow import AdminWindow


class AdminLogin:
    def __init__(self, root, settings_menu):
        login_root = Toplevel(root)
        login_root.grab_set()
        login_root.geometry('300x300+200+200')

        # title label
        title_label = Label(login_root, text="Enter Admin Password")
        title_label.pack(pady=5)

        # entry
        password_entry = Entry(login_root, show="*", width=15)
        password_entry.pack(pady=5)

        # button
        submit_button = Button(login_root, text="login",
                               command=lambda: check_login(login_root, root, password_entry,lower_label, settings_menu))
        submit_button.pack(pady=5)


        # lower label
        lower_label = Label(login_root, text="")
        lower_label.pack(pady=5)

        def check_login(login_root, root, password_entry, lower_label, settings_menu):
            password_entered = password_entry.get()
            password_entry.delete(0, len(password_entered))
            hashed_password = sm.hash_string(password_entered)
            if dm.password_hash() == hashed_password:
                settings_menu.entryconfig("New Volunteer", state=NORMAL)
                login_root.destroy()
                AdminWindow(root)
            else:
                lower_label.config(text="Incorrect Password")