# Au bon beurre

Ce projet est porté par les étudiants suivants :
- Hugo HUET
- Paul LEREVEREND

# Definition of done

### Partie 1: Terminée
* ✔ Automates écrivant les données dans un fichier json
* ✔ Script lisant les fichiers et insérant le données dans la bdd	
* ✔ Back permettant d’interroger la bdd	
* ✔ Front permettant d’afficher les données sur une plage de 60 min glissant	
* ✔ Conteneurs suivant schéma d’archi	
* ✔ Orchestrateur kubernetes 
### Partie 2: A présenter
* ✔ Tests Unitaires automatiques
* ✔ Déploiement automatique	
* ✔ Pipelines de récupération des sources sur le repository github
### Partie 3: En cours
* Schéma de bdd scalable
* Création des utilisateurs
* Base de donnée compressée
* Dump quotidien de la base


# Documentation
Une documentation pour chaque service est présent au sein de leurs dossiers respectifs.

## Gestion des commits
Nous avons décidé que nos commit auraient cette forme-ci :
`(feature) : (ajout,update,delete...)+(sujet du commit)`

## Gestion de configuration
Voici la configuration de notre git :
1. Master/prod
    1. pre-prod -> configurations docker/kubernetes
        1. develop -> configurations local
            1. back
            2. front
            3. unite
            4. collecteur
            5. docker

## A faire avant de merge sur master

- [ ] Lancer les tests unitaires
- [ ] Faire un déploiement sur la pré-prod
- [ ] Mettre à jour le changelog
- [ ] Prévenir les clients

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
