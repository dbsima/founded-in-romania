# Founded In Romania

  * Website for [www.foundedinromania.com](http://foundedinromania.com).
  * Created by [Cloudients](http://www.cloudients.com).

## Features
  1. Shows the first page with the list of startups.
  2. Shows an about page for the origin country of the startups.
  3. Has a backoffice to ease the management of the database.
  4. Register new companies with a Typeform form

## Technologies

### Server-side

  * [Flask](http://flask.pocoo.org/): web microframework for Python based on Werkzeug and Jinja 2.
  * [PostgreSQL](http://www.postgresql.com): Relational database, used to store the company descriptions, user accounts for backoffice and key-value pairs.

### Client-side
  * [jQuery](http://www.jquery.com): Cross-browser compliant JavaScript code.
  * [Modernizr](http://modernizr.com/): JavaScript library that detects HTML5 and CSS3 features in the browser.
  * [Font Awesome](http://fortawesome.github.io/Font-Awesome/): iconic font and CSS toolkit.

## Installation Instructions

### Installing on Linux / Ubuntu

#### Install and configure PostgreSQL
  1. Install PostgreSQL
    ```shell
    sudo apt-get install postgresql postgresql-contrib pgadmin3
    ```

  2. Create a database user with full rights on it
    ```shell
    sudo -u postgres createuser -D -A -P myuser
    sudo -u postgres createdb -O myuser mydb
    ```

  3. Restart the PostgreSQL server
    ```shell
    sudo /etc/init.d/postgresql restart
    ```

#### Install the Python packages manager
  ```shell
  sudo apt-get install python-pip
  ```

#### Work in a virtualenv Python package
  1. Install virtualenv
    ```shell
    sudo pip install virtualenv
    ```

  2. After cloning the repo create the virtualenv
    ```shell
    cd founded-in-romania
    virtualenv venv
    ```

  3. Add the following lines to venv/bin/activate file
    ```shell
    export DATABASE_URL="postgresql://myuser:password@localhost/mydb"
    export APP_SETTINGS="config.DevelopmentConfig"
    ```

  4. Activate virtualenv
    ```shell
    source venv/bin/activate
    ```

  5. Install all necessary packages
    ```shell
    pip install -r requirements.txt
    ```

## Configure app

  1. Go to [Typeform](http://www.typeform.com/) and create a typeform with the exact following questions:
    * "Startup name" (short text, required)
    * "Year founded" (number, required)
    * "Web address" (website, required)
    * "Twitter handle" (short text)
    * "URL to high-resolution logo (.psd, .ai or another)" (website, required)
    * "Contact person" (short text, required)
    * "Contact email address" (email, required)

  Note: these fields are required for this app to work, but you can adapt them as you want

  2. Change config.py with the variables suitable for you and add the file to .gitignore

## Access the app
```shell
python run.py --setup
```
Go to http://localhost:5000/


License
=======
This software is licensed under the MIT License. See [LICENSE.md] (https://github.com/FoundedX/founded-in-romania/blob/master/LICENSE.md) for details.

Portions of this software are copyright of their own owners as described in the files containing them.
