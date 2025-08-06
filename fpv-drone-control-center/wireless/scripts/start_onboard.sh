#!/usr/bin/env bash
export DOCKER_DEFAULT_PLATFORM=linux/arm64
docker compose -f ../docker/docker-compose.yml up onboard --build