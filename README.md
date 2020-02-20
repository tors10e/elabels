# Development Environment
## Install Docker
Choose a stable installation for your platform https://docs.docker.com/engine/installation/

# Development
## Local development
This useful for local development when you want to bypass kubernetes  (i.e. quick iteration development)
1. CD to ./containers
2. run (sudo) docker-compose up
3. Setup python virtual environment and install packages with 'pip install -r requirements.txt'
CD to ./containers/web
4. python manage.py runserver 8080 --settings=web.settings_local
5. visit page at http://localhost:8080/admin or http://localhost:8080/energyaudit

Admin username = admin
Admin password = LetMeIn!

# Test Environment
1. Create a google account and navigate to cloud.google.com
2. Create a project: (https://console.cloud.google.com/projectselector/kubernetes/list?supportedpurview=project) 
and name the project vessel-energy.
3. Create a kubernetes cluster: 
    - set machine to small instance (micro ran into resource problems so bump it up to next level)
    - use defaults for everything else
4. Install gcloud SDK (https://cloud.google.com/sdk/downloads#apt-get): `
    1. Download package, extract, and install
    2. `gcloud init`
    3. gcloud components install kubectl
    4. Connect using `gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project vessel-eenrgy * get the connection information from gcloud.
5. Create a google cloud storage container for static files by running commands in cloud_storage.sh or by visiting https://console.cloud.google.com/storage/browser/vessel-energy?project=vessel-eenrgy
6. Deploy containers
    1. Build and push images and static files to gcloud by executing kubernets/push_images_gcr.sh
    2. Deploy the database:
        1. change directories to kubernetes  - cd ../../kubernetes/
        2. Create the deployment - kubectl create -f veat-db.yaml
        3. Create the service - kubectl create -f veat-db-service.yaml
    3. Build and deploy the web application:
        1. Create the persistent storage - kubectl create -f veat-app-pv.yaml
        2. Create the deployment - kubectl create -f veat-app.yaml, to update use apply instead of create (kubectl create -f veat-app.yaml)
        3. Create the service - kubectl create -f veat-app-service.yaml to update use apply instead of create (kubectl create -f veat-app-service.yaml)
        4. See services page for ip and port to access application.
        5. Scale app to 0 and back to 1.