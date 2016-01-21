clean:
	find . -name "*.pyc" -delete

deps:
	pip install -r requirements/development.txt

setup: clean deps
	rm -rf db.sqlite3
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser

run:
	python manage.py runserver
