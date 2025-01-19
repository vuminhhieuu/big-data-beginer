.PHONY: setup start stop clean

setup:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

start:
	docker-compose up -d

stop:
	docker-compose down

clean:
	docker-compose down -v
	rm -rf venv
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

logs:
	docker-compose logs -f

kafka-shell:
	docker exec -it kafka bash

topics:
	docker exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092 