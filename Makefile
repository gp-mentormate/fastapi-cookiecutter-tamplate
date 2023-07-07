# Makefile

PROJECT_DIR := $(shell pwd)
CACHE_DIRS := $(shell find $(PROJECT_DIR) -type d -name "cache" \
	-o -name "__pycache__" -o -name ".pytest_cache" -o -name "htmlcov")

# Load environment variables from .env file
include .env
export $(shell sed 's/=.*//' .env)

# Clean target to delete .pytest_cache directories and Python cache files
clean:
	@echo "Cleaning up cache folders..."
	@for dir in $(CACHE_DIRS); do \
		echo "Removing: $$dir"; \
		rm -rf $$dir; \
	done

# Run application server
server:
	@hypercorn src.main:app --reload --bind 0.0.0.0:8000

# Run all tests
test:
	@FASTAPI_TEST=true pytest .

# Run test coverage and open it as HTML report
coverage:
	@FASTAPI_TEST=true coverage run -m pytest .
	@coverage html && open htmlcov/index.html

# Create a standalone docker container with postgres
database:
	@docker run --rm --name fastapi-db -e POSTGRES_PASSWORD=$(DB_PASSWORD) -e POSTGRES_USER=$(DB_USER) -e POSTGRES_DB=$(DB_NAME) -d -p $(DB_PORT):5432 postgres:14

# Create migration
migration:
	@if [ -z "$(m)" ]; then \
		echo "Please provide a migration message using 'make migration m=\"MESSAGE\"'"; \
	else \
		echo "Making migration with message: $(m)"; \
		alembic revision --autogenerate -m "$(m)"; \
	fi

# Apply the last alembic migrations
migrate:
	@alembic upgrade head