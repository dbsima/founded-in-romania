'''
This file initializes your application and brings together all of the various
components.
'''

import os, requests, json

from flask import Flask, url_for, redirect, render_template, request
from flask.ext import admin, login
from flask.ext.sqlalchemy import SQLAlchemy

from flask_debugtoolbar import DebugToolbarExtension

from werkzeug.contrib.fixers import ProxyFix

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSON

from .models import db, User, Company
from .views import AdminIndexView, CompanyView

"""
If we set instance_relative_config=True when we create our app with the Flask()
call, app.config.from_pyfile() will load the specified file from the
instance/config.py
"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

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


# Flask views
@app.route('/')
def index():
    entries = Company.query.\
                    with_entities(Company.name, Company.url, Company.logo).\
                    filter_by(status='accepted').\
                    order_by(Company.name).all()
    companies = [dict(name=row[0], url=row[1], logo=row[2]) for row in entries]
    print entries
    return render_template('index.html', companies=companies)

@app.route('/about')
def about():
    return render_template('about.html')

def has_key(d, key):
    if key not in d:
        return None
    return d[key]

@app.route("/data", methods=['GET'])
def get_companies():
    
    no_of_companies = db.session.query(func.count('*')).select_from(Company).scalar() 
    print no_of_companies
    
    payload = {'key': '1912f415723a26ff57f90be983cd38facfc9ca85',
               'completed': 'true',
              'offset' : no_of_companies + 1}
    r = requests.get('https://api.typeform.com/v0/form/HHO2Uc', params=payload)
    json_data = json.loads(r.text)
    questions = json_data['questions']
        
    responses = json_data['responses']
    
    import datetime
    
    for response in responses:
        date_land = response['metadata']['date_land']
        date_submit = datetime.datetime.strptime(date_land, "%Y-%m-%d %H:%M:%S")
        
        # get company details
        name = has_key(response['answers'], 'textfield_1466918')
        
        bitly_url = ''
        founders = ''
        description = ''
        
        url = has_key(response['answers'], 'website_1466924')
        logo_submited = has_key(response['answers'], 'website_1466929')
        founded_year = has_key(response['answers'], 'number_1668017')
        twitter = has_key(response['answers'], 'textfield_1668035')
        contact_name = has_key(response['answers'], 'textfield_1466921')
        contact_email = has_key(response['answers'], 'email_1466925')
        
        # create a new Company entry in the database
        company = Company(name=name,
                           url=url,
                           logo_submited=logo_submited,
                           logo="",
                           contact_email=contact_email,
                           contact_name = contact_name,
                           twitter = twitter,
                           founded_year = founded_year,
                           date_submit = date_submit,
                           status="pending")
        # Add company to database
        db.session.add(company)

    db.session.commit()
    
    return json.dumps(responses)



# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Admin', index_view=AdminIndexView(), base_template='layout.html')

# Add view
admin.add_view(CompanyView(Company, db.session, name='Companies', url='/companies'))
