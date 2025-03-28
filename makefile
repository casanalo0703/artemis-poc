PYTHON_SCRIPT=producer/producer.py
DOCKER_COMPOSE_FILE=docker-compose.yaml

.PHONY: run stop

run:
    @echo "Raising environment..."
    docker-compose up -d
    python3 $(PYTHON_SCRIPT)
	@echo "Env complete, use http://localhost:8081/console to view the console..."
	@echo "Use http://localhost:61616 to send messages to a given queue or topic..."

stop:
    @echo "Tearing down the env..."
    @pkill -f $(PYTHON_SCRIPT) || echo "El script de Python no está corriendo."
    docker-compose down
	@echo "Env torn down."