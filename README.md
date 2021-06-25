# django_backend_irobot
backend test for iRobot company

create a new python enviroment:
	-> $ python -m venv

activate env:
	-> $ source myvenv/bin/activate

clone repository:

	-> $ git clone https://github.com/fabrilopez/django_backend_irobot.git

move provided .env file to same directory manage.py:

install requeriments:
	-> $ pip install -r requirements.txt

create a database named irobot with mysql:
	
	-> $ mysql -u root -p
	>> CREATE DATABASE irobot;

modify credentials on file .env to correspondent mysql instalation.

run makemigrations:

	-> $ python manage.py makemigrations

run migrate:

	-> $ python manage.py migrate

create superuser:

	-> $ python manage.py createsuperuser
	-> <new superuser credentials>

generate toke for superuser:

	-> $ python manage.py drf_create_token -r <username>

run server:

	-> $ python manage.py runserver 8080

open http://localhost:8080/admin to enter backend admin site with superuser credentials.

Thats it! in my laptop works...!!! :)

