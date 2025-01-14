# Variables
APP_NAME = flask-echo-server
DOCKER_IMAGE = $(APP_NAME)
PYTHON = python3
PIP = pip
PORT = 5000

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make install        - Install project dependencies"
	@echo "  make run            - Run the Flask server"
	@echo "  make test           - Run pytest tests"
	@echo "  make docker-build   - Build the Docker image"
	@echo "  make docker-run     - Run the Docker container"
	@echo "  make clean          - Remove unnecessary files (e.g., __pycache__)"

# Install dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Run the Flask server
.PHONY: run
run:
	$(PYTHON) server.py

# Run tests
.PHONY: test
test:
	pytest

# Build the Docker image
.PHONY: docker-build
docker-build:
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker container
.PHONY: docker-run
docker-run:
	docker run -d -p $(PORT):5000 $(DOCKER_IMAGE)

# Clean up unnecessary files
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
