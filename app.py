from flask import Flask
from flask import redirect, render_template, request, make_response
from flask_bootstrap import Bootstrap
from os import getenv, path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


def create_app():
    basedir = path.abspath(path.dirname(__file__))
    env_dir = path.join(basedir, '.env')
    load_dotenv(env_dir)

    c_app = Flask(__name__, '/static')
    c_app.secret_key = getenv('SECRET_KEY')
    c_app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    c_db = SQLAlchemy(c_app)
    c_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    Bootstrap(c_app)

    return c_app, c_db


app, db = create_app()


@app.route('/')
def welcome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
