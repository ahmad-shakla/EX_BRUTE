import os
os.system("clear")
print("███████╗██╗░░██╗░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗ Created")
print("██╔════╝╚██╗██╔╝░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝ By")
print("█████╗░░░╚███╔╝░█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░ Ahmad")
print("██╔══╝░░░██╔██╗░╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░ Shakla")
print("███████╗██╔╝╚██╗░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗ ")
print("╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝\n\n\n")
print("By using this tools you agree that you'r using it for leagel purpses\n\n")
print("0.Exit")
print("1.Gmail                 6.Yahoo               11.Zoho")
print("2.Hotmail               7.Mail                12.GMX") 
print("3.Office365             8.Outlook             13.Wannado-UK")
print("4.Comcast               9.Orange              14.AOL")
print("5.02                   10.Verizon             15.Yahoo-mail-plus\n\n")


user = input ("EX-BRUTE >")
x = 4
while x != 5 :

    if user == "1":
        import gmail

    elif user == "2":
        import hotmail

    elif user == "3":
        import office365

    elif user == "4":
        import comcast

    elif user == "5":
        import o2

    elif user == "6":
        import yahoo

    elif user == "7":
        import mail

    elif user == "8":
        import outlook

    elif user == "9":
        import orange

    elif user == "10":
        import verizon

    elif user == "11":
        import zoho
     
    elif user == "12":
        import gmx

    elif user == "13":
        import wanadoouk
  
    elif user == "14":
        import aol

    elif user == "15":
         import yahoomailplus

    elif user == "0":
         print ("Thnaks for using the script")


    else :
        x = 5
        print ("incorrect command\n")
        user = input ("EX-BRUTE >")
        x = 4
