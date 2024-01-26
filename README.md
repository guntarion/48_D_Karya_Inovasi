# Soft UI Design PRO Django

**Django Web App** generated by `AppSeed` op top of a modern design. Designed for those who like bold elements and beautiful websites, **Soft UI Design PRO** is ready to help you create stunning websites and webapps. 

- 👉 [Soft UI Design PRO Django](https://appseed.us/product/soft-ui-design-pro/django/) - Product page
- 👉 [Soft UI Design PRO Django](https://django-soft-design-enh.appseed-srv1.com) - LIVE Demo
- 👉 [Complete documentation](https://docs.appseed.us/products/django-apps/soft-ui-design-pro) - `Learn how to use and update the product`
  
<br />

> Features

- `Up-to-date dependencies`
- Database: `sqlite`
- UI-Ready app, Django Native ORM
- **Authentication**
  - `Session-Based authentication`
  - `Social Login` (optional) for **Github** & **Twitter**
- **User profiles**
  - `Extended profile`, `Self-Deletion`

<br />

![Soft UI Design PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png)

<br />

## ✨ Start the app in Docker

> **Step 1** - Download the [code](https://appseed.us/product/soft-ui-design-pro/django/) and unzip the sources (requires a `purchase`). 

```bash
$ # Get the code
$ unzip django-soft-ui-design-enh.zip
$ cd django-soft-ui-design-enh
```

<br />


> **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

<br />

## ✨ How to use it

> Download the [code](https://appseed.us/product/soft-ui-design-pro/django/) and unzip the sources (requires a `purchase`). 

```bash
$ # Get the code
$ unzip django-soft-ui-design-enh.zip
$ cd django-soft-ui-design-enh
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
// OR with https
$ python manage.py runsslserver 
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
// OR with https
$ python manage.py runsslserver 
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## ✨ Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- page-404.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

---
Soft UI Design PRO Django - Seed project generated by **[AppSeed Generator](https://appseed.us/generator/)**.
