from flask import  redirect, url_for, request
from flask.ext import login, admin
from flask.ext.admin import helpers, expose
from flask.ext.admin.contrib import sqla

from app.users.forms import LoginForm

# Create customized model view class for User
class UserView(sqla.ModelView):
    # 
    def is_accessible(self):
        return login.current_user.is_authenticated()


# Create customized index view class that handles login & registration
class AdminIndexView(admin.AdminIndexView):

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