install:
	poetry install

serve:
	poetry run uvicorn backlog_tracker.app:app --reload --host 0.0.0.0 --port 5000

lint:
	poetry run flake8 .

test:
	poetry run pytest .

coverage-report:
	@poetry run python -m pytest --cov=backlog_tracker --cov-report xml

migration:
	poetry run alembic revision --autogenerate -m $(ARGS)

migrate:
	poetry run alembic upgrade head

check: lint coverage-report
