compose: compose-clear compose-setup compose-start

compose-start:
		docker compose up --abort-on-container-exit

compose-stop:
		docker compose stop || true

compose-down:
		docker compose down --remove-orphans || true

compose-clear:
		docker compose down -v --remove-orphans || true

compose-setup: compose-build
		docker compose run -rm backlog-tracker-backend make setup

compose-bash:
		docker compose run -rm backlog-tracker-backend bash

compose-build:
		docker compose build

