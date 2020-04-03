from tkinter import *
from Model.Volunteer import Volunteer as volunteer
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm

class NewVolunteer:
    def __init__(self, root):
        self.top_window = Toplevel(root)
        self.top_window.grab_set()
        self.top_window.resizable(0, 0)


        #LabelFrame
        form_frame = LabelFrame(self.top_window, text="Enter Your details")
        form_frame.grid()

        # first name
        first_name_label = Label(form_frame, text="first name:")
        first_name_label.grid(column=0, row=0, padx=5, pady=5)

        first_name_entry = Entry(form_frame)
        first_name_entry.grid(column=1, row=0, padx=5, pady=5)

        # last name
        last_name_label = Label(form_frame, text="last name:")
        last_name_label.grid(column=0, row=1, padx=5, pady=5)

        last_name_entry = Entry(form_frame)
        last_name_entry.grid(column=1, row=1, padx=5, pady=5)

        # email
        email_label = Label(form_frame, text="email:")
        email_label.grid(column=0, row=2, padx=5, pady=5)

        email_entry = Entry(form_frame)
        email_entry.grid(column=1, row=2, padx=5, pady=5)

        # phone
        phone_label = Label(form_frame, text="phone:")
        phone_label.grid(column=0, row=3, padx=5, pady=5)

        phone_entry = Entry(form_frame)
        phone_entry.grid(column=1, row=3, padx=5, pady=5)

        # address label
        address_frame = LabelFrame(form_frame, text="Address")
        address_frame.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

        # street address
        street_address_label = Label(address_frame, text="street:")
        street_address_label.grid(column=0, row=4, padx=5, pady=5)

        street_address_entry = Entry(address_frame)
        street_address_entry.grid(column=1, row=4, padx=5, pady=5)

        # town address
        town_address_label = Label(address_frame, text="town:")
        town_address_label.grid(column=0, row=5, padx=5, pady=5)

        town_address_entry = Entry(address_frame)
        town_address_entry.grid(column=1, row=5, padx=5, pady=5)

        # Area of Work - make this modular. If ECHB adds any more volunteer opportunities, then there needs to be a way to update the list of options
        area_of_work_label = Label(form_frame, text="area of work:")
        area_of_work_label.grid(column=0, row=6, padx=5, pady=5)

        area_of_work_answer = StringVar(root)
        area_of_work_answer.set("--Select One--")
        area_of_work_entry = OptionMenu(form_frame, area_of_work_answer, "E-Waste", "Shop Front", "Zero Waste", "Other")
        area_of_work_entry.grid(column=1, row=6, padx=5, pady=5)

        # pin 1
        pin_1_label = Label(form_frame, text="enter pin:")
        pin_1_label.grid(column=0, row=7, padx=5, pady=5)

        pin_1_entry = Entry(form_frame, show="*")
        pin_1_entry.grid(column=1, row=7, padx=5, pady=5)

        # pin_2
        pin_2_label = Label(form_frame, text="re-enter pin:")
        pin_2_label.grid(column=0, row=8, padx=5, pady=5)

        pin_2_entry = Entry(form_frame, show="*")
        pin_2_entry.grid(column=1, row=8, padx=5, pady=5)

        # submit button
        submit_button = Button(form_frame, text="submit",command=lambda: self.submit(
            first_name_entry,
            last_name_entry,
            email_label,
            email_entry,
            phone_label,
            phone_entry,
            street_address_entry,
            town_address_entry,
            area_of_work_answer,
            pin_1_label,
            pin_1_entry,
            pin_2_entry
        ))
        submit_button.grid(row=9, columnspan=2, padx=5, pady=5)



    def submit(self,
               first_name_entry,
               last_name_entry,
               email_label,
               email_entry,
               phone_label,
               phone_entry,
               street_address_entry,
               town_address_entry,
               area_of_work_answer,
               pin_1_label,
               pin_1_entry,
               pin_2_entry,
               ):

        if not pin_1_entry.get() == pin_2_entry.get():
            pin_1_label.config(text="Pin Numbers do not match!")
        if "@" not in email_entry.get():
            email_label.config(text="Invalid Email")
        if not phone_entry.get().isnumeric():
            phone_label.config(text="Invalid Phone number")
        else:
            dm.save_volunteer(volunteer.volunteer_from_params(
                first_name_entry.get(),
                last_name_entry.get(),
                email_entry.get(),
                sm.hash_string(pin_1_entry.get()),
                phone_entry.get(),
                street_address_entry.get() + town_address_entry.get(),
                area_of_work_answer.get(),

            ), sm.get_key_from_password() )
            self.top_window.destroy()

