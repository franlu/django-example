# django-example
A basic example of django project.

This example contains a project to manage information about shops. Within the project there's an application that is responsible for storing info about the shops in a database. These cards contain the following information about each shop:

* name
* kind
* description
* logo
* image
* tags

### App structure folder
![App folder](/doc/image/struct-app.png)

**This example is written with Python 3.7 and Django 2.2.3**


If you don’t have pip installed, this [Python installation guide](https://docs.python-guide.org/starting/installation/) can guide you through the process.

The sources for django-example can be downloaded. You can either clone the public repository:

```
git clone git://github.com/franlu/django-example
```

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-2.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## requirements.txt

requirements.txt should have the following lines:

```
Django>=2.2.3
django-bootstrap3==11.1.0
Pillow==6.1.0
pytz==2019.1
sqlparse==0.3.0
```
