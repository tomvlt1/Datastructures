from flask import Flask
from routes.home_routes import home_bp
from routes.filter_output import filter_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(filter_bp)

if __name__ == '__main__':
    app.run(debug=True)
    


