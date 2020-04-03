import os
from datetime import date
from Model.VolunteerInfoManager import VolunteerInfoManager
from Model.VolunteerSessionManager import VolunteerSessionManager
from Controller.SecurityManager import SecurityManager as sm


class DataManager:

    records_folder = os.getcwd() + "\\" #"C:\\Records\\"
    volunteer_info_file_string = "volunteerList.txt"
    volunteer_session_file_string = "volunteerHours"
    config_file_string = "config.txt"
    volunteers = []

    volunteer_info_manager = VolunteerInfoManager(records_folder, volunteer_info_file_string, volunteers)
    volunteer_session_manager = VolunteerSessionManager(records_folder, volunteer_session_file_string)



    @staticmethod
    def save_volunteer(volunteer, key):
        DataManager.volunteers.append(volunteer)
        DataManager.volunteers = sorted(DataManager.volunteers, key=lambda volunteer: volunteer.first_name)
        DataManager.save_and_encrypt_volunteer_info(key)

    @staticmethod
    def edit_volunteer(first_name, last_name, email, phone, work_area, address, new_pin_hash, key):
        for vol in DataManager.volunteers:
            if first_name == vol.first_name and last_name == vol.last_name:
                vol.email = email
                vol.phone = phone
                vol.address = address
                vol.work_area = work_area
                vol.pin_hash = new_pin_hash
        DataManager.save_and_encrypt_volunteer_info(key)

    @staticmethod
    def load_config():
        sm.load_config(DataManager.records_folder + DataManager.config_file_string)

    @staticmethod
    def password_hash():
        return sm.password_hash

    @staticmethod
    def salt():
        return sm.salt

    @staticmethod
    def change_password(new_password_hash):
        if not os.path.exists(DataManager.records_folder + DataManager.config_file_string):
            print("ERROR! no config file detected!")
            #log this
        else:
            config_file = open(DataManager.records_folder + DataManager.config_file_string, 'w')
            data = ""
            data += DataManager.salt()
            data += ""
            data += new_password_hash
            print("data we write to file: \n" + data)
            config_file.write(data)
            config_file.close()
            DataManager.load_config()
            DataManager.save_and_encrypt_volunteer_info(sm.get_key_from_password())
            DataManager.open_and_decrypt_volunteer_info(sm.get_key_from_password())

    @staticmethod
    def open_and_decrypt_volunteer_info(key):
        if DataManager.volunteer_info_manager is not None:
            DataManager.volunteer_info_manager.open_and_decrypt_volunteer_info(key)

    @staticmethod
    def save_and_encrypt_volunteer_info(key):
        if DataManager.volunteer_info_manager is not None:
            DataManager.volunteer_info_manager.save_and_encrypt_volunteer_info(key)

    @staticmethod
    def sum_hours_worked(start_date, end_date):
        return DataManager.volunteer_session_manager.sum_hours_worked(start_date, end_date)

    @staticmethod
    def sign_in_volunteer(volunteer):
        DataManager.volunteer_session_manager.sign_in_volunteer(volunteer)

    @staticmethod
    def sign_out_volunteer(volunteer):
        DataManager.volunteer_session_manager.sign_out_volunteer(volunteer)

    @staticmethod
    def update_sign_in_status():
        # potential bug here?
        DataManager.volunteer_session_manager.update_sign_in_status(DataManager.volunteers)

    @staticmethod
    def load_volunteer_sessions_file():
        # potential bug here?
        DataManager.volunteer_session_manager.load_volunteer_sessions()

    @staticmethod
    def delete_volunteer(volunteer, key):
        DataManager.volunteers.remove(volunteer)
        DataManager.save_and_encrypt_volunteer_info(key)

    def check_admin_password(self,attempt):
        return sm.hashed_input
DataManager()

''' 
    def __init__(self):

       if not os.path.exists(self.records_folder):
            os.makedirs(self.records_folder)
            # TODO add logging here
        # volunteer info
        ##################################
        if not os.path.exists(self.records_folder + self.volunteer_info_file_string):
            print("making file")
            # TODO add logging here
        volunteer_info_file = open(self.records_folder + self.volunteer_info_file_string, 'w')
        ##################################

        # volunteer hours
        ##################################
        if os.path.exists(self.records_folder + self.volunteer_hours_file_string):
            print("making file")
            # TODO add logging here
        volunteer_hours_file = open(self.records_folder + self.volunteer_hours_file_string, 'w')
        ##################################

        # config
        ##################################
        if not os.path.exists(self.records_folder + self.config_file_string):
            print("making file")
            # TODO add logging here
        config_file = open(self.records_folder + self.config_file_string, 'w')
        ##################################
'''



