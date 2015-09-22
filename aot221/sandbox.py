#Turing complete sandbox with the ability to handle any +-*/ computation
#Currently uses a .txt file to store usernames and hashed passwords so that only authorized users can access it
#Start with creating an account then log in and run your own computation or use the built-in fib() and powersTwo() functions

from passlib.hash import sha256_crypt
import re

with open('usernames.txt') as f:
    USERARR = f.readlines()
USERARR = map(lambda s: s.strip('\n'), USERARR)
#print USERARR
with open('passwords.txt') as f:
    PASSARR = f.readlines()
PASSARR = map(lambda t: t.strip('\n'), PASSARR)
#print PASSARR

def updateUserInfo():
#updates the username and password files holding your hash info
    with open('usernames.txt') as f:
        USERARR = f.readlines()
    USERARR = map(lambda s: s.strip('\n'), USERARR)
    #print USERARR
    with open('passwords.txt') as f:
        PASSARR = f.readlines()
    PASSARR = map(lambda t: t.strip('\n'), PASSARR)

def createAccount():
    #Registers an account into the username/password files
    print "creating account... \n"
    username = raw_input("Enter your username here: ")
    password = raw_input("Enter your password here: ")
    if username in USERARR:
        username = raw_input("Username already exists. Please enter another: ")
    u = open('usernames.txt','a')
    u.write(username)
    u.write("\n")
    hash = sha256_crypt.encrypt(password)
    p = open('passwords.txt','a')
    p.write(hash)
    p.write("\n")
    #print hash + "\n"
    updateUserInfo()

def checkPassword(password):
    print "checking password..."
    for h in PASSARR:
        if(sha256_crypt.verify(password,h)==True):
            print "found pass in file"
            return True
        else:
            print "did not find pass in file"

def login():
    loggedIn = False
    username = raw_input("Please enter in your username: ")
    password = raw_input("Please enter in your password: ")
    print "checking credentials... \n"
    if (username in USERARR and checkPassword(password)==True):
        loggedIn = True
        print "Welcome to the sandbox, " + username
    else:
        print "Please log in"
        sandbox()
    return loggedIn

def fib(fibNum):
    a,b = 1,1
    for i in range(fibNum-1):
        a,b = b,a+b
    print "Fibonacci of " + str(fibNum) + " is " + str(a)

def powersTwo(upperNum):
    #Calculates powers of two from 1 to upperNum
    for i in xrange(1, upperNum + 1):
        print i**2


def sandbox():
    userChoice = raw_input("0 to create an account | 1 to login \n")
    if (userChoice == '0'):
        createAccount()
        sandbox()
    elif(userChoice =='1'):
        pass
    else:
        print "Enter 0 or 1"
        sandbox()
    loggedIn = login()
    while (loggedIn == True):

        userRequest = raw_input("Type some code to run or '0' to quit: \n")
        try:
            if not(re.match("^[0-9]*$",userRequest ) or
                       re.match("fib",userRequest) or
                       re.match("powersTwo", userRequest) or
                       re.match("print", userRequest) or
                        re.match("+=-/"), userRequest):
                print "Illegal characters are in your code. This is strictly for computation and 'print' \n"
        except Exception:
            pass
        else:
            if (userRequest == "0"):
                break
            else:
                try:
                    #userRequest = 'print ' + userRequest
                    exec userRequest
                    #print "\n"
                except Exception:
                    pass

sandbox()

