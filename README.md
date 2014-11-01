# Founded In Romania

  * Website for [www.foundedinromania.com](http://foundedinromania.com).
  * Created by [Cloudients](http://www.cloudients.com).

## Features
  1. Shows the first page with the list of startups.
  2. Shows an about page about the country of the startups.
  3. Has a backoffice to ease the management of the database.

## Technologies

### Server-side

  * [Flask](http://flask.pocoo.org/): web microframework for Python based on Werkzeug and Jinja 2.
  * [PostgreSQL](http://www.postgresql.com): Relational database, used to store the company descriptions, user accounts for backoffice and key-value pairs.

### Client-side
  * [jQuery](http://www.jquery.com): Cross-browser compliant JavaScript code.
  * [Modernizr](http://modernizr.com/): JavaScript library that detects HTML5 and CSS3 features in the browser.
  * [Font Awesome](http://fortawesome.github.io/Font-Awesome/): iconic font and CSS toolkit.

## Installation Instructions

### Prerequisites

#### Relational Database (PostgreSQL)

Before beginning installation, we must first set the database.  For Ubuntu, Fabric will do that for you, but for you're a Mac OS user simply [download](http://postgresapp.com/) and install.

Many common tasks, such as installing dependencies, deploying servers, migrations,
and configurations are in `fabfile.py`.

#### Python packages

From inside the repository, run:

    pip install -r requirements.txt


### Install PostgreSQL
```shell
sudo apt-get install postgresql postgresql-contrib pgadmin3
```
### Create a database user with full rights on it
```shell
sudo -u postgres createuser -D -A -P myuser
sudo -u postgres createdb -O myuser mydb
```
### Restart the PostgreSQL server
```shell
sudo /etc/init.d/postgresql restart
```
### Install the Python packages manager
```shell
sudo apt-get install python-pip
```
### Install virtualenv Python package
```shell
sudo pip install virtualenv
```
### Create virtualenv
```shell
cd founded-in-romania
virtualenv venv
```
### Add the following lines to venv/bin/activate file
```shell
export DATABASE_URL="postgresql://myuser:password@localhost/mydb"
export APP_SETTINGS="config.DevelopmentConfig"
```
### Activate virtualenv
```shell
source venv/bin/activate
```
### Install all necessary packages
```shell
pip install -r requirements.txt
```
### Access the app
```shell
python run.py --setup
```
Go to http://localhost:5000/
