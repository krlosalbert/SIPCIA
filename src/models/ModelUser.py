from .entities.Users import User

class ModelUser():

    @classmethod # esto es para usar la funcion sin instanciar la clase ModelUser
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT UserId, UserName, UserLastName, UserAddres, UserPhone, UserEmail, UserIdCard, UserPassword, RolId 
                    FROM tbluser WHERE UserIdCard={} AND UserPassword={}""".format(user.UserIdCard, user.UserPassword)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
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