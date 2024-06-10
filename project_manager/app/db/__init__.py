import click
import mysql.connector
import os

from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
def get_db():
    if "db" not in g or not g.db.is_connected():
        g.db = mysql.connector.connect(
            host=current_app.config["DB_HOST"],
            user=current_app.config["DB_USERNAME"],
            password=current_app.config["DB_PASSWORD"],
            database=current_app.config["DB_DATABASE"],

            )
        pass

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        # close the database 
        pass

def init_app(app):
    app.teardown_appcontext(close_db)