# flask-crud

Simple Flask based server to access MariaDB

## Installation

1. Clone this repository into your project directory
2. Create a virtual env inside the directory and activate it:
```
python -m venv venv
. venv/bin/activate
```
3. Create .env file with the following options (Replace with your parameters):
```
DB_IP="XXX.XXX.XXX.XXX"
DB_PORT=0000
DB_USER="my_db_user"
DB_PASS="my_db_pass"
DB_NAME="my_db_name"

SERVER_IP=XXX.XXX.XXX.XXX
SERVER_PORT=0000
```
4. Install requirements
```
pip install -r requirements.txt
```
5. Start the server:
```
gunicorn -c gunicorn.conf.py main:app
```
