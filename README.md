# track image experiments
This is a very minimal database for tracking metadata from imaging experiments. It simply uses the Django admin panel.

### 1. create and active virtual environment
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```
### 2. load requirements
```
$ pip install -r requirements.txt
```
### 3. initialize database
```
$ cd main
$ python manage.py makemigrations core
$ python manage.py migrate
```
### 4. run gunicorn
```
$ ../.venv/bin/gunicorn main.wsgi
```
### 5. default website
http://127.0.0.1:8000/admin/