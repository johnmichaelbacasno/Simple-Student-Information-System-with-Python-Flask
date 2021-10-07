from flask import Flask

from .views.dashboard import dashboard
from .views.students import students
from .views.courses import courses
from .views.colleges import colleges

from extensions import *

def create_app():

    app = Flask(__name__)

    # Initialize config
    app.config.from_object('config.DevelopmentConfig')

    # Initialize extensions
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        # Register blueprints
        app.register_blueprint(dashboard)
        app.register_blueprint(students)
        app.register_blueprint(courses)
        app.register_blueprint(colleges)
    
    return app
