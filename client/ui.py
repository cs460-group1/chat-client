# Interface for registration
# Written by: Amber Thatcher, Stephen Coakley, Nyia Lor, and Jaiden Trinh
# Written for: Instant messenger project
# Created on: 4/10/2016
from client import rpc
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


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
        window.resizable(width=FALSE, height=FALSE)
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        self.show_connect()

    """
    Shows the server connection form.
    """
    def show_connect(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Connect")
        self.frame = Frame(self.window)
        self.frame.grid(sticky=N+S+E+W, padx=10, pady=10)

        Label(self.frame, text="Address").grid(row=0, column=0)
        self.address_entry = Entry(self.frame)
        self.address_entry.grid(row=0, column=1)

        Label(self.frame, text="Port").grid(row=1, column=0)
        self.port_entry = Entry(self.frame)
        self.port_entry.grid(row=1, column=1)

        Button(self.frame, text="Connect", command=self.on_connect).grid(row=2, column=0)
        Button(self.frame, text="Close", command=self.close).grid(row=2, column=1)

        # Keyboard navigation.
        self.address_entry.focus_set()
        self.address_entry.bind("<Return>", lambda e: self.port_entry.focus_set())
        self.port_entry.bind("<Return>", lambda e: self.on_connect())

    """
    Shows the login form.
    """
    def show_login(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Login")
        self.frame = Frame(self.window)
        self.frame.grid(sticky=N+S+E+W, padx=10, pady=10)

        Label(self.frame, text="Username").grid(row=0, column=1)
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=0, column=2)

        Label(self.frame, text="Password").grid(row=1, column=1)
        self.password_entry = Entry(self.frame)
        self.password_entry.grid(row=1, column=2)

        Button(self.frame, text="Login", command=self.on_login).grid(row=2, column=1)
        Button(self.frame, text="Sign Up", command=self.show_register).grid(row=2, column=2)

        # Keyboard navigation.
        self.username_entry.focus_set()
        self.username_entry.bind("<Return>", lambda e: self.password_entry.focus_set())
        self.password_entry.bind("<Return>", lambda e: self.on_login())

    """
    Shows the registration form.
    """
    def show_register(self):
        if self.frame:
            self.frame.destroy()

        self.window.title("Register")
        self.frame = Frame(self.window)
        self.frame.grid(sticky=N+S+E+W, padx=10, pady=10)

        # Have user create username
        name = Label(self.frame, text="Username:")
        name.grid(row=0)
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=0,column=1)
        # Have user enter password
        password = Label(self.frame, text="Password:")
        password.grid(row=1)
        self.password_entry = Entry(self.frame)
        self.password_entry.grid(row=1,column=1)
        # Have user retype Password
        repassword = Label(self.frame, text="Retype Password:")
        repassword.grid(row=2)
        self.repassword_entry = Entry(self.frame)
        self.repassword_entry.grid(row=2,column=1)
        # Have user enter first name
        firstname = Label(self.frame, text="First name:")
        firstname.grid(row=3)
        self.first_name_entry = Entry(self.frame)
        self.first_name_entry.grid(row=3,column=1)
        # Have user enter last name
        lastname = Label(self.frame, text="Last name:")
        lastname.grid(row=4)
        self.last_name_entry = Entry(self.frame)
        self.last_name_entry.grid(row=4,column=1)
        # Have user enter email
        email = Label(self.frame, text="Email:")
        email.grid(row=5)
        self.email_entry = Entry(self.frame)
        self.email_entry.grid(row=5,column=1)
        # Have user enter address
        address = Label(self.frame, text="Address:")
        address.grid(row=6)
        self.address_entry = Entry(self.frame)
        self.address_entry.grid(row=6,column=1)

        # Submit register information button that will send information to server
        submit = Button(self.frame, text="Submit",command = self.on_register)
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
        messagebox.showinfo("Login", "Logged in successfully!")

        # Open the chat window
        self.frame.destroy()
        ChatWindow(self.window, self.proxy)

    def on_register(self):
        self.proxy.create_user(
            username = self.username_entry.get(),
            password = self.password_entry.get(),
            first_name = self.first_name_entry.get(),
            last_name = self.last_name_entry.get(),
            email = self.email_entry.get(),
            address = self.address_entry.get()
        )
        messagebox.showinfo("Register", "Account created successfully!")
        # Go back to login
        self.show_login()

    def close(self):
        if self.proxy:
            self.proxy.close()
        self.window.destroy()


class ChatWindow:
    def __init__(self, window, proxy):
        self.window = window
        self.proxy = proxy

        window.protocol("WM_DELETE_WINDOW", self.close)
        window.geometry("800x600")
        window.resizable(width=TRUE, height=TRUE)
        window.title("Instant Messenger")

        window.rowconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)

        self.group_frame = Frame(window)
        self.group_frame.grid(row=0, column=0, sticky=N+S+E+W, padx=10, pady=10)
        self.message_frame = Frame(window)
        self.message_frame.grid(row=0, column=1, sticky=N+S+E+W)
        self.friends_frame = Frame(window)
        self.friends_frame.grid(row=0, column=2, sticky=N+S+E+W, padx=10, pady=10)

        # Groups frame.
        Label(self.group_frame, text="Groups").pack()

        # Friends frame.
        Label(self.friends_frame, text="Friends").pack()

        # Set up the chat log frame.
        self.message_frame.rowconfigure(0, weight=1)
        self.message_frame.columnconfigure(0, weight=1)
        self.message_history = Text(self.message_frame)
        self.message_history.grid(row=0, column=0, sticky=N+S+E+W)
        self.message_scrollbar = Scrollbar(self.message_frame)
        self.message_scrollbar.grid(row=0, column=1, sticky=N+S+E+W)
        self.message_scrollbar.config(command=self.message_history.yview)
        self.message_history.config(yscrollcommand=self.message_scrollbar.set)

        # Set up the message input.
        self.chat_entry = Entry(self.message_frame)
        self.chat_entry.bind("<Return>", self.send_message)
        self.chat_entry.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W, padx=5, pady=5, ipadx=5, ipady=5)
        self.chat_entry.focus_set()

    def send_message(self, event):
        print("Message to send:", self.chat_entry.get())
        self.chat_entry.delete(0, END)

    def close(self):
        self.proxy.close()
        self.window.destroy()


def run(handler):
    # Set up root window.
    root = Tk()

    # Make tkinter less ugly.
    Style().theme_use("clam")

    # Show window.
    LoginWindow(root, handler)
    root.mainloop()
