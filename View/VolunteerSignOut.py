from tkinter import *
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm


class VolunteerSignOut:

    def __init__(self, root, volunteer, refreshfn):
        self.signout_root = Toplevel(root)
        self.signout_root.grab_set()
        self.signout_root.geometry('300x300+200+200')

        # title label
        title_label = Label(self.signout_root, text="Are you sure you wish to sign out?")
        title_label.pack(pady=5)

        # ok button
        ok_button = Button(self.signout_root, command=lambda: self.sign_out_finish(volunteer, refreshfn),
                           text=("OK"))
        ok_button.pack(fill=X)

    def sign_out_finish(self, volunteer, refreshfn):
        dm.sign_out_volunteer(volunteer)
        refreshfn()
        self.signout_root.destroy()
