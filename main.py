from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import psycopg2

@app.route('/')
def index():
    conn = psycopg2.connect("postgresql://postgres:root@localhost:5432/versions")
    cur = conn.cursor()
    cur.execute("SELECT applications FROM versions")
    applications = cur.fetchall()

    cur.execute("SELECT id, version FROM mdp WHERE applications = 'MDP'")
    mdp = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Hurtownia'")
    warehouse = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Kontrakty'")
    contracts = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'MZB'")
    mzb = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Cenniki' ")
    pricelist = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'eCRF'")
    ect = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Analizy'")
    analysis = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Poradnie'")
    clinic = cur.fetchall()

    cur.execute("SELECT id, version FROM versions WHERE applications = 'Magazyn'")
    storage = cur.fetchall()



app = Flask(__name__)

Bootstrap(app)

@app.route("/", methods=('GET','POST'))
def add_version():








if __name__ = "__main__":
    app.run()