import os
from Model.VolunteerSession import VolunteerSession
from datetime import datetime


class VolunteerSessionManager:

    volunteer_sessions = []

    def __init__(self, records_folder, volunteer_session_file_string):
        self.records_folder = records_folder
        self.volunteer_session_file_string = volunteer_session_file_string
        self.time_format = "%H:%M"
        self.blank_time = "-"
        self.date_file_append = "_%Y_%m_%d"
        self.file_end = ".csv"

    def sum_hours_worked(self, start_date, end_date):
        if end_date.strftime("%Y%m%d") < start_date.strftime("%Y%m%d"):
            return
        running_date = start_date
        running_total = 0
        while True:
            running_total += self.sum_hours_in_day(running_date)
            if running_date.strftime("%d%m%Y") == end_date.strftime("%d%m%Y"):
                break
            running_date += running_date.timedelta(days=1)
        return running_total

    def sum_hours_in_day(self, date):
        date_string = date.strftime("%d_%m_%Y")
        file_path = self.records_folder + self.volunteer_session_file_string + date_string
        if not os.path.exists(file_path):
            print("no file for date:" + date_string)
            # TODO add logging here
        else:
            session_file = open(file_path, 'r')
            lines = session_file.readlines()
            running_total = 0
            for line in lines:
                fields = line.split(",")

                start_string = fields[2]
                end_string = fields[3]

                start_time = datetime.strptime(start_string, self.time_format)
                end_time = datetime.strptime(end_string, self.time_format)

                diff = start_time - end_time
                running_total += diff.total_seconds()/3600 # to get it into hours

            session_file.close()
            return running_total

    def sign_in_volunteer(self, volunteer):
        now = datetime.now()
        volunteer_session = VolunteerSession(
            volunteer.first_name,
            volunteer.last_name,
            now.strftime(self.time_format),
            self.blank_time,
            volunteer.work_area
        )
        self.volunteer_sessions.append(volunteer_session)
        self.save_volunteer_sessions()

    def sign_out_volunteer(self, volunteer):
        now = datetime.now()
        updated = False
        for volunteer_session in self.volunteer_sessions:
            if (
                volunteer_session.end_time == "-" and
                volunteer.first_name == volunteer_session.first_name and
                volunteer.last_name == volunteer_session.last_name
            ):
                volunteer_session.end_time = now.strftime(self.time_format)
                updated = True
                break
        if not updated:
            print("ERROR! could not find the record to update!")
            #log this
        self.save_volunteer_sessions()

    def load_volunteer_sessions(self):
        now = datetime.now()
        date_string = now.strftime(self.date_file_append)
        file_path = self.records_folder + self.volunteer_session_file_string + date_string + self.file_end
        if not os.path.exists(file_path):
            print("making the volunteer sessions file")
            # TODO add logging here
            session_file = open(file_path, 'w')
            session_file.close()
        else:
            session_file = open(file_path, 'r+')
            lines = session_file.readlines()
            for line in lines:
                fields = line.split(",")
                volunteer_session = VolunteerSession(
                    fields[0],
                    fields[1],
                    fields[2],
                    fields[3],
                    fields[4]
                )
                self.volunteer_sessions.append(volunteer_session)
                session_file.close()

    def save_volunteer_sessions(self):
        """
        we want to overwrite what is already in the file.
        The volunteer_sessions loaded in the program should represent the most complete version
        """
        now = datetime.now()
        date_string = now.strftime(self.date_file_append)
        file_path = self.records_folder + self.volunteer_session_file_string + date_string + self.file_end
        if not os.path.exists(file_path):
            print("ERROR! No volunteer sessions file!")
            # TODO add logging here
        else:
            session_file = open(file_path, 'w')
            data = ""
            for volunteer_session in self.volunteer_sessions:
                data += volunteer_session.first_name.lstrip()
                data += ","
                data += volunteer_session.last_name
                data += ","
                data += volunteer_session.start_time
                data += ","
                data += volunteer_session.end_time
                data += ","
                data += volunteer_session.area_of_work.rstrip()
                data += "\n"
            session_file.write(data)
            session_file.close()

    def update_sign_in_status(self, volunteers):
        for volunteer in volunteers:
            for volunteer_session in self.volunteer_sessions:
                if (
                    volunteer.first_name == volunteer_session.first_name and
                    volunteer.last_name == volunteer_session.last_name
                ):
                    volunteer.signed_in = (volunteer_session.end_time == self.blank_time)



