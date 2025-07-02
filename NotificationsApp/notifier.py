from interface import Notifier

class emailnotifier(Notifier):
    def send(self,message,user):
        print(f"📧 Email to {user.get_email()}:{message} ")
class SMSnotifier(Notifier):
    def send(self,message,user):
        print(f"📱 SMS to {user.get_phone()}: {message} ")
class pushnotifier(Notifier):
    def send(self,message,user):
        print(f"🔔 Push notification: {message} ")
        