"""
This is where you define the models of your application. This may be split into
several modules in the same way as views.py.
"""

from flask.ext.admin.actions import action
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
        User database model
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
 
    def is_authenticated(self):
        """Flask-Login integration"""
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        """
            Required for administrative interface
        """
        return self.username


class Company(db.Model):
    """
        Company database model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    twitter = db.Column(db.String(64))
    founded_year = db.Column(db.Integer)
    founders = db.Column(db.String(180))
    url = db.Column(db.Text)
    bitly_url = db.Column(db.String(180))
    logo_submited = db.Column(db.Text)
    logo = db.Column(db.String(180))
    contact_email = db.Column(db.String(120))
    contact_name = db.Column(db.String(120))
    date_submit = db.Column(db.DateTime)
    status = db.Column(db.String(64))

    def __unicode__(self):
        """
            Required for administrative interface
        """
        return self.name

    
class Pair(db.Model):
    """
        Key-Value pairs database model
    """
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True)
    val = db.Column(db.Integer)

    def __unicode__(self):
        """
            Required for administrative interface
        """
        return self.key