install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check VD_games

VD-even:
	uv run VD-even

VD-calc:
	uv run VD-calc

VD-gcd:
	uv run VD-gcd
