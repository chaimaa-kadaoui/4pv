# Pricemoov - Test Data Engineer - 2018

## Objectif général

Ce test contient un dataset de **prévision de demande**, un dataset de **recommandation de prix** et un dataset de **stock disponible**. Ces données sont stockées au niveau (Catégorie + Zone). Le but de cet exercice est de créer un module qui permette de monitorer ces données.

## Description des datasets

Recommandation de prix:

  - Catégorie (category_id): Catégorie de matériel
  - Zone (zone_id): Zone géographique de départ du matériel
  - Date (occupancy_date) : date
  - **prix suggéré (suggested_prices)**

Prévision de demande
- Catégorie (category_id): Catégorie de matériel
- Zone (zone_id): Zone géographique de départ du matériel
- date d'occupation (occupancy_date) : date
- Segment client (yield_class_agg)
- **Prévision (yhat)**
- **erreur (error)**

Stock disponible
- Catégorie (category_id): Catégorie de matériel
- Zone (zone_id): Zone géographique de départ du matériel
- date (date)
- **stock disponible (available_resources)**

### Etape 1: Gestion des alertes

Une alerte peut être créée, détruite et updatée via un CRUD. Elle possède:

  - Un libellé: champs de desription
  - Une date de début d'application: permet de définir le début de la plage de date où le monitoring a lieu
  - Un date de fin d'application: permet de définir la fin de la plage de date où le monitoring a lieu
  - Une donnée de référence (dans notre cas, celles décrites en gras plus haut)
  - Une condition d'application : différence par rapport à une valeur seuil

Ainsi, il est possible de créer une alerte sur les stocks, entre janvier et mars 2019, sur une région/catégorie donnée.
Cette alerte permettra de monitorer les valeurs du dataset.

### Etape 2: Déclanchement des alertes sur les données fournies

Une alerte est active si sa condition n'est pas vérifiée pour une des données sous-jacente. Ainsi, si un seuil de référence n'est pas respecté sur un certain périmetre, un des champs de l'alerte remontera l'information.
Les alertes sont activées par batch quotidien.

### Etape 3: Récupération des alertes actives à un instant t

Les alertes actives peuvent être stockée dans un redis et récupérées par api

### Etape 4: Définir des alertes intelligentes

Définir une méthode pour suggérer des alertes pertinentes portant sur la prévision
Construire ces alertes

### Etape 5: Déploiement

L'application peut-être déployée sur docker.
