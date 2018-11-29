""""This file will contain all the models """
import datetime


class User():
    """User Model: it describes the behaviours and properties of a user"""

    def __init__(self, userid, first_name, last_name, other_names, phonenumber,
                 email, username, password, isAdmin=False, registeredOn=datetime.datetime.now()):
        self.userid = userid
        self.first_name = first_name
        self.last_name = last_name
        self.other_names = other_names
        self.phonenumber = phonenumber
        self.username = username
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.registeredOn = registeredOn

    def __str__(self):
        return '{} {} {}'.format(self.userid, self.username, self.isAdmin)


incidents = []

class IncidentModel():
    def __init__(self):
        self.db = incidents

    def save(self,incidentType,comment,location,createdBy,images,videos,status="draft"):
        data = {
            "incidentId": len(self.db) + 1,
            "createdOn": datetime.datetime.now(),
            "createdBy":createdBy,
            "incidentType":incidentType,
            "location": location,
            "status": status,
            "comment": comment,
            "images" : images,
            "videos": videos
        }   
        self.db.append(data)
        return data