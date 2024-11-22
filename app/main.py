from routes.Home_Routes import home_bp
from routes.Collaborators_Routes import collaborators_bp
from routes.appLogin import login_bp
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(collaborators_bp, url_prefix='/collaborators')
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
