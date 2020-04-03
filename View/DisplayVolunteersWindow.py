from tkinter import *
from Model.DataManager import DataManager as dm
from View.EditVolunteer import EditVolunteer
from View.DeleteVolunteer import DeleteVolunteer


class DisplayVolunteersWindow:

    def __init__(self, root):
        self.display_volunteers_window = Toplevel(root)
        self.display_volunteers_window.grab_set()
        self.display_volunteers_window.resizable(0, 0)

        self.print_titles()
        self.display_volunteers()



    def display_volunteers(self):

        rowcount = 1
        for volunteer in dm.volunteers:
            volunteer_fn_label = Label(self.display_volunteers_window, text=volunteer.first_name)
            volunteer_ln_label = Label(self.display_volunteers_window, text=volunteer.last_name)
            volunteer_email_label = Label(self.display_volunteers_window, text=volunteer.email)
            volunteer_phone_label = Label(self.display_volunteers_window, text=volunteer.phone)
            volunteer_address_label = Label(self.display_volunteers_window, text=volunteer.address)
            volunteer_area_label = Label(self.display_volunteers_window, text=volunteer.work_area)

            volunteer_fn_label.grid(row=rowcount, column=0)
            volunteer_ln_label.grid(row=rowcount, column=1)
            volunteer_email_label.grid(row=rowcount, column=2)
            volunteer_phone_label.grid(row=rowcount, column=3)
            volunteer_address_label.grid(row=rowcount, column=4)
            volunteer_area_label.grid(row=rowcount, column=5)

            edit_button = Button(
                self.display_volunteers_window,
                text="Edit Volunteer",
                command=lambda vol=volunteer: EditVolunteer(self.display_volunteers_window, vol, self.refresh))
            edit_button.grid(row=rowcount, column=6, padx=5, pady=5)

            delete_button = Button(
                self.display_volunteers_window,
                text="Delete Volunteer",
                command=lambda vol=volunteer: DeleteVolunteer(self.display_volunteers_window, vol, self.refresh))
            delete_button.grid(row=rowcount, column=7, padx=5, pady=5)

            rowcount += 1

        ok_button = Button(self.display_volunteers_window, text="OK",
                           command=lambda: self.display_volunteers_window.destroy())
        ok_button.grid(row=rowcount, column=2, columnspan=2, padx=5, pady=5)


    def print_titles(self):
        fn_Label = Label(self.display_volunteers_window, text="First Name")
        fn_Label.grid(row=0, column=0)

        ln_Label = Label(self.display_volunteers_window, text="Last Name")
        ln_Label.grid(row=0, column=1)

        email_Label = Label(self.display_volunteers_window, text="Email")
        email_Label.grid(row=0, column=2)

        phone_Label = Label(self.display_volunteers_window, text="Phone")
        phone_Label.grid(row=0, column=3)

        address_Label = Label(self.display_volunteers_window, text="Address")
        address_Label.grid(row=0, column=4)

        work_area_Label = Label(self.display_volunteers_window, text="Work Area")
        work_area_Label.grid(row=0, column=5)

    def refresh(self):
        for child in self.display_volunteers_window.winfo_children():
            child.destroy()
        self.print_titles()
        self.display_volunteers()