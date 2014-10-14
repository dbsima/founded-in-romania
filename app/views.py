'''
This is where the routes are defined. It may be split into a package of its own
(app/views/) with related views grouped together into modules.
'''

import os

from jinja2 import Markup

from wtforms.fields import SelectField

from flask import  redirect, url_for, request
from flask.ext import login, admin
from flask.ext.admin import helpers, expose, form
from flask.ext.admin.contrib import sqla
from flask.ext.admin.form import rules

from .models import db, User, Company
from .forms import LoginForm

from flask.ext.admin.base import BaseView, expose
from flask.ext.admin.actions import action, ActionsMixin

class UserView(sqla.ModelView):
    """
        
    """ 
    def is_accessible(self):
        return login.current_user.is_authenticated()
    


# Create 
class AdminIndexView(admin.AdminIndexView):
    """
    Customized index view class that handles login/logout    
    """
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(AdminIndexView, self).index()

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
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
    
    
app_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir))
logo_path = os.path.join(app_dir, 'app/static/images/logos')


class CompanyView(sqla.ModelView):
    """
        
    """
    column_list = ('name',
                   'founded_year',
                   'logo_submited',
                   'logo',
                   'contact_name',
                   'date_submit',
                  'status')
    
    column_labels = dict(founded_year='Year', contact_name='Contact')
    column_searchable_list = ('name', 'contact_email', 'status')
    column_default_sort = ('date_submit', True)
    column_filters = ('founded_year', 'status')
    
    page_size = 20
    
    #form_excluded_columns = ['url', ]
    
    # Override form field to use Flask-Admin SelectField
    form_overrides = {
        'logo': form.FileUploadField,
        'status': SelectField
    }
    
    def prefix_name(obj, file_data):
        import uuid
        return str(uuid.uuid4())+".png"

    
    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'logo': {
            'label': 'File',
            'base_path': logo_path,
            'namegen': prefix_name
        },
        'status': dict(
            choices=[('pending', 'pending'), ('accepted', 'accepted'), ('hidden', 'hidden')])
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
    
    #action_disallowed_list = ['delete']
    
    def is_action_allowed(self, name):    
        return super(CompanyView, self).is_action_allowed(name)
    
    @expose('/action/', methods=('POST',))
    def action_view(self):
        return self.handle_action()

    # Actions
    @action('status_pending', 'Change status to pending', 'Are you sure you want to make the status pending?')
    def action_pending(self, items):
        for item in items:
            Company.query.filter_by(id=item).update({'status': 'pending'})
        db.session.commit()
            
    @action('status_accepted', 'Change status to accepted', 'Are you sure you want to make the status accepted?')
    def action_approved(self, items):
        for item in items:
            Company.query.filter_by(id=item).update({'status': 'accepted'})
        db.session.commit()
    
    @action('status_hidden', 'Change status to hidden', 'Are you sure you want to make the status hidden?')
    def action_hidden(self, items):
        for item in items:
            Company.query.filter_by(id=item).update({'status': 'hidden'})
        db.session.commit()
            
