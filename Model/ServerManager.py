
import http.client
import os
######################
# this class talks to the server to update key information
######################
from datetime import datetime


class ServerManager:

    server_domain = ""
    server_port = 0
    file_end = ".csv"



    @staticmethod
    def POST_file(records_folder, file_name_stub):
        date_string = datetime.now().strftime("_%Y_%m_%d")
        file_name = file_name_stub + date_string + ServerManager.file_end
        if file_name == None:
            print("Error: File name not specified")
            return None
        body_content = "Content-Disposition: form-data; name=\"filename\"; filename=\"" + file_name + "\"\r\n\r\n"
        print(ServerManager.server_domain + ":" + ServerManager.server_port)
        with open(records_folder + file_name, 'rt') as file:
            for line in file:
                body_content += line
        print("making the connection:")
        connection = http.client.HTTPConnection(ServerManager.server_domain, ServerManager.server_port)
        connection.request('POST', '/upload', body_content)

