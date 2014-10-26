"""
This is where you define the models of your application. This may be split into
several modules in the same way as views.py.
"""

from flask.ext.admin.actions import action
from flask.ext.sqlalchemy import SQLAlchemy

import requests, json
from flask import current_app

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

    
def has_key(d, key):
    if key not in d:
        return None
    return d[key]

class TypeformAPI:
    def __init__(self):
        self.fields = {}
            
            
    def get_data(self):
        last_date = Pair.query.with_entities(Pair.val).filter_by(key='since').one()
        since = last_date[0]

        typeform_url = 'https://api.typeform.com/v0/form/' + current_app.config['TYPEFORM_FORM_UID']
        payload = {
            'key': current_app.config['TYPEFORM_API_KEY'],
            'completed': 'true',
            'since' : since
        }

        r = requests.get(typeform_url, params=payload)
        json_data = json.loads(r.text)
        self.questions = json_data['questions']
        self.responses = json_data['responses']
            
    def set_fields(self):
        for question in self.questions:
            if question['question'] == 'Startup name':
                self.fields['name'] = question['id']
            elif question['question'] == 'Year founded':
                self.fields['year'] = question['id']
            elif question['question'] == 'Web address':
                self.fields['web_address'] = question['id']
            elif question['question'] == 'Twitter handle':
                self.fields['twitter'] = question['id']
            elif question['question'] == 'URL to high-resolution (white) logo':
                self.fields['url_logo'] = question['id']
            elif question['question'] == 'Contact person':
                self.fields['contact_name'] = question['id']
            elif question['question'] == 'Contact email address':
                self.fields['contact_email'] = question['id']
        
    def update_db(self):
        if len(self.responses) == 0: return
        
        import datetime
        from datetime import timedelta
        import time

        for response in self.responses:
            date_land = response['metadata']['date_land']
            date_submit = datetime.datetime.strptime(date_land, "%Y-%m-%d %H:%M:%S")

            #print response
            # get company details
            name = has_key(response['answers'], self.fields['name'])
            url = has_key(response['answers'], self.fields['web_address'])
            url_to_logo = has_key(response['answers'], self.fields['url_logo'])
            founded_year = has_key(response['answers'], self.fields['year'])
            twitter = has_key(response['answers'], self.fields['twitter'])
            contact_name = has_key(response['answers'], self.fields['contact_name'])
            contact_email = has_key(response['answers'], self.fields['contact_email'])

            bitly_url = ''
            founders = ''
            description = ''

            status = "pending"

            # create a new Company entry in the database
            company = Company(name=name,
                               url=url,
                               logo_submited=url_to_logo,
                               contact_email=contact_email,
                               contact_name = contact_name,
                               twitter = twitter,
                               founded_year = founded_year,
                               date_submit = date_submit,
                               status=status)
            # Add company to database
            db.session.add(company)

        # know there is another last date
        since = time.mktime((date_submit + timedelta(hours=2)).timetuple())
        last_date = Pair.query.with_entities(Pair.val).filter_by(key='since').update({'val': since})

        db.session.commit()