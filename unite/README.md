# Unités

## Création des données
Les données sont crées puis stockées dans des fichier ici.
```
python3 src/main.py [numero_unite]
```

## Observateur
L'observateur va regarder s'il y a un nouveau fichier de données et par la suite il va envoyer son contenu au collecteur pour insérer les données dans la base de données.
> **Le collecteur doit être lancer pour que l'observateur puisse lui envoyer les données**
```
python3 src/connection.py
```

## Tests

```
pytest
```