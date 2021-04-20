import smtplib
import traceback


class Mailer:

    def __init__(self, host=None, port=None, username=None, pw=None):
        self.host = host
        self.port = port
        self.username = username
        self.pw = pw
        self.server = smtplib.SMTP(self.host, self.port)

    def connect_to_server(self):
        try:
            self.server.starttls()
            print("Successfully connected to Server " + self.host)
        except Exception as e:
            print("Connection to server failed")
            traceback.print_exc()

    def login_to_server(self):
        try:
            self.server.login(self.username, self.pw)
            print("Successfull Log-in of user: " + self.username)
        except Exception as e:
            print("Log-in failed")
            traceback.print_exc()

    def shutdown_server(self):
        try:
            self.server.quit()
            print("Successfull shutdown of server")
        except Exception as e:
            print("shutdown failed")
            traceback.print_exc()

    def send_single_mail(self, to_addrs, mssg):
        try:
            self.server.send_message(mssg)
            print("Success: Mail sent to " + to_addrs)
            return 1
        except Exception as e:
            print("Failure: Mail not sent")
            traceback.print_exc()
            return 0

    def send_multiple_mails(self, adresses, mssg):
        counter = 0
        for to_addrs in adresses:
            print(to_addrs)
            counter += self.send_single_mail(to_addrs, mssg)
        print(str(counter) + " of " + str(len(adresses)) + " where sent successfully")
