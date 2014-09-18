from app.shared.models import db

# Create Company model
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
    status = db.Column(db.String(64))

    # Required for administrative interface
    def __unicode__(self):
        return self.name