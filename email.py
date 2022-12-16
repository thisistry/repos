import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'me@gmail.com'
msg['To'] = 'you@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('me@gmail.com', 'mypassword')

mailserver.sendmail('me@gmail.com','you@gmail.com',msg.as_string())

mailserver.quit()




#######################################################################
import smtplib

SERVER = "localhost"

FROM = "sender@example.com"
TO = ["user@example.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()


##############################################################################
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "sender@email"
receiver_email = "receiver@email"
password = "<your password here>"
message = """ Subject: Hi there

This message is sent from Python."""


# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
server = smtplib.SMTP(smtp_server,port)

try:
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

    
    
    toaddr = 'buffy@sunnydale.k12.ca.us'
cc = ['alexander@sunydale.k12.ca.us','willow@sunnydale.k12.ca.us']
bcc = ['chairman@slayerscouncil.uk']
fromaddr = 'giles@sunnydale.k12.ca.us'
message_subject = "disturbance in sector 7"
message_text = "Three are dead in an attack in the sewers below sector 7."
message = "From: %s\r\n" % fromaddr
        + "To: %s\r\n" % toaddr
        + "CC: %s\r\n" % ",".join(cc)
        + "Subject: %s\r\n" % message_subject
        + "\r\n" 
        + message_text
toaddrs = [toaddr] + cc + bcc
server = smtplib.SMTP('smtp.sunnydale.k12.ca.us')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, message)
server.quit()




import smtplib
from email.mime.multipart import MIMEMultipart

me = "user63503@gmail.com"
to = "someone@gmail.com"
cc = "anotherperson@gmail.com,someone@yahoo.com"
bcc = "bccperson1@gmail.com,bccperson2@yahoo.com"

rcpt = cc.split(",") + bcc.split(",") + [to]
msg = MIMEMultipart('alternative')
msg['Subject'] = "my subject"
msg['To'] = to
msg['Cc'] = cc
msg.attach(my_msg_body)
server = smtplib.SMTP("localhost") # or your smtp server
server.sendmail(me, rcpt, msg.as_string())
server.quit()
