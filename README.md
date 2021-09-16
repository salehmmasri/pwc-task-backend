# Departments Management System

## Overview  
- Backend for the Departments Management System, using ElephantSQL as a DataBase and Docker container

---

## Deployed link

- [Backend deployed on Heroku](https://employee-be.herokuapp.com/)

---


## Paths
- /admin/empolyees/
- /api/v1/empolyees/all
- /api/v1/empolyees/<int:pk>
- /api/v1/department/
- /api/v1/department/<int:pk>

---

## Dependencies  
- python = "^3.9"
- Django = "^3.2.7"
- djangorestframework = "^3.12.4"
- django-environ = "^0.7.0"
- django-filter = "^2.4.0"
- django-cors-headers = "^3.8.0"
- gunicorn = "^20.1.0"
- whitenoise = "^5.3.0"
- psycopg2-binary = "^2.9.1"

---

## Authors  
- Software Developer: Saleh Al-Masri
  - [Official Github](https://github.com/salehmmasri)   

---

## enviroment variables
- ALLOWED_HOSTS
- DATABASE_HOST
- DATABASE_NAME
- DATABASE_PASSWORD
- DATABASE_PORT
- DATABASE_USER
- DEBUG
- ENGINE
- PROJECT_PATH
- SECRET_KEY