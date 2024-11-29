from routes.Home_Routes import home_bp
from routes.Collaborators_Routes import collaborators_bp
from routes.Login import login_bp
from routes.Profile import account_bp
from routes.Mentors_Routes import mentors_bp
from flask import Flask,session, redirect, url_for

 
app = Flask(__name__)

app.config['SECRET_KEY'] = '456ytu@w789'


# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(collaborators_bp, url_prefix='/collaborators')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(account_bp, url_prefix='/account')
app.register_blueprint(mentors_bp,url_prefix ='/mentors')
 
#la ruta /logout debe estar fuera de cualquier Blueprint para que sea accesible globalmente.

@app.route('/logout')

def logout():

    session.clear()  # Elimina todas las variables de la sesión

    return redirect(url_for('home.home'))  # Redirige a la página de inicio

if __name__ == '__main__':

    app.run(debug=True)

   
