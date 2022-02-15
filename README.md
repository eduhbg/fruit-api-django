# Fruit API with Django

## Overview
The project aims to study Django and Django Rest Framework in a pratical context.

![image](https://user-images.githubusercontent.com/58524485/153967458-eee68e80-fa4e-416c-9d1e-a87bd26f8751.png)


## Features
- [x] GET, POST, DELETE and PUT data with API

## Running the project
Go to the project folder (`cd .../fruit-api-django/`) with your terminal and type:
```
sudo apt install python3-virtualenv
virtualenv env
source env/bin/activate
pip install django
pip install djangorestframework
python3 manage.py runserver
```

The project will run in localhost (http://127.0.0.1:8000/).

To see all the data, just make a request with the endpoint http://127.0.0.1:8000/fruits/ or http://127.0.0.1:8000/regions/.

To change or delete, just pass the id in the endpoint (http://127.0.0.1:8000/fruits/id/) and in the body (json) fill in with the text you want to change, such as the fruit name. If you want to delete, just fill the id in the endpoint. 

## Dependencies
- [Python](https://www.python.org/downloads) - used version 3.8.10;
- Virtualenv (`sudo apt install python3-virtualenv`);
- Check out for more dependencies [here](https://github.com/eduhbg/fruit-api-django/blob/main/requirements.txt).
