export PROJECT_ID=${PROJECT_ID}
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-central1-a
gcloud container clusters create pn-cluster --num-nodes 3 
gcloud container clusters get-credentials pn-cluster

docker pull patrick699/frontend:1.0.1
docker pull patrick699/conv:1.0.0

docker tag patrick699/frontend:1.0.1 gcr.io/$PROJECT_ID/frontend:1.0.1
docker tag patrick699/conv:1.0.0 gcr.io/$PROJECT_ID/conv:1.0.0

docker push gcr.io/$PROJECT_ID/frontend:1.0.1
docker push gcr.io/$PROJECT_ID/conv:1.0.0

kubectl create service clusterip conv --tcp 9000
kubectl create service loadbalancer front --tcp=8000:5000
kubectl create deployment conv --image=gcr.io/$PROJECT_ID/conv:1.0.0
kubectl create deployment front --image=gcr.io/$PROJECT_ID/frontend:1.0.1

