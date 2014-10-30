import os
import argparse

from werkzeug.security import generate_password_hash

from app import app, db
from app.models import User, Pair, Company, TypeformAPI


def database_setup():
    """
    Create db and populate it with what you get from the Typeform API
    """
    # Create tables
    db.drop_all()
    db.create_all()

    # Add admin account
    admin = User(login="admin", password=generate_password_hash("p4r0l4#3st3#0k"))
    db.session.add(admin)

    # Initialize 'since' variable
    newest_date_submit = Pair(key="since", val=0)
    db.session.add(newest_date_submit)

    # Commit changes to the database
    db.session.commit()

    print 'Database setup completed. Now run the app without --setup.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Founded in Romania app')
    parser.add_argument('--setup', dest='run_setup', action='store_true')

    args = parser.parse_args()
    if args.run_setup:
        database_setup()
    else:
        try:
            import logging
            logging.basicConfig(filename='error.log', level=logging.DEBUG)

            app.run()
        except Exception:
            app.logger.exception('Failed')
