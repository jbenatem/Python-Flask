from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from UsuarioController import crear_usuarios
#import data.mostrar_data as md

app = Flask(__name__)
app.secret_key = "3j3mp10"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return redirect(url_for("login"))

@app.route('/login', methods=["POST","GET"])
def login():
    #Creamos flag para determinar si se inicia sesión
    success_login = False
    if request.method == "POST":
        user = request.form["uname"]
        password = request.form["psw"]
        #Obtener listado de usuarios creados
        users = crear_usuarios()
        for x in users:
            if user == x.usuario and password == x.contraseña:
                success_login = True
                #Guardamos el usuario que inició sesión
                user_logged = x
                user_fullname = user_logged.get_nombres()
        #Configuramos la sesión
        session.permanent = True       
        #session["user"] = user_fullname
        #Verificamos si el login fue exitoso
        if success_login:
            #Guardar imagen de prueba
            #md.Guardar_Distribucion_Clases()
            session["user"] = user_fullname
            return redirect(url_for("user", usr = user))
        else:
            session["user"] = user
            return render_template('login.html')

    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template('login.html')

@app.route('/user', methods=["POST","GET"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template('user.html', user=user)
    else:
        flash("No has iniciado sesión")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)