default: build

build:
	docker-compose up --build

start:
	docker-compose up

stop:
	docker-compose down

clean:
	docker-compose down -v