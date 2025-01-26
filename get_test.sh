#!/usr/bin/env bash
curl -X GET http://localhost:5001/messages | jq '.'
