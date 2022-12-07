docker-build:
	docker compose build 

docker-up:
	docker compose up

install:
	poetry install

start:
	poetry run uvicorn backlog_tracker.app:app --reload --host 0.0.0.0 --port 8080

lint:
	poetry run flake8 .

test:
	poetry run pytest .

coverage-report:
	@poetry run python -m pytest --cov=app --cov-report xml

migration:
	poetry run alembic revision --autogenerate -m $(ARGS)

migrate:
	poetry run alembic upgrade head

check: lint test
