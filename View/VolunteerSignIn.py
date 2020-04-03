from tkinter import *
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm


class VolunteerSignIn:
    def __init__(self, root, volunteer, refreshfn):
        self.root_main = root
        self.signin_root = Toplevel(root)
        self.signin_root.grab_set()
        self.signin_root.geometry('300x300+200+200')

        # title label
        title_label = Label(self.signin_root, text="Enter your pin")
        title_label.pack(pady=5)

        # entry
        pin_entry = Entry(self.signin_root, show="*", width=15)
        pin_entry.pack(pady=5)

        # button
        submit_button = Button(self.signin_root, text="sign in",
                               command=lambda: self.check_signin(pin_entry, lower_label, volunteer, refreshfn))
        submit_button.pack(pady=5)


        # lower label
        lower_label = Label(self.signin_root, text="")
        lower_label.pack(pady=5)

    def check_signin(self, pin_entry, lower_label, volunteer, refreshfn):
        pin_entered = pin_entry.get()
        pin_entry.delete(0, len(pin_entered))
        hashed_pin = sm.hash_string(pin_entered)
        if volunteer.pin_hash == hashed_pin:
            lower_label.config(text="correct pin")
            dm.sign_in_volunteer(volunteer)
            refreshfn()
            self.signin_root.destroy()

        else:
            lower_label.config(text="Incorrect pin")
