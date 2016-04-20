#Interface for registration
#Written by: Amber Thatcher, Stephen Coakley, Nyia Lor, and Jaiden Trinh
#Written for: Instant messenger project
#Created on: 4/10/2016
from client import rpc
import tkinter as tk


"""
The main connection and login window.

Window shown before launching the main chat window. Handles connecting to the
server, logging in, and registration.
"""
class LoginWindow:
    def __init__(self, window, handler):
        self.window = window
        self.handler = handler
        self.frame = None
        self.proxy = None

        window.protocol("WM_DELETE_WINDOW", self.close)
        window.minsize(width=200, height=300)
        self.show_connect()

    """
    Shows the server connection form.
    """
    def show_connect(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Connect")
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        tk.Label(self.frame, text="Address").grid(row=0, column=0)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Port").grid(row=1, column=0)
        self.port_entry = tk.Entry(self.frame)
        self.port_entry.grid(row=1, column=1)

        tk.Button(self.frame, text="Connect", command=self.on_connect).grid(row=2, column=0)
        tk.Button(self.frame, text="Close", command=self.close).grid(row=2, column=1)

    """
    Shows the login form.
    """
    def show_login(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Login")
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        tk.Label(self.frame, text="Username").grid(row=0, column=1)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=2)

        tk.Label(self.frame, text="Password").grid(row=1, column=1)
        self.password_entry = tk.Entry(self.frame)
        self.password_entry.grid(row=1, column=2)

        tk.Button(self.frame, text="Login", command=self.on_login).grid(row=2, column=1)
        tk.Button(self.frame, text="Sign Up", command=self.show_register).grid(row=2, column=2)

    """
    Shows the registration form.
    """
    def show_register(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Register")
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        #Have user create username
        name = tk.Label(self.frame, text="Username:")
        name.grid(row=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0,column=1)
        #Have user enter password
        password = tk.Label(self.frame, text="Password:")
        password.grid(row=1)
        self.password_entry = tk.Entry(self.frame)
        self.password_entry.grid(row=1,column=1)
        #Have user retype Password
        repassword = tk.Label(self.frame, text="Retype Password:")
        repassword.grid(row=2)
        self.repassword_entry = tk.Entry(self.frame)
        self.repassword_entry.grid(row=2,column=1)
        #Have user enter first name
        firstname = tk.Label(self.frame, text="First name:")
        firstname.grid(row=3)
        self.first_name_entry = tk.Entry(self.frame)
        self.first_name_entry.grid(row=3,column=1)
        #Have user enter last name
        lastname = tk.Label(self.frame, text="Last name:")
        lastname.grid(row=4)
        self.last_name_entry = tk.Entry(self.frame)
        self.last_name_entry.grid(row=4,column=1)
        #Have user enter email
        email = tk.Label(self.frame, text="Email:")
        email.grid(row=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=5,column=1)

        #Submit register information button that will send information to server
        submit = tk.Button(self.frame, text="Submit",command = self.on_register)
        submit.grid(row=6,column=1)

    def on_connect(self):
        address = self.address_entry.get()
        port = int(self.port_entry.get())
        self.proxy = rpc.connect(address, port, self.handler)

        self.show_login()

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.token = self.proxy.login(username=username, password=password)
        print(self.token)

    def on_register(self):
        self.proxy.create_user(
            username = self.username_entry.get(),
            password = self.password_entry.get(),
            first_name = self.first_name_entry.get(),
            last_name = self.last_name_entry.get(),
            email = self.email_entry.get(),
            address = self.address_entry.get()
        )

    def close(self):
        if self.proxy:
            self.proxy.close()
        self.window.destroy()


def run(handler):
    root = tk.Tk()
    LoginWindow(root, handler)
    root.mainloop()
