compose: compose-clear compose-build compose-db-prepare compose-start

compose-start:
	docker compose up --abort-on-container-exit

compose-build:
	docker compose build

compose-db-prepare:
	docker compose run --rm backend make migrate

compose-start-backend:
	docker compose up -d backend

compose-start-db:
	docker compose up -d db

compose-stop:
	docker compose stop || true

compose-down:
	docker compose down --remove-orphans || true

compose-clear:
	docker compose down -v --remove-orphans || true

compose-backend-bash:
	docker compose run --rm backend bash

compose-frontend-bash:
	docker compose run --rm frontend bash

compose-lint-backend:
	docker compose run --rm backend make lint

compose-test-backend:
	docker compose run --rm backend make test

compose-test-cov:
	docker compose run --rm backend make coverage-report

compose-lint-frontend:
	docker compose run --rm frontend make lint

compose-test-frontend:
	docker compose run --rm frontend make test
