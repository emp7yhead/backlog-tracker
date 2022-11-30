docker-up:
	docker compose up

install:
	poetry install

start: migrate
	poetry run uvicorn run:app --reload

lint:
	poetry run flake8 .

test:
	poetry run pytest .

coverage-report:
	@poetry run python -m pytest --cov=app --cov-report xml

makemigration:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic upgrade head

check: lint test
