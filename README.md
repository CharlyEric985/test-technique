# Test Technique Backend & DevOps – API Articles

## Description

Cette API REST en Django permet de gérer des articles avec :

- Authentification JWT
- Permissions (Admin, Editor, Reader)
- Cache Redis pour accélérer les requêtes sur la liste d'articles

---

## Stack Technique

- Backend : Django 4.x + Django REST Framework  
- Base de données : PostgreSQL  
- Cache : Redis  
- Authentification : JWT (djangorestframework-simplejwt)  
- Containerisation : Docker + docker-compose  

---

## Installation et configuration

1. Cloner le projet :

```bash
git clone https://github.com/axian-group/test-technique
cd test-technique

Créer le fichier .env à partir de l'exemple :

cp .env.example .env

    Lancer Docker :

sudo docker-compose up --build

Appliquer les migrations :

sudo docker-compose exec web python manage.py migrate

Créer un superutilisateur pour accéder à l’admin Django :

sudo docker-compose exec web python manage.py createsuperuser