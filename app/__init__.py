'''
This file initializes your application and brings together all of the various
components.
'''

import os
import requests
import json

from flask import Flask, url_for, redirect, render_template, request, abort
from flask.ext import admin, login
from flask.ext.sqlalchemy import SQLAlchemy

from flask_debugtoolbar import DebugToolbarExtension

from werkzeug.contrib.fixers import ProxyFix
from werkzeug.routing import BaseConverter

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from .models import db, User, Company, Pair
from .views import AdminIndexView, CompanyView, TypeformView

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.wsgi_app = ProxyFix(app.wsgi_app)

db.app = app
db.init_app(app)


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


@app.route('/')
def index():
    entries = Company.query.\
                    with_entities(Company.name, Company.url, Company.logo).\
                    filter_by(status='accepted').\
                    order_by(Company.name).all()
    companies = [dict(name=row[0], url=row[1], logo=row[2]) for row in entries]

    return render_template('index.html', companies=companies)


@app.route('/about')
def about():
    return render_template('about.html')


# Google WebMaster Tools verification page
@app.route("/google25e87b64455912d9.html")
def site_verification():
    """Returns site verification content"""
    return app.send_static_file("site_verification.html")


# Robots file
@app.route("/robots.txt")
def robots_txt():
    return app.send_static_file("robots.txt")

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def not_authorized(e):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(410)
def gone(e):
    return render_template('410.html'), 410

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Admin', index_view=AdminIndexView(), base_template='layout.html')

# Add Companies view
admin.add_view(CompanyView(Company, db.session, name='Companies', endpoint="companies"))
admin.add_view(TypeformView(name='Get Typeform new entries', endpoint="data"))
