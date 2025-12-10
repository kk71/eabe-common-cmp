#!/bin/sh

prod_user="root"
prod_ip="106.15.250.228"
default_image_name="eb-cmp-backend"

docker rmi $default_image_name
docker build -t $default_image_name -f ./Dockerfile ..

echo "image successfully built as ${default_image_name}:lastest"
