# Phishing-Simulator

## Description: 
this lean project is designed for performing phishing simulations, for example in the context of IT security awareness campaigns. 


## Usage:
the project includes four classes that provide the functionality to perform a phishing simulation:
* AdressManager: this class is responsible for reading and providing email addresses. Also a random split into 
two subgroups is performed which can be accessed. This is helpful if subgroups of the target group should be adressed
by different fake phishing mails. Please note that the data should be stored in an excel-file with a specific format.

* Mailcreator: this class is responsible for creating fake phishing mails to be supplied to the target group. We provide
two templates in HTML-format which might be used. Typically phishing mails point to some external resources. In the provided 
templates such a link is embedded within the message, while the link is determined by an argument to the respective functions. 
In case other mail-content is desired obviously this class can be extended.

* Mailer: this class handles the SMTP client session, i.e. we can connect and log-in to an e-mail server and send
mails to the target groups.

* ServerInfo: this class merely holds the serverinformation.

## Test:

Please refer to the Test to get familiar on how to use the functionality. There are two scenarios implemented.
The first one shows how to send a Spoof-mail, i.e. we create and send an email with a forged sender address. The second
scenario shows how to send fake phishing-mails to multiple targets at once. Please note that access to an e-mail server is required.

## License: 

This project is open source. However, using it in in a commercial context requires permission of the author Basil Sattler. Please contact via the following E-Mail adress:
basil.sattler@daten-analysieren.de
