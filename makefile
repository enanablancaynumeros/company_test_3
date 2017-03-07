build_api:
	cd docker && \
	docker-compose build

run:
	cd docker && \
	docker-compose up -d kombu_consumer

run_workers:
	cd docker && \
	docker-compose up -d worker

run_web:
	cd docker && \
	docker-compose up -d web

logs:
	cd docker && \
	docker-compose logs

integration_tests:
	cd docker && \
	docker-compose build && \
	docker-compose up tests

install_env:
	./bin/install_on_ubuntu.sh

docker_cleanup:
	cd docker && \
	docker-compose down -v