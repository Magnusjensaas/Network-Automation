import model
from controller import SimpleController

class UserView:
    def __init__(self):
        self.controller = SimpleController(self)

    def update_display(self, state, msg):
        if isinstance(msg, model.User):
            msg = f"{msg.username};{msg.email}"
        print(f"{'Success' if state else 'Error'}>>>{msg}")

    def create_user(self):
        username = input("username: ")
        email = input("email: ")
        self.controller.create(username, email)

    def get_user(self):
        user_id = input("user id: ")
        self.controller.get(user_id)
