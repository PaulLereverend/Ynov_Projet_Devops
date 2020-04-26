# Au bon beurre

Ce projet est porté par les étudiants suivants :
- Hugo HUET
- Paul LEREVEREND

# Documentation
Une documentation pour chaque service est présent au sein de leurs dossiers respectifs.

# Utilisation

## Docker

```
docker-compose up
```

front -> http://localhost:8080/

back -> http://localhost:5000/

## Kubernetes (avec minikube)

Installation de minikube (MacOS)
```
brew update && brew install kubectl && brew cask install docker virtualbox && brew install minikube
```
Démarrage de la VM
```
minikube start
```
Utilisation de l'environnement docker de la VM
```
eval $(minikube docker-env)
```
Création d'un registry pour héberger les images
```
docker run -d -p 6000:5000 --restart=always --name registry registry:2
```
Build et push des images sur le registry
```
docker-compose build
docker-compose push
```
Déploiement sur kubernetes
```
kubectl apply -f back-service.yaml,collecteur-deployment.yaml,collecteur-service.yaml,data-1-persistentvolumeclaim.yaml,data-2-persistentvolumeclaim.yaml,data-3-persistentvolumeclaim.yaml,data-4-persistentvolumeclaim.yaml,data-5-persistentvolumeclaim.yaml,db-claim0-persistentvolumeclaim.yaml,db-deployment.yaml,db-service.yaml,front-deployment.yaml,front-service.yaml,ingress.yaml,my-db-persistentvolumeclaim.yaml,unite1-deployment.yaml,unite2-deployment.yaml,unite3-deployment.yaml,unite4-deployment.yaml,unite5-deployment.yaml,back-deployment.yaml
```
Accès au front et au back
```
minikube ip

Ajouter dans /etc/hosts
{minikube_ip}    kubernetes.front
{minikube_ip}    kubernetes.back
```

front -> http://kubernetes.front/

back -> http://kubernetes.back/


### Aide
Pour tout supprimer
```
kubectl delete daemonsets,replicasets,services,deployments,pods,rc --all
```
Pour accéder au dashboard
```
minikube dashboard
```