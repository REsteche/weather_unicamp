#!/bin/bash

# Default tag value
TAG="latest"

# Parse command-line arguments
while getopts "t:" opt; do
  case $opt in
    t) TAG=$OPTARG ;;
    \?) echo "Invalid option: -$OPTARG" >&2
        exit 1 ;;
  esac
done

# Build and run the Docker container using Docker Compose
docker-compose build --build-arg TAG="$TAG"
docker-compose up
