
class Volunteer:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.pin_hash = None
        self.phone = None
        self.address = None
        self.work_area = None
        self.signed_in = False

    '''def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = None
        self.pin_hash = None
        self.phone = None
        self.address = None
        self.work_area = None
    '''

    @classmethod
    def volunteer_from_params(cls, first_name, last_name, email, pin_hash, phone, address, work_area):
        volunteer = cls()
        volunteer.first_name = first_name
        volunteer.last_name = last_name
        volunteer.email = email
        volunteer.pin_hash = pin_hash
        volunteer.phone = phone
        volunteer.address = address
        volunteer.work_area = work_area
        return volunteer




