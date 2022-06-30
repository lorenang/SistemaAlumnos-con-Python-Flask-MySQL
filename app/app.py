# Recordemos que un módulo es un archivo con extensión 'py' y contiene en su interior funciones, clases, definición
# de variables etc.

# Un paquete en Python agrupa un conjunto de módulos relacionados y se los localiza en un directorio.


# Crearemos un paquete llamado 'models' que contenga en su interior los módulos llamados 'Estudiante.py' y 'Conexion.py'.

# La aplicación principal llamarla 'app.py'

# Debemos crear una carpeta llamada 'models' y en su interior tres archivos: 'Estudiante.py', 'Conexion.py' y '__init__.py'.

# El archivo '__init__.py' generalmente se encuentra vacío y tiene por objetivo indicar al intérprete de Python que dicha carpeta es un paquete.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from Conexion import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                #login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña Incorrecta")
                return render_template('login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(host="127.0.0.1", port=5000, debug=True)