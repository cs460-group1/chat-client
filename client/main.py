from client import ui


"""
Handles commands pushed from the server.
"""
class Handler:
    def receive_message(self, group, username, time, text):
        pass

def main():
    ui.run(Handler)
