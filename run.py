import os
from flask import Flask, url_for, redirect, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from wtforms import form, fields, validators
from flask.ext import admin, login
from flask.ext.admin.contrib import sqla
from flask.ext.admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Markup
import requests, json
# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_fir_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Create user model.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    
# Create Company model.
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # about the company
    name = db.Column(db.String(80))
    url = db.Column(db.String(180))
    twitter = db.Column(db.String(64))
    founded_year = db.Column(db.Integer)
    # logo
    logo_submited = db.Column(db.String(180))
    logo_accepted = db.Column(db.String(180))
    # contact
    contact_email = db.Column(db.String(120))
    contact_name = db.Column(db.String(120))
    # administrative stuff
    date_submit = db.Column(db.DateTime)
    date_accept = db.Column(db.DateTime)
    status = db.Column(db.String(64))

    # Required for administrative interface
    def __unicode__(self):
        return self.name


# Create customized model view class
class UserView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class CompanyView(sqla.ModelView):
    #form_excluded_columns = ['path_to_logo', 'contact_name', 'twitter', 'founded_year', 'date_submit', ]
    
    def is_accessible(self):
        return login.current_user.is_authenticated()
    
    def _link_logo(view, context, model, name):
        if not model.logo_submited:
            return ''

        return Markup('<a href="'+model.logo_submited+'" target="_blank">URL</a>')
    
    def _link_url(view, context, model, name):
        if not model.url:
            return ''

        return Markup('<a href="http://'+model.url+'" target="_blank">'+model.url+'</a>')
    
    def _link_twitter(view, context, model, name):
        if not model.url:
            return ''

        return Markup('<a href="https://twitter.com/'+model.twitter+'" target="_blank">'+model.twitter+'</a>')

    column_formatters = {
        'logo_submited': _link_logo,
        'url': _link_url,
        'twitter': _link_twitter
    }



# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        #self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')

def has_key(d, key):
    if key not in d:
        return ''
    return d[key]

@app.route("/data", methods=['GET'])
def get_users():
    payload = {'key': '1912f415723a26ff57f90be983cd38facfc9ca85',
               'completed': 'true',
              'offset' : '1'}
    r = requests.get('https://api.typeform.com/v0/form/HHO2Uc', params=payload)
    json_data = json.loads(r.text)
    questions = json_data['questions']
    
    for question in questions:
        print question
        
    responses = json_data['responses']
    
    import datetime
    
    for response in responses:
        date_land = response['metadata']['date_land']
        date_submit = datetime.datetime.strptime(date_land, "%Y-%m-%d %H:%M:%S")
        
        name = has_key(response['answers'], 'textfield_1466918')
        url = has_key(response['answers'], 'website_1466924')
        logo_submited = has_key(response['answers'], 'website_1466929')
        year = has_key(response['answers'], 'number_1668017')
        twitter = has_key(response['answers'], 'textfield_1668035')
        contact_name = has_key(response['answers'], 'textfield_1466921')
        contact_email = has_key(response['answers'], 'email_1466925')
    
        company = Company(name=name,
                           url=url,
                           logo_submited=logo_submited,
                           logo_accepted="",
                           contact_email=contact_email,
                           contact_name = contact_name,
                           twitter = twitter,
                           founded_year = year,
                           date_submit = date_submit,
                           status="pending")
        db.session.add(company)

    db.session.commit()
        
    json_data = json.dumps(r.text, indent=4, separators=(',', ':'))
    #print responses
    return json_data


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Auth', index_view=MyAdminIndexView(), base_template='layout.html')

# Add view
admin.add_view(CompanyView(Company, db.session))


def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import string
    import random
    import datetime

    db.drop_all()
    db.create_all()
    # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")
    test_user = User(login="test", password=generate_password_hash("test"))
    db.session.add(test_user)

    db.session.commit()
    return

if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True, port=5001)
