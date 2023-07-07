# Makefile

PROJECT_DIR := $(shell pwd)
CACHE_DIRS := $(shell find $(PROJECT_DIR) -type d -name "cache" -o -name "__pycache__" -o -name ".pytest_cache")

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

# Apply the last alembic migrations
migrate:
	@alembic upgrade head

# Run application server
server:
	@hypercorn src.main:app --reload --bind 0.0.0.0:8000

# Run all tests
test:
	@pytest .

# Create a standalone docker container with postgres
database:
	@docker run --rm --name fastapi-db -e POSTGRES_PASSWORD=$(DB_PASSWORD) -e POSTGRES_USER=$(DB_USER) -e POSTGRES_DB=$(DB_NAME) -d -p $(DB_PORT):5432 postgres:14
