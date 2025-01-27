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
	@echo "  make clean     - Clean up temporary files"
	@echo "  make help      - Show this help message"
