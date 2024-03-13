#!/bin/sh
docker build -t cyril4000/psba-django ./app/.
docker push cyril4000/psba-django

docker build -t cyril4000/psba-api ./api/.
docker push cyril4000/psba-api

az container create --resource-group RG_JULLIARDC --file deploy.yaml