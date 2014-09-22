from app.shared.models import db

# Company model
class Company(db.Model):
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

    # Required for administrative interface
    def __unicode__(self):
        return self.name