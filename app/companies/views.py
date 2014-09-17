from flask.ext import login
from jinja2 import Markup
from flask.ext.admin.contrib import sqla

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

        return Markup('<a href="'+model.url+'" target="_blank">'+model.url+'</a>')
    
    def _link_twitter(view, context, model, name):
        if not model.url:
            return ''

        return Markup('<a href="https://twitter.com/'+model.twitter+'" target="_blank">'+model.twitter+'</a>')

    column_formatters = {
        'logo_submited': _link_logo,
        'url': _link_url,
        'twitter': _link_twitter
    }