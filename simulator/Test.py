from simulator import Mailer, AddressManager, ContentSupplier

import os

host = os.environ.get('HOST')
port = os.environ.get('PORT')
from_addr = os.environ.get('FROM_ADRESS')
from_name = os.environ.get('FROM_NAME')
username = os.environ.get('USER_NAME')
pw = os.environ.get('PASSWORD')
subject = os.environ.get('SUBJECT')
path = os.environ.get('PATH')

adress_manager = AddressManager.AdressManager(
    path + "/data/examples.xls",
    from_addr,
    from_name,
    username)

mailer = Mailer.Mailer(host, port, username, pw)
mailer.connect_to_server()
mailer.login_to_server()
dict_adresses_links = {}

for i in range(0, len(adress_manager.get_adresses())):
    dict_adresses_links[adress_manager.get_adresses()[i]] = adress_manager.get_links()[i]

for to_adr, link_id in dict_adresses_links.items():
    example_message = ContentSupplier.create_html_mail_bequest(from_name,
                                                               from_addr,
                                                               to_adr,
                                                               subject,
                                                               link_id)
    mailer.send_single_mail(to_adr, example_message)

mailer.shutdown_server()
