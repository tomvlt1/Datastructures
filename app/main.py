from app.routes.home_routes import home_bp
from app.routes.filter_output import collaborators_bp
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(collaborators_bp, url_prefix='/collaborators')

if __name__ == '__main__':
    app.run(debug=True)

    


