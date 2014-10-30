# Founded In Romania

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