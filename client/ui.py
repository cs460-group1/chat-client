# Interface for registration
# Written by: Amber Thatcher, Stephen Coakley, Nyia Lor, and Jaiden Trinh
# Written for: Instant messenger project
# Created on: 4/10/2016
from client import rpc
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import queue



# Set up a global incoming message queue.
message_queue = queue.Queue()


"""
Handles commands pushed from the server.
"""
class Handler(rpc.Handler):
    """
    Puts an incoming message into the message queue.
    """
    def receive_message(self, **kwargs):
        message_queue.put(kwargs)


"""
The main connection and login window.

Window shown before launching the main chat window. Handles connecting to the
server, logging in, and registration.
"""
class LoginWindow:
    default_address = "0.0.0.0"
    default_port = 6543

    def __init__(self, window):
        self.window = window
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
            self.proxy = rpc.connect(address, port, Handler)
            self.show_login()
        except Exception as e:
            messagebox.showerror("", "Could not connect to server.\n\nError: " + str(e))

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

    def on_register(self):
        if self.repassword_entry.get() != self.password_entry.get():
            messagebox.showerror("", "Password must match in both entries")
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
            # Go back to login
            self.show_login()
        except rpc.RpcException as e:
            messagebox.showerror("", "Registration failed.\n\nError: " + str(e))

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


"""
Main application window.
"""
class ChatWindow:
    def __init__(self, window, proxy, token):
        self.window = window
        self.proxy = proxy
        self.token = token
        self.dest_username = None
        self.dest_group = None

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
        Label(self.group_frame, text="Groups").grid(pady=(0,10))
        self.group_frame.rowconfigure(1, weight=1)
        self.group_list = None
        Button(self.group_frame, text="Add user", command=self.on_add_group_user).grid(row=2)
        Button(self.group_frame, text="Remove user", command=self.on_remove_group_user).grid(row=3)
        Button(self.group_frame, text="New group", command=self.on_create_group).grid(row=4)

        # Friends frame.
        Label(self.friends_frame, text="Friends").grid(pady=(0,10))
        self.friends_frame.rowconfigure(1, weight=1)
        self.friends_list = None
        Button(self.friends_frame, text="Add friend", command=self.on_add_friend).grid(row=2)

        # Set up the chat log frame.
        self.message_frame.rowconfigure(1, weight=1)
        self.message_frame.columnconfigure(0, weight=1)
        self.message_title = Label(self.message_frame)
        self.message_title.grid(row=0, column=0, columnspan=2, pady=(0,10), sticky=N+S+E+W)
        self.message_list = Listbox(self.message_frame)
        self.message_list.grid(row=1, column=0, sticky=N+S+E+W)
        self.message_scrollbar = Scrollbar(self.message_frame)
        self.message_scrollbar.grid(row=1, column=1, sticky=N+S+E+W)
        self.message_scrollbar.config(command=self.message_list.yview)
        self.message_list.config(yscrollcommand=self.message_scrollbar.set)

        # Set up the message input.
        self.chat_entry = Entry(self.message_frame)
        self.chat_entry.bind("<Return>", self.on_send_message)
        self.chat_entry.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W, pady=(5, 0), ipady=5)
        self.chat_entry.focus_set()

        # Show remote data.
        self.refresh_groups_list()
        self.refresh_friends_list()

        # Schedule the incoming message callback.
        self.window.after(100, self.check_message_queue)

    """
    Refreshes the list of groups from the server.
    """
    def refresh_groups_list(self):
        groups = self.proxy.get_groups(token=self.token)

        if self.group_list:
            self.group_list.destroy()

        self.group_list = Frame(self.group_frame)
        for i, id in enumerate(groups):
            group = self.proxy.get_group(token=self.token, id=id)
            label = Button(self.group_list, text=group["name"], command=lambda g=id: self.choose_group(g))
            label.grid(row=i, sticky=E+W)
        self.group_list.grid(row=1, sticky=N+E+W)

    """
    Refreshes the list of friends from the server.
    """
    def refresh_friends_list(self):
        friends = self.proxy.get_friends(token=self.token)

        if self.friends_list:
            self.friends_list.destroy()

        self.friends_list = Frame(self.friends_frame)
        for i, username in enumerate(friends):
            label = Button(self.friends_list, text=username, command=lambda u=username: self.choose_user(u))
            label.grid(row=i, sticky=E+W)
        self.friends_list.grid(row=1, sticky=N+E+W)

    """
    Displays the existing messages for the current room.
    """
    def refresh_message_list(self):
        # Remove messages already in the pane.
        self.message_list.delete(0, END)

        # If we are talking to a user,
        if self.dest_username:
            messages = self.proxy.get_messages_with_user(token=self.token, username=self.dest_username)
        # If we are in a group
        elif self.dest_group:
            messages = self.proxy.get_messages_in_group(token=self.token, group=self.dest_group)
        else:
            return

        for message in messages:
            self.display_message(message)

    """
    Sets the message destination to a user.
    """
    def choose_user(self, username):
        self.dest_group = None
        self.dest_username = username
        self.message_title.config(text="User: " + username)
        self.refresh_message_list()

    """
    Sets the message destination to a group.
    """
    def choose_group(self, group_id):
        self.dest_username = None
        self.dest_group = group_id
        group = self.proxy.get_group(token=self.token, id=group_id)

        self.message_title.config(text="Group: " + group["name"])
        self.refresh_message_list()

    """
    Displays a message in the chat history.
    """
    def display_message(self, message):
        self.message_list.insert(END, message["sender"] + ": " + message["text"])

    """
    Shows a dialog for adding a user to a group.
    """
    def on_add_group_user(self):
        if self.dest_group:
            username = PromptWindow.prompt(self.window, "Type in a username")
            self.proxy.add_group_user(token=self.token, group=self.dest_group, username=username)
            self.refresh_groups_list()
            self.choose_group(self.dest_group)

    """
    Shows a dialog for removing a user from a group.
    """
    def on_remove_group_user(self):
        if self.dest_group:
            username = PromptWindow.prompt(self.window, "Type in a username")
            self.proxy.remove_group_user(token=self.token, group=self.dest_group, username=username)
            self.refresh_groups_list()
            self.choose_group(self.dest_group)

    """
    Shows a dialog for creating a group.
    """
    def on_create_group(self):
        group_id = self.proxy.create_group(token=self.token)
        self.refresh_groups_list()
        self.choose_group(group_id)

    """
    Shows a dialog for adding a friend.
    """
    def on_add_friend(self):
        username = PromptWindow.prompt(self.window, "Type in a username")
        self.proxy.add_friend(token=self.token, username=username)
        self.refresh_friends_list()

    """
    Handles the event for sending a message.
    """
    def on_send_message(self, event):
        text = self.chat_entry.get()

        # Slash commands are evaluated as Python code...
        if text[0] == "/":
            exec(text[1:])
        # If we are talking to a user,
        elif self.dest_username:
            self.proxy.send_message(
                token=self.token,
                receiver={
                    "type": "user",
                    "username": self.dest_username,
                },
                text=text
            )
        # If we are in a group
        elif self.dest_group:
            self.proxy.send_message(
                token=self.token,
                receiver={
                    "type": "group",
                    "id": self.dest_group,
                },
                text=text
            )

        # Clear the message entry.
        self.chat_entry.delete(0, END)

    """
    Callback that runs periodically to display incoming messages in real-time.
    """
    def check_message_queue(self):
        while True:
            try:
                message = message_queue.get(False)
                self.display_message(message)
            except queue.Empty:
                break

        # Schedule again.
        self.window.after(100, self.check_message_queue)

    def close(self):
        try:
            self.proxy.logout(token=self.token)
            self.proxy.close()
        finally:
            self.window.destroy()


"""
Convenience class for creating "prompt" dialog boxes.
"""
class PromptWindow:
    def prompt(root, title):
        window = PromptWindow(root, title)
        root.wait_window(window.window)
        return window.result

    def __init__(self, root, title):
        self.window = Toplevel(root)
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.title(title)

        self.label = Label(self.window, text=title)
        self.label.grid(padx=10, pady=10)
        self.entry = Entry(self.window)
        self.entry.bind("<Return>", lambda e: self.submit())
        self.entry.grid(row=1, padx=10)
        self.entry.focus_set()
        self.button = Button(self.window, text="OK", command=self.submit)
        self.button.grid(row=2, padx=10, pady=10)

    def submit(self):
        self.result = self.entry.get()
        self.window.destroy()


def run():
    # Set up root window.
    root = Tk()

    # Make tkinter less ugly.
    style = Style()
    style.theme_use("clam")
    style.configure("Title.TLabel", font=("Helvetica", 16))

    # Show window.
    window = LoginWindow(root)
    window.center()
    root.mainloop()
