from user import User
#yeah... this isn't finished yet. 
#bcrypt hash passswords

users = [
    User(1, "BigHead", "password", "bighead","bighead@dwellingly.com", "false" ),
    User(2, "Default User", "userPassword", "defaultUser","user0@dwellingly.com", "false" ),
    User(2, "Default User1", "userPassword", "defaultUser1","user10@dwellingly.com", "false" )
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.uid: u for u in users}
useremail_mapping = {u.email: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password: #might need safe_str_cmp from workzeug.security
        return user

def identity(payload):
    user_id = payload['uid']
    return userid_mapping.get(user_id, None)