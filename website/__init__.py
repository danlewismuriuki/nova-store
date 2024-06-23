from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DB_NAME = 'database.sqlite3'

def create_database():
    db.create_all()
    print('Database Created')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KJHGWSnbvbno9878ikhgfedf'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/')


    return app
