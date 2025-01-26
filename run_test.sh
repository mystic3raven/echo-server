#!/usr/bin/env bash

# Generate a random message
message="$(./random_str.sh)"

# Send the message to the /echo endpoint on echo2_server
curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"$message\"}" http://localhost:5001/echo

