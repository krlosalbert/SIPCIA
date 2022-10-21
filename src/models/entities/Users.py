from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, UserName, UserLastName, UserAddres, UserPhone, UserEmail, UserIdCard, UserPassword, RolId) -> None:
        self.id           = id
        self.UserName     = UserName
        self.UserLastName = UserLastName
        self.UserAddres   = UserAddres
        self.UserPhone    = UserPhone 
        self.UserEmail    = UserEmail
        self.UserIdCard   = UserIdCard 
        self.UserPassword = UserPassword
        self.RolId        = RolId   