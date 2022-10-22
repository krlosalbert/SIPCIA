from .entities.Users import User

class ModelUser():

    @classmethod # esto es para usar la funcion sin instanciar la clase ModelUser
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT UserId, UserName, UserLastName, UserAddres, UserPhone, UserEmail, UserIdCard, UserPassword, RoleId 
                    FROM tbluser WHERE UserIdCard={}""".format(user.IdCard)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], User.check_password(row[7], user.password), row[8])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod # esto es para usar la funcion sin instanciar la clase ModelUser
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT UserId, UserName FROM tbluser WHERE UserId={} ".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                return User(row[0],row[1],None,None,None,None,None,None,None)
              
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod # esto es para usar la funcion sin instanciar la clase ModelUser
    def Users(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT u.UserId, u.UserName, u.UserLastName, u.UserAddres, u.UserPhone, u.UserEmail, u.UserIdCard, r.RoleDescription FROM tbluser u INNER JOIN tblrole r ON u.RoleId=r.RoleId"
            cursor.execute(sql)
            user_list = cursor.fetchall()
            return user_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod # esto es para usar la funcion sin instanciar la clase ModelUser
    def InsertUsers(self, db, user):
        try:
            con = db.connection
            cursor = con.cursor()
            sql = """INSERT INTO tbluser (UserName, UserLastName, UserAddres, UserPhone, UserEmail, UserIdCard, UserPassword, RoleId) 
                    VALUES("{}", "{}", "{}", {}, "{}", {}, "{}", {})""".format(user.Name, user.LastName, user.Addres, user.Phone, user.Email, user.IdCard, user.password, user.RolId)
            cursor.execute(sql)
            result = con.commit()
            
            return result
        except Exception as ex:
            raise Exception(ex)