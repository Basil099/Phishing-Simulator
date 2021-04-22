import Mailer
import AddressManager
import MailCreator
import ServerInfo

import os


def scenario_spoof_mail():
    # This scenario shows how to send a spoof-mail, i.e. we create and send an email with a forged sender address

    # First, we specify sender the e-mail should show
    from_addr = "darth.vader@old-lords.com"
    from_name = "Darth Vader"

    # Here we specify the receiver, please change this as you would like to see the outcome
    to_addr = "info@daten-analysieren.de"

    # Then we specify our server information
    # With the server info comes the real sender, while the email will look like it is from darth vader,
    # it will actually be from the user specified in ServerInfo class.
    server_info = ServerInfo.ServerInfo()

    # Using the specified server information we create a session
    mailer = Mailer.Mailer(server_info)
    mailer.connect_to_server()
    mailer.login_to_server()

    # We use the mail_creator class to generate Vaders' message
    mail_creator = MailCreator.MailCreator(from_name, from_addr)
    vaders_message = mail_creator.create_mail_darthvader(to_addr)

    # And finally send it. After that we shutdown the mail server again.
    mailer.send_mail(vaders_message)
    mailer.shutdown_server()


def scenario_phishing_simulation():
    # This scenario shows how to run a phishing simulation, like commonly applied in course of security awareness
    # campaigns.

    # It starts again with defining sender and server information. In this scenario actual and apparent sender match.
    server_info = ServerInfo.ServerInfo()
    from_addr = server_info.username
    from_name = "Basil Sattler"


    # Using the specified server information we create a session
    mailer = Mailer.Mailer(server_info)
    mailer.connect_to_server()
    mailer.login_to_server()

    # We load the target adresses from the file stored in the data directory. Please note that the file should have
    # the format it has in the example file
    adress_manager = AddressManager.AdressManager("../data/examples.xls")

    # We instantiate an object of the MailCreator class
    mail_creator = MailCreator.MailCreator(from_name, from_addr)

    # Typically phishing mails point to some external resources where the actual phishing happens. Such a link can be
    # embedded into the mail while creation. This can be used, for example, to track whether the recipient has
    # clicked on the link.
    link = "https://daten-analysieren.de/"

    # We iterate over the adresses the adress_manager provides, create dynamically a e-mail and send it.
    for to_adr in adress_manager.get_adresses():
        bequest_message = mail_creator.create_html_mail_bequest(to_adr, link)
        mailer.send_mail(bequest_message)

    # And finally shut down the server.
    mailer.shutdown_server()


if __name__ == '__main__':
    print("First Scenario, sending a Spoof-Mail")
    scenario_spoof_mail()
    print("Second Scenario, performing a phishing simulation")
    scenario_phishing_simulation()
