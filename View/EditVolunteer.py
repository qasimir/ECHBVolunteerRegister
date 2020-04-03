from tkinter import *
from Model.Volunteer import Volunteer as volunteer
from Controller.SecurityManager import SecurityManager as sm
from Model.DataManager import DataManager as dm

class EditVolunteer:
    def __init__(self, root, volunteer, display_volunteer_fn):
        self.top_window = Toplevel(root)
        self.top_window.grab_set()
        self.top_window.resizable(0, 0)

        #LabelFrame
        form_frame = LabelFrame(self.top_window, text="Edit Your details")
        form_frame.grid()

        # first name
        first_name_label = Label(form_frame, text="first name:")
        first_name_label.grid(column=0, row=0, padx=5, pady=5)

        first_name_entry = Label(form_frame, text=volunteer.first_name)
        first_name_entry.grid(column=1, row=0, padx=5, pady=5)

        # last name
        last_name_label = Label(form_frame, text="last name:")
        last_name_label.grid(column=0, row=1, padx=5, pady=5)

        last_name_entry = Label(form_frame, text=volunteer.last_name)
        last_name_entry.grid(column=1, row=1, padx=5, pady=5)

        # email
        email_label = Label(form_frame, text="email:")
        email_label.grid(column=0, row=2, padx=5, pady=5)

        email_entry = Entry(form_frame)
        email_entry.insert(END, volunteer.email)
        email_entry.grid(column=1, row=2, padx=5, pady=5)

        # phone
        phone_label = Label(form_frame, text="phone:")
        phone_label.grid(column=0, row=3, padx=5, pady=5)

        phone_entry = Entry(form_frame)
        phone_entry.insert(END, volunteer.phone)
        phone_entry.grid(column=1, row=3, padx=5, pady=5)


        #address
        address_label = Label(form_frame, text="Address:")
        address_label.grid(column=0, row=4, padx=5, pady=5)

        address_entry = Entry(form_frame)
        address_entry.insert(END, volunteer.address)
        address_entry.grid(column=1, row=4, padx=5, pady=5)

        # Area of Work - make this modular. If ECHB adds any more volunteer opportunities, then there needs to be a way to update the list of options
        area_of_work_label = Label(form_frame, text="area of work:")
        area_of_work_label.grid(column=0, row=6, padx=5, pady=5)

        area_of_work_answer = StringVar(root)
        area_of_work_answer.set(volunteer.work_area)
        area_of_work_entry = OptionMenu(form_frame, area_of_work_answer, "E-Waste", "Shop Front", "Zero Waste", "Other")
        area_of_work_entry.grid(column=1, row=6, padx=5, pady=5)

        # old_pin
        old_pin_label = Label(form_frame, text="old pin:")
        old_pin_label.grid(column=0, row=7, padx=5, pady=5)

        old_pin_entry = Entry(form_frame, show="*")
        old_pin_entry.grid(column=1, row=7, padx=5, pady=5)

        # new_pin
        new_pin_label = Label(form_frame, text="new pin:")
        new_pin_label.grid(column=0, row=8, padx=5, pady=5)

        new_pin_entry = Entry(form_frame, show="*")
        new_pin_entry.grid(column=1, row=8, padx=5, pady=5)

        # re_new_pin
        re_new_pin_label = Label(form_frame, text="re-enter new pin:")
        re_new_pin_label.grid(column=0, row=9, padx=5, pady=5)

        re_new_pin_entry = Entry(form_frame, show="*")
        re_new_pin_entry.grid(column=1, row=9, padx=5, pady=5)

        # submit button
        submit_button = Button(form_frame, text="submit",command=lambda: self.submit(
            first_name_entry,
            last_name_entry,
            email_label,
            email_entry,
            phone_label,
            phone_entry,
            address_entry,
            area_of_work_answer,
            old_pin_label,
            old_pin_entry,
            new_pin_label,
            new_pin_entry,
            re_new_pin_entry,
            volunteer,
            display_volunteer_fn
        ))
        submit_button.grid(row=10, columnspan=2, padx=5, pady=5)



    def submit(self,
               first_name,
               last_name,
               email_label,
               email_entry,
               phone_label,
               phone_entry,
               address_entry,
               area_of_work_answer,
               old_pin_label,
               old_pin_entry,
               new_pin_label,
               new_pin_entry,
               re_new_pin_entry,
               volunteer,
               display_volunteer_fn
               ):

        old_pin_hash = sm.hash_string(old_pin_entry.get())

        if not old_pin_hash == volunteer.pin_hash:
            old_pin_label.config(text="incorrect pin")
            return
        if not new_pin_entry.get() == re_new_pin_entry.get():
            new_pin_label.config(text="new pins do not match!")
            return
        if "@" not in email_entry.get():
            email_label.config(text="Invalid Email")
            return
        if not phone_entry.get().isnumeric():
            phone_label.config(text="Invalid Phone number")
            return
        else:
            new_pin_entry = new_pin_entry.get()
            pin = (old_pin_hash if new_pin_entry == "" else new_pin_entry)

            dm.edit_volunteer(
                first_name.cget("text"),
                last_name.cget("text"),
                email_entry.get(),
                phone_entry.get(),
                area_of_work_answer.get(),
                address_entry.get(),
                sm.hash_string(pin),
                sm.get_key_from_password())
            display_volunteer_fn()
            self.top_window.destroy()

