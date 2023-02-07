install:
	poetry install

serve:
	poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 5000

lint:
	poetry run flake8 .

test:
	poetry run pytest .

coverage-report:
	@poetry run python -m pytest --cov=src --cov-report xml

migration:
	poetry run alembic revision --autogenerate -m $(ARGS)

migrate:
	poetry run alembic upgrade head

check: lint coverage-report
