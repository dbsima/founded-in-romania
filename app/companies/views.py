from flask.ext import login
from jinja2 import Markup
from flask.ext.admin.contrib import sqla

class CompanyView(sqla.ModelView):
    # Override displayed fields
    column_list = ('name',
                   'twitter',
                   'founded_year',
                   'logo_submited',
                   'logo_accepted',
                   'contact_name',
                   'date_submit',
                  'status')
    
        
    column_searchable_list = ('name', 'contact_email')
    
    #form_excluded_columns = ['url', ]
    
    def is_accessible(self):
        return login.current_user.is_authenticated()
    
    def _link_logo(view, context, model, name):
        if not model.logo_submited:
            return ''

        return Markup('<a href="'+model.logo_submited+'" target="_blank">URL</a>')
    
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
    
    def hyperlink(href, text, uri_scheme):
        if not href or not text:
            return ''
        if not href:
            href = '#href'
        if not text:
            text = 'text'
            
        return Markup('<a href="' + uri_scheme+href+'" target="_blank">'+text+'</a>')
    
    column_formatters = {
        'logo_submited': _link_logo,
        'name': _link_name,
        'twitter': _link_twitter,
        'contact_name': _link_mail
    }