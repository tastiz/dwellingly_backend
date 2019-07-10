class User:
    def __init__(self, id, name, password, username, email, archived):
        self.id = id  # TODO changed this from uid to get JWT working, may need to change it back later....
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.archived = archived
    
    def user_method(self):
        pass 
