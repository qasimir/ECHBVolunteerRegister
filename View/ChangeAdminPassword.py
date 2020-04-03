from tkinter import *
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm

class ChangeAdminPassword:
    def __init__(self, root, notification_label):
        self.top_window = Toplevel(root)
        self.top_window.grab_set()
        self.top_window.resizable(0, 0)


        #LabelFrame
        form_frame = LabelFrame(self.top_window, text="Change your Password")
        form_frame.grid()

        # old_password
        old_password_label = Label(form_frame, text="old password:")
        old_password_label.grid(column=0, row=7, padx=5, pady=5)

        old_password_entry = Entry(form_frame, show="*")
        old_password_entry.grid(column=1, row=7, padx=5, pady=5)

        # new_password
        new_password_label = Label(form_frame, text="new password:")
        new_password_label.grid(column=0, row=8, padx=5, pady=5)

        new_password_entry = Entry(form_frame, show="*")
        new_password_entry.grid(column=1, row=8, padx=5, pady=5)

        # re_new_password
        re_new_password_label = Label(form_frame, text="re-enter new password:")
        re_new_password_label.grid(column=0, row=9, padx=5, pady=5)

        re_new_password_entry = Entry(form_frame, show="*")
        re_new_password_entry.grid(column=1, row=9, padx=5, pady=5)

        # submit button
        submit_button = Button(form_frame, text="submit",command=lambda: self.submit(
            old_password_label,
            old_password_entry,
            new_password_label,
            new_password_entry,
            re_new_password_entry,
            notification_label
        ))
        submit_button.grid(row=10, columnspan=2, padx=5, pady=5)



    def submit(self,
               old_password_label,
               old_password_entry,
               new_password_label,
               new_password_entry,
               re_new_password_entry,
               notification_label
               ):

        old_password_hash = sm.hash_string(old_password_entry.get())

        if not old_password_hash == dm.password_hash():
            old_password_label.config(text="incorrect password")
            return
        if not new_password_entry.get() == re_new_password_entry.get():
            new_password_label.config(text="new passwords do not match!")
            return
        else:
            dm.change_password(sm.hash_string(new_password_entry.get()))
            # need to re-encrypt the volunteer data, using the new key

            notification_label.config(text="Password Changed Successfully")
            self.top_window.destroy()

