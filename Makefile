test:
	docker-compose run --rm  fastapi  python3.8 -m pytest . --disable-pytest-warnings

coverage:
	docker-compose exec fastapi python3.8 . --disable-pytest-warnings --cov="."

coverage-report:
	docker-compose exec fastapi python3.8 -m pytest . --disable-pytest-warnings --cov="." --cov-report html && open app/htmlcov/index.html
