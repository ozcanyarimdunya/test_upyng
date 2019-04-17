.PHONY: default

default: migrations

doc:
	docker-compose up --build

dockerd:
	docker-compose up -d --build

migrations:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser