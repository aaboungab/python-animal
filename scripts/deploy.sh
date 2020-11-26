#! /bin/bash

echo "Pulling images from Dockerhub.."
docker-compose pull
docker stack deploy --compose-file docker-compose.yaml animalapp


