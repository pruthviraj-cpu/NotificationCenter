class user:
    def __init__(self,email,username,phone):
        self.n=username
        self.e=email
        self.p=phone
    
    def get_email(self):
        return self.e
    def get_phone(self):
        return self.p

class admin(user):
    def access_panel(self):
        print(f"{self.n} get logged in the admin panel")
class coustomer(user):
    def browse(self):
        print(f"{self.n} is browsing the offers")