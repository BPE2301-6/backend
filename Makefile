.PHONY: format lint check fix

# форматирование
format:
	@echo "🧹 formatting with ruff..."
	uv run --active ruff check . --fix

# линтинг без исправлений
lint:
	@echo "🔍 linting with ruff..."
	uv run --active ruff check .

# проверка форматирования + линтинг
check:
	@echo "🧪 checking with ruff..."
	uv run --active ruff check .

# автофикс (если хочешь отдельно от format)
fix:
	@echo "🛠 auto-fixing with ruff..."
	uv run --active ruff check . --fix
