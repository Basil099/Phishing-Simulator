import smtplib


def mail(from_addr, to_addrs, mssg):
    server = smtplib.SMTP("host231.checkdomain.de", 587)
    server.starttls()
    print("Started.........................")
    server.login("security@daten-analysieren.de", 'ubcene8w!Dv??')
    print("Login  success.........")
    server.sendmail(from_addr, to_addrs, mssg)
    print("Mail Sent success.........")
    server.quit()


from_addr = 'Christian.Kobler@Adweko.de'
to_addr = 'basilsattler@gmx.de'
from_name = 'Christian Kobler'
subject = "Discover India's Top 10 presentations templates"



#mail(from_addr, to_addr, message.encode())