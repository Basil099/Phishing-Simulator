from email.message import EmailMessage


class MailCreator:

    def __init__(self, from_name, from_addr):
        self.from_name = from_name
        self.from_addr = from_addr

    def create_html_mail_survey(self, to_addr, link):
        msg = EmailMessage()
        msg.set_content(f"""\
        <html>
        <head></head>
        <body>
            <p>Liebe Mitarbeiter der ADWEKO,</p>
    
            <p>wir freuen uns, dass unser Partner, das Marktforschungsunternehmen daten-analysieren.de, gerade eine Studie 
            mit dem Thema “Branche im Wandel – Auswirkungen der Corona-Pandemie auf   
            eine Industrie” durchführt. </p>
    
            <p>Das Ausfüllen der Umfrage dauert nur 5 Minuten. Durch die Teilnahme erhält die ADWEKO Consulting exklusive 
            Einblicke in die Studienergebnisse, von denen wir alle profitieren. Als Teilnehmer erhaltet ihr die Chance 
            einen Amazon-Gutschein im Wert von 100€ zu gewinnen. </p>
    
            <p>Es ist sehr wichtig, dass möglichst alle teilnehmen. Bitte folgt dem Link zur Umfrage: </p>
    
            <p>
                 <a href=""" + link + """>LINK ZUR TEILNAHME</a>
            </p>
            <p>Umfrageschluss ist der 31.01.2021</p>
    
            <p>Danke und viele Grüße </p>
            <p>Christian Kobler </p>
    
        </body>
        </html>
        """, subtype='html')
        msg['Subject'] = "Umfrage - eine Branche im Wandel"
        msg['From'] = self.from_name + '<' + self.from_addr + '>'
        msg['To'] = to_addr
        return msg

    def create_html_mail_bequest(self, to_addr, link):
        msg = EmailMessage()
        msg.set_content(f"""\
        <html>
        <head></head>
        <body>
        <p>Hallo,</p>
        <p>
          ich bestätige hiermit den Erhalt ihrer Informationen. Ich habe die
          Kontodaten aktualisiert und Sie als offensichtlichen Erben eingetragen.
          Indes sind hier die Informationen der Security-Firma der Bank, die für
          alle Transaktionen von herrenlosen Kontakten zuständig ist.
        </p>
        <a href=""" + link + """>JETZT KONTAKTIEREN!</a>
        <p>
          Ich würde Sie bitten, die Security-Firma (Trans Alliance Group) zu
          kontaktieren und ihnen die unten angehängten Informationen zuzuschicken.
          Leiten Sie deren Antwort an mich weiter. Schicken Sie den unten
          angehängten Brief an den angegebenen Absender.
        </p>
        <p>
          Kontaktperson: <br /><br />Mr. Robert Gill<br />
          Operation Manager / Int ‘L Transfer & Remittance Depart.<br />
          Trans Alliance Financial & Security Firm<br />
          Amsterdam, Netherlands.<br />
          Tel: + 31-644 540 367<br />
          E-Mail: trans_alliancesecurity@msn.com
        </p>
        <p>
          Ich kontaktiere Sie als Erbe des kürzlich verstorbenen Ingenieurs Erich
          Anorld, wegen des Fonds in Höhe von 7,467,000.00 Euro, der sich unter den
          Kontodaten NL85-ABNA-60.83.41.843 bei Ihrer Bank ABN AMRO N.V. befindet.
          Informieren Sie mich bitte sofort, wenn Sie noch zusätzliche Informationen
          benötigen, um den Fond auf mein Bankkonto zu transferieren. Ich erwarte
          Ihre Antwort so bald wie irgend möglich.
        </p>
        <p>
          Mit freundlichen Grüße<br />Anmerkung: Hier ist meine Telefonnummer +31 61
          76 71 725. Rufen Sie mich an, sobald Sie diesen Brief erhalten haben, um
          die Transaktion so schnell, wie möglich über die Bühne zu bringen. Möge
          Gott ihren Haushalt segnen, gerade jetzt im Moment, da wir die
          Auferstehung unseres Herrn Jesus Christus feiern.
        </p>
        </body>
        </html>
        """, subtype='html')
        msg['Subject'] = "Ihr Erbe"
        msg['From'] = self.from_name + '<' + self.from_addr + '>'
        msg['To'] = to_addr
        return msg

    def create_mail_darthvader(self, to_addr):
        msg = EmailMessage()
        msg.set_content(f"""\
        <html>
        <head></head>
        <body>
        <p>Hi,</p>
        <p>
          I am your Father!
        </p>
        </body>
        </html>
        """, subtype='html')
        msg['Subject'] = "Please join the dark side"
        msg['From'] = self.from_name + '<' + self.from_addr + '>'
        msg['To'] = to_addr
        return msg
