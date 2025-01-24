#!/usr/bin/env bash
message="$(./random_str.sh)"
curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"$message\"}" http://localhost:5001/echo

# curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, ECS!"}' http://127.0.0.1:5000/echo
