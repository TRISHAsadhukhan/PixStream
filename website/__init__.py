
from flask import Flask , render_template , redirect , request , url_for
from .routes.auth import auth
from .routes.views import views



def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'pixStreamByTrishh'
    
    app.register_blueprint(auth , url_prefix="/auth/")
    app.register_blueprint(views)

    
    return app