#Interface for registration
#Written by: Amber Thatcher, Stephen Coakley, Nyia Lor, and Jaiden Trinh
#Written for: Instant messenger project
#Created on: 4/10/2016
from tkinter import*
from socket import*
#import smtplib for sending function
import smtplib
#import email modules
from email.mime.text import MIMEText

#Function to display home window
def Home():
    root = Tk()
    root.title("Group 1's Instant Messenger")
    root.minsize(width=200,height=40)
    register = Button(root,text="Register",command=Register)
    register.grid(row=0,column=1)
    login = Button(root,text="Login",command=Login)
    login.grid(row=0,column=2)
    stop = Button(root,text="Exit",command=Exit)
    stop.grid(row=0,column=3)
    

#Function for display register window
def Register():
    root.withdraw()
    global new
    new = Tk()
    new.title("Register")
    #Have user create username
    name = Label(new,text="Username:")
    name.grid(row=0)
    nameEntry = Entry(new)
    nameEntry.grid(row=0,column=1)
    #Have user enter password
    password = Label(new,text="Password:")
    password.grid(row=1)
    passwordEntry = Entry(new)
    passwordEntry.grid(row=1,column=1)
    #Have user retype Password
    repassword = Label(new,text="Retype Password:")
    repassword.grid(row=2)
    repasswordEntry = Entry(new)
    repasswordEntry.grid(row=2,column=1)
    #Have user enter first name
    firstname = Label(new,text="First name:")
    firstname.grid(row=3)
    firstnameEntry = Entry(new)
    firstnameEntry.grid(row=3,column=1)
    #Have user enter last name
    lastname = Label(new,text="Last name:")
    lastname.grid(row=4)
    lastnameEntry = Entry(new)
    lastnameEntry.grid(row=4,column=1)
    #Have user enter email
    email = Label(new,text="Email:")
    email.grid(row=5)
    emailEntry = Entry(new)
    emailEntry.grid(row=5,column=1)

    #Submit register information button that will send information to server
    submit = Button(new,text="Submit",command = sendInfo)
    submit.grid(row=6,column=1)

#Function to send information to server
def sendInfo():
    #Server connection
    serverName = "173.0.255.207"
    serverPort = 12009
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    #Send information for registration validation
    clientSocket.send(nameEntry.encode())
    clientSocket.send(passwordEntry.encode())
    clientSocket.send(repasswordEntry.encode())
    clientSocket.send(firstnameEntry.encode())
    clientSocket.send(lastnameEntry.encode())
    clientSocket.send(emailEntry.encode())
    #Wait for response from server
    incoming = clientSocket.recv(1024)
    print(incoming.decode('ascii'))
    connectionSocket.close()

#Function for display login window
def Login():
    root.withdraw()
    global login
    login = Tk()
    login.title("Login")
    #Enter username
    name = Label(login,text="Username:")
    name.grid(row=0)
    nameEntry = Entry(login)
    nameEntry.grid(row=0,column=1)
    #Enter password
    password = Label(login,text="Password:")
    password.grid(row=1)
    passwordEntry = Entry(login)
    passwordEntry.grid(row=1,column=1)
    #Login button
    submit = Button(login,text="Login",command = sendLogin)
    submit.grid(row=5,column=0)
    #Forgot password button
    forgot = Button(login,text="Forgot password?",command = forgotPassword)
    forgot.grid(row=5,column=1)

#Function to send login information to server
def sendLogin():
    #Server connection
    serverName = "173.0.255.207"
    serverPort = 12009
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    #Send information for registration validation
    clientSocket.send(nameEntry.encode())
    clientSocket.send(passwordEntry.encode())
    #Wait for response from server
    incoming = clientSocket.recv(1024)
    print(incoming.decode('ascii'))
    connectionSocket.close()
    
#Function to exit program
def Exit():
    root.destroy()

#Function for forgotten password
def forgotPassword():
    with open("password.txt") as fp:
        #Create a message
        msg = MIMEText(fp.read())

        #Send message via our server
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

        #Function to recover password
        global passwordRecover
        passwordRecover = Tk()
        passwordRecover.title("Retrieve forgotten password")
        passwordSent = Label(passwordRecover,text="Password has been sent to your email")
        passwordSent.grid(row=0)

        #Button to go back to home page
        home = Button(passwordRecover,text="Home",command = Home)
        home.grid(row=1)

root = Tk()
root.title("Group 1's Instant Messenger")
root.minsize(width=200,height=40)
register = Button(root,text="Register",command=Register)
register.grid(row=0,column=1)
login = Button(root,text="Login",command=Login)
login.grid(row=0,column=2)
stop = Button(root,text="Exit",command=Exit)
stop.grid(row=0,column=3)
    



root.mainloop()



    
