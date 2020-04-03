from tkinter import *
from Model.DataManager import DataManager as dm
from View.EditVolunteer import EditVolunteer
from View.DeleteVolunteer import DeleteVolunteer
from datetime import datetime


class SumHours:
    def __init__(self, root):
        self.sum_window = Toplevel(root)
        self.sum_window.grab_set()
        self.sum_window.resizable(0, 0)

        start_frame = LabelFrame(self.sum_window, text="start date")
        start_frame.grid(row=0, column=0, sticky='w')

        end_frame = LabelFrame(self.sum_window, text="end date")
        end_frame.grid(row=0, column=1, sticky='E')

        #labels
        s_day_label = Label(start_frame, text="day")
        s_day_label.grid(row=0, column=0,padx=2, pady=2)

        e_day_label = Label(end_frame, text="day")
        e_day_label.grid(row=0, column=0, padx=2, pady=2)

        s_month_label = Label(start_frame, text="month")
        s_month_label.grid(row=0, column=1, padx=2, pady=2)

        e_month_label = Label(end_frame, text="month")
        e_month_label.grid(row=0, column=1, padx=2, pady=2)

        s_year_label = Label(start_frame, text="year")
        s_year_label.grid(row=0, column=2, padx=2, pady=2)

        e_year_label = Label(end_frame, text="year")
        e_year_label.grid(row=0, column=2, padx=2, pady=2)

        #entrys
        s_day_entry = Entry(start_frame)
        s_day_entry.grid(row=1, column=0, padx=2, pady=2)

        e_day_entry = Entry(end_frame)
        e_day_entry.grid(row=1, column=0, padx=2, pady=2)

        s_month_entry = Entry(start_frame)
        s_month_entry.grid(row=1, column=1, padx=2, pady=2)

        e_month_entry = Entry(end_frame)
        e_month_entry.grid(row=1, column=1, padx=2, pady=2)

        s_year_entry = Entry(start_frame)
        s_year_entry.grid(row=1, column=2, padx=2, pady=2)

        e_year_entry = Entry(end_frame)
        e_year_entry.grid(row=1, column=2, padx=2, pady=2)

        # result_label
        result_label = Label(self.sum_window, text=" ")
        result_label.grid(row=2, column=0, padx=2, pady=10)

        # Button
        calculate_button = Button(self.sum_window, text="calculate",
                                  command=lambda: self.sum_hours(s_day_entry,
                                                                 s_month_entry,
                                                                 s_year_entry,
                                                                 e_day_entry,
                                                                 e_month_entry,
                                                                 e_year_entry,
                                                                 result_label))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=2, padx=2)



    def sum_hours(self,
                s_day_entry,
                s_month_entry,
                s_year_entry,
                e_day_entry,
                e_month_entry,
                e_year_entry,
                result_label):
        s_day = s_day_entry.get()
        s_month = s_month_entry.get()
        s_year = s_year_entry.get()
        e_day = e_day_entry.get()
        e_month = e_month_entry.get()
        e_year = e_year_entry.get()

        # do some checking stuff here
        start_date = datetime.strptime((s_day + " " + s_month + " " + s_year), "%d %m %Y")
        end_date = datetime.strptime((e_day + " " + e_month + " " + e_year), "%d %m %Y")
        result = dm.sum_hours_worked(start_date, end_date)
        result_label.config(text=(result + " hours worked."))

