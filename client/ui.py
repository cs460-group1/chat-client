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
    default_address = "0.0.0.0"
    default_port = 6543

    def __init__(self, window, handler):
        self.window = window
        self.handler = handler
        self.frame = None
        self.proxy = None
        self.username = StringVar()
        self.password = StringVar()

        window.protocol("WM_DELETE_WINDOW", self.close)
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

        self.window.title("Connect to server")
        self.frame = Frame(self.window)
        self.frame.grid(sticky=N+S+E+W, padx=10, pady=10)

        Label(self.frame, text="Connect to a server", style="Title.TLabel").grid(columnspan=2, padx=10, pady=10)

        Label(self.frame, text="Address").grid(row=1, column=0, sticky=E)
        self.address_entry = Entry(self.frame)
        self.address_entry.insert(END, LoginWindow.default_address)
        self.address_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(self.frame, text="Port").grid(row=2, column=0, sticky=E)
        self.port_entry = Entry(self.frame)
        self.port_entry.insert(END, str(LoginWindow.default_port))
        self.port_entry.grid(row=2, column=1, padx=10, pady=10)

        button_frame = Frame(self.frame)
        button_frame.grid(row=3, column=0, columnspan=2)
        Button(button_frame, text="Connect", command=self.on_connect).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Close", command=self.close).grid(row=0, column=1, padx=10, pady=10)

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

        Label(self.frame, text="Log in", style="Title.TLabel").grid(columnspan=2, padx=10, pady=10)

        Label(self.frame, text="Username").grid(row=1, column=0, sticky=E)
        self.username_entry = Entry(self.frame, textvariable=self.username)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(self.frame, text="Password").grid(row=2, column=0, sticky=E)
        self.password_entry = Entry(self.frame, textvariable=self.password, show="•")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        button_frame = Frame(self.frame)
        button_frame.grid(row=3, column=0, columnspan=2)
        Button(button_frame, text="Login", command=self.on_login).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Sign Up", command=self.show_register).grid(row=0, column=1, padx=10, pady=10)

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
        name = Label(self.frame, text="Username")
        name.grid(row=0, sticky=E)
        self.username_entry = Entry(self.frame, textvariable=self.username)
        self.username_entry.grid(row=0,column=1, padx=10, pady=10)
        # Have user enter password
        password = Label(self.frame, text="Password")
        password.grid(row=1, sticky=E)
        self.password_entry = Entry(self.frame, textvariable=self.password, show="•")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        # Have user retype Password
        repassword = Label(self.frame, text="Retype password")
        repassword.grid(row=2, sticky=E)
        self.repassword_entry = Entry(self.frame, show="•")
        self.repassword_entry.grid(row=2, column=1, padx=10, pady=10)
        # Have user enter first name
        firstname = Label(self.frame, text="First name")
        firstname.grid(row=3, sticky=E)
        self.first_name_entry = Entry(self.frame)
        self.first_name_entry.grid(row=3, column=1, padx=10, pady=10)
        # Have user enter last name
        lastname = Label(self.frame, text="Last name")
        lastname.grid(row=4, sticky=E)
        self.last_name_entry = Entry(self.frame)
        self.last_name_entry.grid(row=4, column=1, padx=10, pady=10)
        # Have user enter email
        email = Label(self.frame, text="Email address")
        email.grid(row=5, sticky=E)
        self.email_entry = Entry(self.frame)
        self.email_entry.grid(row=5, column=1, padx=10, pady=10)
        # Have user enter address
        address = Label(self.frame, text="Street address")
        address.grid(row=6, sticky=E)
        self.address_entry = Entry(self.frame)
        self.address_entry.grid(row=6, column=1, padx=10, pady=10)

        # Submit register information button that will send information to server
        button_frame = Frame(self.frame)
        button_frame.grid(row=7, column=0, columnspan=2)
        Button(button_frame, text="Sign Up", command=self.on_register).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Cancel", command=self.show_login).grid(row=0, column=1, padx=10, pady=10)

    def on_connect(self):
        address = self.address_entry.get()
        port = int(self.port_entry.get())

        try:
            self.proxy = rpc.connect(address, port, self.handler)
            self.show_login()
        except Exception as e:
            messagebox.showerror("", "Could not connect to server.\n\nError: " + str(e))
            self.window.wait_window()

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            token = self.proxy.login(username=username, password=password)

            # Open the chat window
            self.frame.destroy()
            ChatWindow(self.window, self.proxy, token)
        except rpc.RpcException as e:
            messagebox.showerror("", "Log in failed.\n\nError: " + str(e))
            self.window.wait_window()

    def on_register(self):
        if self.repassword_entry.get() != self.password_entry.get():
            messagebox.showerror("", "Password must match in both entries")
            self.window.wait_window()
            return

        try:
            self.proxy.create_user(
                username = self.username_entry.get(),
                password = self.password_entry.get(),
                first_name = self.first_name_entry.get(),
                last_name = self.last_name_entry.get(),
                email = self.email_entry.get(),
                address = self.address_entry.get()
            )
            messagebox.showinfo("", "Account created successfully!")
            self.window.wait_window()
            # Go back to login
            self.show_login()
        except rpc.RpcException as e:
            messagebox.showerror("", "Registration failed.\n\nError: " + str(e))
            self.window.wait_window()

    def center(self):
        self.window.update_idletasks()
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        size = tuple(int(_) for _ in self.window.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.window.geometry("+%d+%d" % (x, y))

    def close(self):
        if self.proxy:
            self.proxy.close()
        self.window.destroy()


class ChatWindow:
    def __init__(self, window, proxy, token):
        self.window = window
        self.proxy = proxy
        self.token = token

        window.protocol("WM_DELETE_WINDOW", self.close)
        window.minsize(width=200, height=200)
        window.geometry("800x600")
        window.resizable(width=TRUE, height=TRUE)
        window.title("Instant Messenger")

        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=0)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=0)

        self.group_frame = Frame(window)
        self.group_frame.grid(row=0, column=0, sticky=N+S+E+W, padx=10, pady=10)
        self.message_frame = Frame(window)
        self.message_frame.grid(row=0, column=1, sticky=N+S+E+W, pady=10)
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
        self.chat_entry.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W, pady=5, ipady=5)
        self.chat_entry.focus_set()

    def send_message(self, event):
        print("Message to send:", self.chat_entry.get())
        self.chat_entry.delete(0, END)

    def close(self):
        self.proxy.logout(token=self.token)
        self.proxy.close()
        self.window.destroy()


def run(handler):
    # Set up root window.
    root = Tk()

    # Make tkinter less ugly.
    style = Style()
    style.theme_use("clam")
    style.configure("Title.TLabel", font=("Helvetica", 16))

    # Show window.
    window = LoginWindow(root, handler)
    window.center()
    root.mainloop()
