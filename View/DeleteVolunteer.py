from tkinter import *
from Model.DataManager import DataManager as dm
from Controller.SecurityManager import SecurityManager as sm

class DeleteVolunteer:

    def __init__(self, root, volunteer, display_volunteer_fn):
        self.delete_root = Toplevel(root)
        self.delete_root.grab_set()
        self.delete_root.resizable(0, 0)

        # title label
        title_label = Label(self.delete_root,
                            text="Are you sure you wish to delete this volunteer:\n" +
                                 volunteer.first_name + " " +
                                 volunteer.last_name + "?")
        title_label.pack(pady=5)

        # ok button
        ok_button = Button(self.delete_root, command=lambda: self.delete_finish(volunteer, display_volunteer_fn),
                           text=("OK"))
        ok_button.pack(fill=X)

    def delete_finish(self, volunteer, display_volunteer_fn):
        dm.delete_volunteer(volunteer,sm.get_key_from_password())
        display_volunteer_fn()
        self.delete_root.destroy()