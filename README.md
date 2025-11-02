# Ramp

Ramp is a Python-first CLI that provisions a production-ready Firebase stack - auth, DB, payments, email, hosting, CI - in under 30 minutes, leaving you with a clean repo and a live app you own.

## Development

### Setup

1. Install [uv](https://github.com/astral-sh/uv) (Python package manager)
2. Sync dependencies:
   ```bash
   uv sync --extra dev
   ```

### Quick Commands

```bash
# Run the CLI
uv run ramp

# Run tests
uv run pytest tests/ -v

# Check linting
uv run ruff check src tests

# Format code
uv run ruff format src tests

# Auto-fix linting issues
uv run ruff check src tests --fix
```

### Project Structure

```
ramp/
├── src/ramp/          # Source code
│   ├── cli.py        # CLI entry point
│   └── __main__.py   # Module entry point
├── tests/            # Test suite
└── pyproject.toml    # Project configuration
```

### Code Quality

- **Linting**: Ruff is configured for code quality checks
- **Formatting**: Ruff formatter is used for consistent code style
- **Type hints**: Use type hints for all functions and methods
- **Docstrings**: Follow Google Python Style Guide for docstrings
