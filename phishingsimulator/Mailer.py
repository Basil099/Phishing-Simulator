import smtplib
import traceback


class Mailer:

    def __init__(self, serverinfo):
        self.host = serverinfo.host
        self.port = serverinfo.port
        self.username = serverinfo.username
        self.pw = serverinfo.pw
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

    def send_mail(self, message):
        try:
            self.server.send_message(message)
            print("Success: Mail sent")
            return 1
        except Exception as e:
            print("Failure: Mail not sent")
            traceback.print_exc()
            return 0