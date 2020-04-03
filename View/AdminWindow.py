from tkinter import *
from Model.DataManager import DataManager as dm
from Controller.SecurityManager import SecurityManager as sm
from View.DisplayVolunteersWindow import DisplayVolunteersWindow
from View.ChangeAdminPassword import ChangeAdminPassword
from View.SumHours import SumHours
class AdminWindow:
    def __init__(self, root):
            self.admin_window = Toplevel(root)
            self.admin_window.grab_set()
            self.admin_window.geometry('500x500+200+200')
            #self.admin_window.protocol("WM_DELETE_WINDOW", self.on_closing)

            notification_label = Label(self.admin_window, text="Admin Window")
            notification_label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
            self.load_volunteers(notification_label)

            # load volunteers
            load_volunteers_button = Button(self.admin_window, command=lambda: self.load_volunteers(notification_label), text="Load Volunteers")
            load_volunteers_button.grid(column=0, row=1, padx=5, pady=5)

            #show volunteers
            show_volunteer_info_button = Button(self.admin_window,
                                                command=lambda: self.show_volunteer_info(notification_label),
                                                text="Show Volunteer Information")
            show_volunteer_info_button.grid(column=1, row=1, padx=5, pady=5)

            # sum hours
            '''sum_hours_worked_button = Button(self.admin_window, command=lambda: SumHours(self.admin_window),
                                            text="Sum Hours Worked")
            sum_hours_worked_button.grid(column=1, row=2, padx=5, pady=5)'''

            #change password
            change_password_button = Button(self.admin_window, command=lambda: ChangeAdminPassword(self.admin_window, notification_label),
                                            text="Change Password")
            change_password_button.grid(column=0, row=2, padx=5, pady=5)

            # close
            close_button = Button(self.admin_window,
                                            command=lambda: self.admin_window.destroy(),
                                            text="Close")
            close_button.grid(column=0, row=3, padx=5, pady=5, columnspan=2)


    def load_volunteers(self, notification_label):
        dm.open_and_decrypt_volunteer_info(sm.get_key_from_password())
        notification_label.config(text="Volunteers successfully loaded!")

    def show_volunteer_info(self, notification_label):
        self.load_volunteers(notification_label)
        DisplayVolunteersWindow(self.admin_window)


    '''def on_closing(self):
        sm.password_entry = None
        self.admin_window.destroy()
    '''