import ssl
import smtplib


smtp = smtplib.SMTP("mail.python.org", port=587)

context = ssl.create_default_context()

smtp.starttls(context=context)
# (220, b'2.0.0 Ready to start TLS')
