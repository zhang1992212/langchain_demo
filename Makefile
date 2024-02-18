.PHONY: up
up:
	@pip freeze > requirements.txt

.PHONY: down
down:
	@pip install -r requirements.txt
