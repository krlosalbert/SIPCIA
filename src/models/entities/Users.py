from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, UserName, UserLastName, UserAddres, UserPhone, UserEmail, UserIdCard, UserPassword, RolId) -> None:
        self.id       = id
        self.Name     = UserName
        self.LastName = UserLastName
        self.Addres   = UserAddres
        self.Phone    = UserPhone 
        self.Email    = UserEmail
        self.IdCard   = UserIdCard 
        self.password = UserPassword
        self.RolId    = RolId   

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def password_hashed(self, password):
        password_hashed = generate_password_hash(password)
        return password_hashed
        
#esto es para generar la clave encriptada
#print(generate_password_hash("1234"))