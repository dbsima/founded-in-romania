import os

from flask import url_for
from flask.ext import login
from jinja2 import Markup

from flask.ext.admin import form
from flask.ext.admin.form import rules

from flask.ext.admin.contrib import sqla

from app.companies.models import Company

app_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir))
print app_dir
logo_path = os.path.join(app_dir, 'static/images/logos')
print logo_path

class CompanyView(sqla.ModelView):
    # Override displayed fields
    column_list = ('name',
                   'founded_year',
                   'logo_submited',
                   'logo',
                   'contact_name',
                   'date_submit',
                  'status')
    
    column_labels = dict(founded_year='Year', contact_name='Contact')
    
        
    column_searchable_list = ('name', 'contact_email', 'status')
    
    #form_excluded_columns = ['url', ]
    
    # Override form field to use Flask-Admin FileUploadField
    form_overrides = {
        'logo': form.FileUploadField
    }
    
    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'logo': {
            'label': 'File',
            'base_path': logo_path
        }
    }
    
    def is_accessible(self):
        return login.current_user.is_authenticated()
    
    def _link_logo_submitted(view, context, model, name):
        if not model.logo_submited:
            return ''

        return Markup('<a href="'+model.logo_submited+'" target="_blank">URL</a>')
    
    def _link_logo(view, context, model, name):
        if not model.logo:
            return ''
        
        return Markup('<a href="'+url_for('static', filename='images/logos/' + model.logo)+'" target="_blank">link</a>')
    
    def _link_name(view, context, model, name):
        if not model.url or not model.name:
            return ''

        return Markup('<a href="'+model.url+'" target="_blank">'+model.name+'</a>')
    
    def _link_twitter(view, context, model, name):
        if not model.twitter:
            return ''

        return Markup('<a href="https://twitter.com/'+model.twitter+'" target="_blank">'+model.twitter+'</a>')
    
    def _link_mail(view, context, model, name):
        if not model.contact_email or not model.contact_name:
            return ''

        return Markup('<a href="mailto:'+model.contact_email+'" target="_blank">'+model.contact_name+'</a>')
    
    column_formatters = {
        'logo_submited': _link_logo_submitted,
        'logo': _link_logo,
        'name': _link_name,
        'twitter': _link_twitter,
        'contact_name': _link_mail
    }