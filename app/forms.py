from wtforms import form, fields, validators
from werkzeug.security import check_password_hash

from .models import db, User


class LoginForm(form.Form):
    """
    Login and registration forms (for flask-login).
    """
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # Compare the plaintext password with the the hash from the database
        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()
