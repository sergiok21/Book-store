## Introduction:

This project is a demonstration book store that has several functional features. To ensure high availability and scalability of the system, microservices architecture is used.

## Details:

---

The application has both a user interface and APIs - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`. As additional constraints have been introduced in the project, it is a RESTful project.

Two databases are used - PostgreSQL and Redis. The non-relational database is used for caching objects and interacting with Celery - sending delayed notifications.

## Installation:

---

* Create a virtual environment first.

```
python -m venv venv
venv/Scripts/Activate.ps1
```

* Install dependencies from `requirements.txt` file. Additionally, install psycopg2-binary if the application will be deployed not on Windows.

```
pip install -r requirements.txt
```

* Create and edit the configuration file `.env` with your own parameters for all applications.

```
DEBUG=<Mode>
SECRET_KEY=<Key>

DATABASE_NAME=<Database>
DATABASE_USER=<User>
DATABASE_PASSWORD=<Password>
DATABASE_HOST=<IP>
DATABASE_PORT=<Port>
```

* Perform migration for all applications except for `interfaces`.

```
python manage.py migrate
```

* Create a superuser.

```
python manage.py createsuperuser
```

* To use the program immediately, fixtures based on prepared data are provided.

```
python manage.py loaddata books_service/fixtures/<file.json>
```

* Launch the application:
    - Users service - 8000.
    - Books service - 8001.
    - Baskets service - 8003.
    - Orders service - 8004.
    - Interfaces - 8005.

```
python manage.py runserver <IP>:<Port>
```

*Note. To make everything work correctly, Redis must also be installed.*

## Results:

---

The application can be interacted with both through the interface and APIs. Interaction for admin users is provided to create delayed tasks. The API available for the admin user is protected from regular user requests.
