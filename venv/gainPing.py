from os import system

def singleIp(ip):
    ipAddress = ip
    result = system("ping -n 3 " + ipAddress)
    counterFailed = ""
    counterSuccess = ""
    if (result == 1):
        counterFailed += ipAddress
    else:
        counterSuccess += ipAddress
    resultIp(counterFailed, counterSuccess)

def multiIp(ip,findChar):
    firstIp = ip[0:findChar]
    reza = firstIp.rfind(".")
    start = firstIp[reza + 1:]
    stop = ip[findChar + 1:]
    secondIp = firstIp[:reza+1] + stop
    start = int(start)
    stop = int(stop)
    counterFailed = ""
    counterSuccess = ""
    ipAddress = firstIp
    while start < stop + 1:
        ipAddress = firstIp[:reza + 1] + str(start)
        result = system("ping -n 3 " + ipAddress)
        start += 1
        if(result == 1):
            counterFailed += ipAddress
            counterFailed += " // "
        else:
            counterSuccess += ipAddress
            counterSuccess += " // "
    resultIp(counterFailed, counterSuccess)

def resultIp(counterFailed,counterSuccess):
    if counterFailed != "":
        print()
        print(counterFailed, " FAILED !!! ")
    elif counterSuccess != "":
        print()
        print(counterSuccess, "SUCCESS !!! ")
    else:
        print()
        print("Sorry something's wrong.Please try again!")
    repeat_program()

def repeat_program():
    again = input("Do you want to Continue(Y/N)? ")
    again = again.lower()
    if again == "y" or again == "yes":
        program()
    elif again == "n" or again == "no":
        exit()
    else:
        print("Please type yes or no !")
        repeat_program()

def program():
    ip = ""
    ip = input("please enter ip : ")  # ex = "72.9.147.145/146"
    ip = str(ip)
    checkIp(ip)
    findChar = ip.find("/")
    if findChar == -1:
        singleIp(ip)
    elif findChar != -1:
        multiIp(ip, findChar)
    else:
        print("Sorry something's wrong.Please try again!")

def checkIp(ip):
    dot = 0
    slash = 0
    for i in ip:
        if i == ".":
            dot += 1
        if i == "/":
            slash += 1
    dot1 = ip.find(".")
    dot2 = ip.find(".", dot1 + 1)
    dot3 = ip.find(".", dot2 + 1)
    num1 = ip[0:dot1]
    num2 = ip[dot1 + 1:dot2]
    num3 = ip[dot2 + 1:dot3]
    if ip.find("/") == -1:
        num4 = ip[dot3 + 1:]
    if ip.find("/") != -1:
        dot4 = ip.find("/")
        num4 = ip[dot3 + 1:dot4]
        num5 = ip[dot4 + 1:]

    if not(7<=len(ip)<=19): #check the number of characters
        print("IP is wrong.Please try again!")
        program()
    elif dot != 3: #check the number of dots
        print("IP is wrong.Please try again!")
        program()
    elif not(slash == 1 or slash == 0): #check the number of slash
        print("IP is wrong.Please try again!")
        program()
    elif num1.isdigit() == False or num2.isdigit() == False or num3.isdigit() == False or num4.isdigit() == False: #check the type of string
        print("IP is wrong.Please try again!")
        program()
    elif ip.find("/") != -1:
        if num5.isdigit() == False: #check the type of string
            print("IP is wrong.Please try again!")
            program()
    elif not(0<=int(num1)<=255) or not(0<=int(num2)<=255) or not(0<=int(num3)<=255) or not(0<=int(num4)<=255): #check the range of numbers
        print("IP is wrong.Please try again!")
        program()
    elif ip.find("/") != -1:
        if not(0<=int(num5)<=255): #check the range of numbers
            print("IP is wrong.Please try again!")
            program()
    else:
        print("It may take some time ...")

print("*** WELCOME TO PROGRAM ***")
print("You can gain ping from your IP.Just type IP and wait for results...")
print("Example for single IP : 1.1.1.1")
print("Example for multi IP : 1.1.1.1/3 => (1.1.1.1)(1.1.1.2)(1.1.1.3)")
print()
program() #startProgram

#Kasra Jannati
#www.designdrm.com
#(+98)9376320630
#kasrajannati@designdrm.com






