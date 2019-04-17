.PHONY: default

default: install

doc:
	docker-compose up --build

dockerd:
	docker-compose up -d --build

install:
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 127.0.0.1:8000

superuser:
	python manage.py createsuperuser