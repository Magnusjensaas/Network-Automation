user_database = []

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def get_user(user_id):
        for user in user_database:
            if int(user.id) == int(user_id):
                return user
            return False

    @staticmethod
    def get_users():
        return  user_database

    def store_user(self):
        user_id = len(user_database) + 1
        self.id = user_id
        user_database.append(self)
        return True