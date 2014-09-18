from app import app, db
from werkzeug.security import generate_password_hash
from app.users.models import User
import os

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

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_db()
        
    # Start app
    try:
        app.run(debug=True, port=8080)
    except Exception:
        app.logger.exception('Failed')
