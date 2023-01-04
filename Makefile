setup: clear build db-prepare 

start:
	docker compose up --abort-on-container-exit

build:
	docker compose build

db-prepare:
	docker compose run --rm backend make migrate && docker compose stop db

start-backend:
	docker compose up -d backend

start-frontend:
	docker compose up -d frontend

start-db:
	docker compose up -d db

stop:
	docker compose stop || true

kill:
	docker compose kill || true

down:
	docker compose down --remove-orphans || true

clear:
	docker compose down -v --remove-orphans || true

backend-bash:
	docker compose run --rm backend bash

frontend-bash:
	docker compose run --rm frontend bash

lint-backend:
	docker compose run --rm backend make lint

test-backend:
	docker compose run --rm backend make test

lint-frontend:
	docker compose run --rm frontend make lint

test-frontend:
	docker compose run --rm frontend make test
