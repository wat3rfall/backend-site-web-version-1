# import smtplib

# server = smtplib.SMTP_SSL('smtp.live.com', 465)
# server.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
# server.starttls() #Puts connection to SMTP server in TLS mode
# server.ehlo()
# server.login("ceves.noreply@gmail.com", "Climat2020!b6f")
# server.sendmail(
#   "ceves.noreply@gmail.com", 
#   "laurencel2001@gmail.com", 
#   "this message is from python")
# server.quit()

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "ceves.noreply@gmail.com"
receiver_email = "laurencel2001@gmail.com"
password = "Climat2020!b6f"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "laurencel2001@gmail.com"  # Enter your address
# receiver_email = "laurencel2001@gmail.com"  # Enter receiver address
# password = "python27"
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)