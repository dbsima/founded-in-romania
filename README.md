# Founded In Romania

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
### Activate virtualenv
```shell
source venv/bin/activate
```
### Install all necessary packages
```shell
pip install -r requirements.txt
```

### Tested
```shell
python run.py
```
Go to http://localhost:5000/ and to http://localhost:5000/data to populate the db