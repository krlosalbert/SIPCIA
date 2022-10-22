from werkzeug.security import check_password_hash, generate_password_hash
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

    @classmethod
    def check_password(self, hashed_password, UserPassword):
        return check_password_hash(hashed_password, UserPassword)

number = "hospital2022"
#esto es para generar la clave encriptada
#print(generate_password_hash("1234"))