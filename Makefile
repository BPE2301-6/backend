.PHONY: check fix

check:
	@echo "🧪 checking with ruff..."
	uv run --active ruff check .

fix:
	@echo "🛠 auto-fixing with ruff..."
	uv run --active ruff check . --fix
