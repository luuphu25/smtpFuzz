import smtplib
import time 
import sys

def send_email(sender, receiver, date, line):
     
    From = sender
    To = receiver
    #Date = time.ctime(time.time())
    Date = date
    Subject = "Hello"
    Body =   date 
    mMessage = ("From: %s\nTo: %s\nDate:%s \nSubject:  %s\nBody: %s\n" % (From, To, Date, Subject, Body))

    #print('Connect to Server .. ')
    smtp_server = "192.168.185.128"
    port = 587
    password = "123456"

    server = smtplib.SMTP(smtp_server, port)
    server.login(From, password)
    server.sendmail(From, To, mMessage.encode("utf8"))
    print("\n Sent!" )
    server.quit()

From = "attacker@offsec.local"
To = "admin@offsec.local"
i = 0
payload_file = sys.argv[1]

with open(payload_file) as file: 
    for payload in file: 
        i += 1
        send_email(From, To, payload, str(i))





