VENV_PATH := .venv

# Default target
.PHONY: all
all: help

# Install development dependencies
.PHONY: install
install:
	@echo "Installing development dependencies..."
	uv sync

# Format code with Black
.PHONY: black
black:
	@echo "Running Black..."
	uv run black .

# Sort imports with isort
.PHONY: isort
isort:
	@echo "Running isort..."
	uv run isort .

# Run both linters
.PHONY: lint
lint: black isort
	@echo "Linting complete."

# Run pre-commit
.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit..."
	$(VENV_PATH)/bin/pre-commit run --all-files

# Clean up .pyc and cache files
.PHONY: clean
clean:
	@echo "Cleaning up..."
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +

# Display help message
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make install   - Install development dependencies"
	@echo "  make black     - Format code with Black"
	@echo "  make isort     - Sort imports with isort"
	@echo "  make lint      - Run both linters (Black and isort)"
	@echo "  make pre-commit- Run pre-commit"
	@echo "  make clean     - Clean up temporary files"
	@echo "  make help      - Show this help message"

# Build the container
.PHONY: build
build:
	@echo "Building the container..."
	docker build . -t router

# Run the container
.PHONY: run
run:
	@echo "Running the container..."
	docker run -it --rm --env-file .env router

.PHONY: tests
tests: build
	@echo "Running tests inside the container..."
	docker run --rm --env-file .env router pytest -v tests/