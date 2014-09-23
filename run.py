'''
This is the file that is invoked to start up a development server. It gets a
copy of the app from your package and runs it. This won't be used in production,
but it will see a lot of mileage in development.
'''

import os
from app import app, db
from werkzeug.security import generate_password_hash
from app.models import User


def build_db():
    """
    Populate a small db with some example entries.
    """

    import string

    db.drop_all()
    db.create_all()
    
    # Passwords are hashed
    test_user = User(login="test", password=generate_password_hash("test"))
    db.session.add(test_user)

    db.session.commit()
    return


if __name__ == '__main__':
    
    db.drop_all()    
    db.create_all()
    test_user = User(login="test", password=generate_password_hash("test"))
    db.session.add(test_user)

    db.session.commit()

    # Build a sample db on the fly, if one does not exist yet.
    #app_dir = os.path.realpath(os.path.dirname(__file__))
    #database_path = os.path.join(app_dir, "app/" + app.config['DATABASE_FILE'])
    
    #print database_path 
    
    #if not os.path.exists(database_path):
    #    build_db()
        
    # Start app
    try:
        app.run()
    except Exception:
        app.logger.exception('Failed')
