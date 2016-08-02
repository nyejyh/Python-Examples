# Project 10: Jason Huang

import time
import smtplib
import sys

answer = raw_input("Please tell me one of your current life problems: ")
time.sleep(1)
print "I see.  Just so you know, Curtis is the source of the life problem you just told me."
time.sleep(1)
email = raw_input("I can offer to send Curtis at example2@gmail.com an email with your life complaint, please enter Yes or No. ")

if email == "Yes":
    print "Congratulations, your complaint has been sent."
    fromaddr = 'example@gmail.com' #this can use any gmail account, leaving it blank for now
    toaddrs = 'example2@gmail.com'
    msg = "\r\n".join([
            "From: example@gmail.com",
            "To: example2@gmail.com",
            "Subject: TROLL ME NOW",
            "",
            answer
            ])
    username = 'example@gmail.com' #this can use any gmail account, leaving it blank for now
    password = '????' #this is sensitive, have to go to my own account to activate it, deactivated for now.
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
else:
    print "I respect your decision, this program will now exit."
    sys.exit()
    