import smtplib
import time as t
import sys 
print('''░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░          ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒       ░░     ░     ░░   ░
░ ░         ░        ░  ░   ░        ░ ░        ░     ░  ░   ░
░                         ░                    ░
''')

heart = '♥️'

print("Annoying gmail shell"+heart+"", file=sys.stderr)

def INFO(MESSAGE, CARRIER_MESSAGE, NUMBER,email_login,email_password):
    to_number = NUMBER+CARRIER_MESSAGE
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()           
    server.login(email_login, email_password)
    print ('==================================')
    send(server, email_login,to_number,MESSAGE)

def send(server, email_login,to_number,MESSAGE):
    while True:
        try:
            server.sendmail(email_login, to_number, MESSAGE)
            print ('[+]'' The message was sent successfully ')
        except KeyboardInterrupt:
            print ('\n==================================\n')
            print ('[!] '' Exiting')
            exit()

def main():
    try:
        
        t.sleep(1)
        email_login = input('[~]'' Log in to your email address : ')
        t.sleep(.5)
        email_password = input('[~]'' Password your email : ')
        t.sleep(.5)
        NUMBER = input('[~]'' Send spam messages to Emil : ')
        t.sleep(.5)
        print ('\n ''''
        Chose a type of transmitter 
        att,tmobile,verizon,sprint''' )
        CARRIER = input('[~]'' Enter a type : ')
        t.sleep(.5)
        MESSAGE = input('[~]'' Write a message to him : ')
        if CARRIER == 'att':
            CARRIER_MESSAGE = '@mms.att.net'
        if CARRIER == 'tmobile':
            CARRIER_MESSAGE = '@tmomail.net'
        if CARRIER == 'verizon':
            CARRIER_MESSAGE = '@vtext.com'
        if CARRIER == 'sprint':
            CARRIER_MESSAGE = '@messaging.sprintpcs.com'
        INFO(MESSAGE,CARRIER_MESSAGE,NUMBER,email_login,email_password)
    except smtplib.SMTPAuthenticationError:
        print (  '[!] ''There is an error in the account information, verify with your password')
    except KeyboardInterrupt:
        print ('\n')
        exit()

main()
