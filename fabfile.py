from fabric.api import *

env.key_filename = '/home/dbsima/founded-in-romania/fir.pem'

PROJECT_DIR = '/var/www/app/founded-in-romania/'

def deploy(user, host):
    """
    On the server, update local repository to the latest production version and
    restart the app.
    """
    env.hosts = [host]
    env.user = user
    with cd(PROJECT_DIR):
        run('git pull origin master')
        run('cp ../config.py .')
        run('source venv/bin/activate')
        # kill the server
        run('kill `cat rocket.pid`')
        # demonize the app runner with pid writen in rocket.pid
        run('gunicorn run:app -p rocket.pid -D')
        run('ls -lat')

def local_migrate_db():
    """
    Update the local database with the content of the database on the server
    """
    with cd(PROJECT_DIR):
        pass
