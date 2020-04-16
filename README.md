# Ynov_Projet_Devops

## Installation

1. Clone this repository
2. Install Python 3.7 or newer: `brew install python`.
3. Install pip : `sudo easy_install pip`
4. Install "virtualenv" : `pip install virtualenv`
5. Go into "back": `cd back`.
6. Create a new virtualenv called `env`: `virtualenv env`.
7. Start virtualenv: `source env/bin/activate`.
8. Install package `pip install -r requirements.txt`.
9. Migrate : `python manage.py migrate`.
10. Runserver : `python manage.py runserver`

https://cloud.tencent.com/developer/article/1594506 <br>
https://medium.com/@BennettGarner/build-your-first-rest-api-with-django-rest-framework-e394e39a482c <br>
https://www.django-rest-framework.org/tutorial/quickstart/ <br>
https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files <br>
https://medium.com/code-zen/django-mariadb-85cc9daeeef8 <br>
https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04 <br>
https://github.com/tokibito/django-example-todo <br>
`pip freeze -l > requirements.tx`