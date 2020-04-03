import os
from cryptography.fernet import Fernet
from Model.Volunteer import Volunteer

class VolunteerInfoManager:

    def __init__(self, records_folder, volunteer_info_file_string, volunteers):
        self.records_folder = records_folder
        self.volunteer_info_file_string = volunteer_info_file_string
        self.volunteers = volunteers

    def open_and_decrypt_volunteer_info(self, key):
        if not os.path.exists(self.records_folder + self.volunteer_info_file_string):
            print("making file")
            # TODO add logging here
            volunteer_info_file = open(self.records_folder + self.volunteer_info_file_string, 'w')
            volunteer_info_file.close()

        volunteer_info_file = open(self.records_folder + self.volunteer_info_file_string, 'rb')
        with volunteer_info_file as f:
            data = f.read()
        if not data == b'':
            fernet = Fernet(key)
            raw_data = fernet.decrypt(data)
            volunteer_raw_data = raw_data.decode("utf-8").split(';')
            volunteer_raw_data = volunteer_raw_data[:len(volunteer_raw_data)-1]# to remove the trailing ";"

            if len(self.volunteers) > 0:
                #log this
                self.volunteers.clear()
            for volunteer_str in volunteer_raw_data:
                volunteer = Volunteer()
                attributes = volunteer_str.split(",")

                volunteer.first_name = attributes[0]
                volunteer.last_name = attributes[1]
                volunteer.email = attributes[2]
                volunteer.pin_hash = attributes[3]
                volunteer.phone = attributes[4]
                volunteer.address = attributes[5]
                volunteer.work_area = attributes[6]

                self.volunteers.append(volunteer)

    def save_and_encrypt_volunteer_info(self, key):
        data = ""
        if len(self.volunteers) > 0:
            for volunteer in self.volunteers:
                data += (volunteer.first_name + "," +
                         volunteer.last_name + "," +
                         volunteer.email + "," +
                         volunteer.pin_hash + "," +
                         volunteer.phone + "," +
                         volunteer.address + "," +
                         volunteer.work_area + ";")
            volunteer_info_file = open(self.records_folder + self.volunteer_info_file_string, 'wb')
            fernet = Fernet(key)
            encrypted = fernet.encrypt(str.encode(data))

            with volunteer_info_file as f:
                f.write(encrypted)
        else:
            print("nothing to save")
            # we need to log this as an error
