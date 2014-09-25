'''
This is the file that is invoked to start up a development server. It gets a
copy of the app from your package and runs it. This won't be used in production,
but it will see a lot of mileage in development.
'''

import os
import argparse
from app import app, db
from werkzeug.security import generate_password_hash
from app.models import User, Pair


def database_setup():
    """
        
    """
    # Create tables
    db.drop_all()    
    db.create_all()
    
    # Add admin account
    admin = User(login="test", password=generate_password_hash("test"))
    db.session.add(admin)
    
    # Initialize 'since' variable
    newest_date_submit = Pair(key="since", val=0)
    db.session.add(newest_date_submit)

    # Commit changes to the database
    db.session.commit()
    print 'Database setup completed. Now run the app without --setup.'

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run New-Responsive-Image-Format app')
    parser.add_argument('--setup', dest='run_setup', action='store_true')

    args = parser.parse_args()
    if args.run_setup:
        database_setup()
    else:
        try:
            app.run()
        except Exception:
            app.logger.exception('Failed')