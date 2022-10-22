'''
    importo el framework flask que me ayudara a trabajar en el aplicativo,
    junto me traigo las clases tambien.

    *lineas de codigo para instalar el flask*
    pip install flask

    *linea de codigo para instalar mysql*
    pip install Flask-MySQLdb
'''

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

from routes import *

#importo la clase de configuracion creada
from config import config

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.Users import User

#instancio la clase flask
app = Flask(__name__)

#declaro variable para llamar al metodo MySQL pasandole el parametro de app el cual contiene la clase instanciada de flask
db = MySQL(app)

#declaro variable para llamar al metodo login manager pasandole el parametro app con la clase instanciada de flask
login_manager_app=LoginManager(app)

#declaro funcion para logear el usuario
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

#creo ruta principal utilizando el decorador @ que me redirige al login
#defino una funcion para redireccionar la pagina a esa ruta establecida
@app.route('/')
def index():
    return render_template("login.html")
    
#creo ruta principal utilizando el decorador @ y le asigno los metodos a recibir porque por defecto recibe metodo GET
@app.route('/login', methods = ["GET", "POST"])
def login():
    logged_user = None
    if request.method == 'POST':
        user = User(None, None, None, None, None, None, request.form['user'], request.form['password'], None)
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta, Intentelo de nuevo") 
                return render_template("login.html")  
        else:
            flash("El usuario ingresado no fue encontrado....") 
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route('/users')
def users():
    users_list = ModelUser.Users(db)
    return render_template("users.html", users=users_list)

#creo ruta de cerrar sesion
@app.route('/logout')
def logout():
    logout_user()
    return render_template("login.html")

#creo nueva utilizando el decorador @
@app.route('/home')
@login_required
def home():
    return render_template("home.html")
    
#funcion para redirigir al login si el usuario intenta ingresar una url y no se encuentra logeado
def status_401(error):
    return redirect(url_for('login'))

#funcion para motrar mensajes si el usuario intenta ingresar a una url no definida
def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404

#validacion para ejecutar el servidor y que este en constante movimiento
if __name__ == '__main__':
    app.config.from_object(config['development']) #utilizo la configuracion del diccionario config en su llave development
    app.register_error_handler(401, status_401) #utilizo metodo para utilizar la funcion del error 401
    app.register_error_handler(404, status_404) #utilizo metodo para utilizar la funcion del error 401
    app.run()