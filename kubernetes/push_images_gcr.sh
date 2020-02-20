#!/usr/bin/env bash
    echo "****************************"
	echo "Building web app image...."
	echo "****************************"
	docker build -t gcr.io/vessel-eenrgy/veat_app:v1 ../containers/web
	echo "****************************"
	echo "Web app image build complete, building database image ...."
	echo "****************************"
	docker build -t gcr.io/vessel-eenrgy/veat-db:v1 ../containers/database
	echo "****************************"
	echo "Database image build complete, pushing web app image to google repository"
	echo "****************************"
    docker push gcr.io/vessel-eenrgy/veat_app:v1
    echo "****************************"
    echo "Pushing database image to google repository"
    echo "****************************"
    docker push gcr.io/vessel-eenrgy/veat-db:v1
    echo "****************************"
    echo "Synchronizing google storage container with static directory"
    echo "****************************"
    gsutil rsync -R ../containers/web/static/ gs://vessel-energy/static
    echo "****************************"
    echo "Push complete, scale containers appropriately on k8 to finish deployment."
    echo "****************************"