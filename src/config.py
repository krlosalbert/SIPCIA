""" 
    En este archivo de configuracion voy a crear una clase que se llame configuracion de desarrollo
"""
class Config:
    #llave privada la cual me permite para mandar mensajes a traves de flask
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*s^'

class DevelopmentConfig(Config):
    DEBUG = True  #inicia nuestro servidor en modo de depuracion

    #configuracion para la conexion a la base de datos
    MYSQL_HOST     = 'localhost'
    MYSQL_USER     = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB       = 'dbsipcia'

#diccionario con la clase creada arriba
config={
    'development':DevelopmentConfig
}