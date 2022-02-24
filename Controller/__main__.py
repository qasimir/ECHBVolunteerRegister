import sys
from tkinter import *
from Model.DataManager import DataManager as dm
from Controller.SecurityManager import SecurityManager as sm
from View.AdminLogin import AdminLogin
from View.NewVolunteer import NewVolunteer
from View.VolunteerSignIn import VolunteerSignIn
from View.VolunteerSignOut import VolunteerSignOut

class mainWindow:

    title = "Environment Centre Hawke's Bay Volunteer Register"

    def __init__(self):

        if sys.argv[1] is not None:
            dm.set_connection_param("Domain",sys.argv[1])
        else:
            print("No server name specified. Saving locally")
        if sys.argv[2] is not None:
            dm.set_connection_param("Port",sys.argv[2])
        else:
            print("No port number specified.")

        #First, load the encryption config files
        dm.load_config()

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # REMOVE THIS AFTER TESTING
        dm.open_and_decrypt_volunteer_info(sm.get_key_from_password())
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        dm.load_volunteer_sessions_file()

        # set up the project and the frames
        #######################################
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry('500x500+200+200')
        #######################################

        # set up the toolbar
        #######################################
        # set up the task menu. The one at the top.
        menu_bar = Menu(self.root)
        # ? sets the menu at the top to be the menu_bar
        self.root.config(menu=menu_bar)
        # creates a sub menu of the menu bar
        settings_menu = Menu(menu_bar)
        settings_menu.add_command(label="New Volunteer", command=self.new_volunteer, state=DISABLED)#!!!!!!!!!! was state=NORMAL/DISABLED for testing
        settings_menu.add_command(label="Admin Login", command=lambda: self.admin_login(settings_menu))

        # turns the settings menu into a cascade, and thus it can be rendered
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        menu_bar.add_command(label="Refresh", command=self.refresh)
        #######################################

        # add the frames
        #######################################

        self.mainFrame = LabelFrame(self.root, text="Volunteer Sign-in")
        self.mainFrame.pack(fill=BOTH)

        #left hand side
        self.left_side = LabelFrame(self.mainFrame, text="Signed Out")
        self.left_side.pack(side=LEFT, fill=X, expand=True)

        self.left_scroll = Scrollbar(self.left_side)
        self.left_scroll.pack(side=RIGHT, fill=Y)

        self.left_canvas = Canvas(self.left_side, yscrollcommand=self.left_scroll.set)
        self.left_canvas.pack(fill=X, expand=True)

        self.left_scroll.config(command=self.left_canvas.yview)


        # right hand side
        self.right_side = LabelFrame(self.mainFrame, text="Signed In")
        self.right_side.pack(side=RIGHT, fill=X, expand=True)

        self.right_scroll = Scrollbar(self.right_side)
        self.right_scroll.pack(side=RIGHT, fill=Y)

        self.right_canvas = Canvas(self.right_side, yscrollcommand=self.right_scroll.set)
        self.right_canvas.pack(fill=X, expand=True)

        #######################################

        #load the files
        #######################################
        self.refresh()
        #######################################

        self.root = mainloop()

    def new_volunteer(self):
       NewVolunteer(self.root)

    def sign_in_volunteer(self, volunteer):
        VolunteerSignIn(self.root, volunteer, self.refresh)

    def sign_out_volunteer(self, volunteer):
        VolunteerSignOut(self.root, volunteer, self.refresh)

    def admin_login(self, settings_menu):
        AdminLogin(self.root, settings_menu)

    def refresh(self):
        self.clear_screen()
        self.update_sign_in_status()
        self.display_volunteers()

        self.left_canvas.config(scrollregion=self.left_canvas.bbox("all"))
        #self.right_canvas.config(scrollregion=self.canvas.bbox("all"))

    def clear_screen(self):
        for child in self.left_canvas.winfo_children():
            child.destroy()

        for child in self.right_canvas.winfo_children():
            child.destroy()

    def update_sign_in_status(self):
        dm.update_sign_in_status()

    def display_volunteers(self):
        for volunteer in dm.volunteers:
            if volunteer.signed_in:
                volunteer_button = Button(self.right_canvas,
                                          command=lambda v=volunteer: self.sign_out_volunteer(v),
                                          text=(volunteer.first_name + " " + volunteer.last_name))
                volunteer_button.pack(fill=X)
            else:
                volunteer_button = Button(self.left_canvas,
                                          command=lambda v=volunteer: self.sign_in_volunteer(v),
                                          text=(volunteer.first_name + " " + volunteer.last_name))
                volunteer_button.pack(fill=X)


mainWindow()

