# Blog-Django

A Django blog built for FSDI 112. Visitors can read posts, sign up, and log in;
logged-in users can write posts and edit or delete their own.

## Features

- Static pages: Home, About, Contact
- Blog posts with full CRUD (list, detail, create, edit, delete)
- User accounts: sign up (unique email required), login, logout, password change and reset
- Permission rules on posts (see [Access rules](#access-rules))
- Custom 403 and 404 pages
- Password reset emails print to the terminal (no mail server needed)

## Tech stack

- Python 3 / Django 6.1.1 (see `requirements.txt`)
- SQLite (`db.sqlite3`)
- Django class-based views and templates

## Getting started

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create the database tables
python manage.py migrate

# 4. (Optional) Create an admin user
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/**. Stop the server with `Ctrl + C`.

## URL map

| URL                      | Name              | View                  | Who can access           |
|--------------------------|-------------------|-----------------------|--------------------------|
| `/`                      | `home`            | `HomePageView`        | Everyone                 |
| `/about/`                | `about`           | `AboutPageView`       | Everyone                 |
| `/contact/`              | `contact`         | `contact_page`        | Everyone                 |
| `/list/`                 | `post_list`       | `PostListView`        | Everyone                 |
| `/detail/<pk>/`          | `post_detail`     | `PostDetailView`      | Superusers only          |
| `/new/`                  | `post_new`        | `PostCreateView`      | Logged-in users          |
| `/edit/<pk>/`            | `post_edit`       | `PostUpdateView`      | The post's author        |
| `/delete/<pk>/`          | `post_delete`     | `PostDeleteView`      | The post's author        |
| `/accounts/signup/`      | `signup`          | `SignUpView`          | Everyone                 |
| `/accounts/logout/`      | `logout`          | `LogoutGetView`       | Everyone                 |
| `/accounts/login/` etc.  | `login`, password views | `django.contrib.auth` | Everyone           |
| `/admin/`                | —                 | Django admin          | Staff                    |

## Access rules

- **Create** a post: any logged-in user; the author is set automatically.
- **Edit / delete** a post: only its author.
- **Detail** page: logged-in superusers only.
- Anyone not allowed gets the custom `403.html`; logged-out users are sent to the login page.
- After login, users are redirected to the home page.

## Project structure

```
Blog/
├── config/                  Project settings, root URL map, custom email backend
├── pages/                   Home / About / Contact views and URLs
├── posts/                   Post and Status models, CRUD views and URLs
├── accounts/                Sign-up form/view and GET-friendly logout
├── templates/
│   ├── base.html, navbar.html, 403.html, 404.html
│   ├── pagesTemplates/      home, about, contact
│   ├── postsTemplates/      list, detail, new, edit, delete
│   └── registration/        login, signup, password change/reset pages
├── static/                  CSS/, js/, images/
├── manage.py
└── requirements.txt
```

## Data models (`posts/models.py`)

- **Post**: `title`, `subtitle`, `body`, `created_on` (auto), `author` (FK to `User`)
- **Status**: `name` (unique), `description`

## How a page is wired up

Every page needs three pieces: a template, a view, and a URL.

```
Browser requests /about/
   → config/urls.py        includes pages.urls
   → pages/urls.py         matches "about/" → AboutPageView
   → pages/views.py        renders pagesTemplates/about.html
```

To add a new page:

1. Create the template in `templates/<app>Templates/`.
2. Add a view in the app's `views.py`.
3. Add a `path(...)` with a `name=` in the app's `urls.py`.

Link to pages by name, not hard-coded paths:

```html
<a href="{% url 'post_list' %}">Posts</a>
```

## Notes

- `LOGIN_REDIRECT_URL = 'home'` and `LOGIN_URL = 'login'` are set in `config/settings.py`.
- Email uses `config.mail.PlainConsoleEmailBackend`, so password reset emails appear in the server console.
- See `README_2.md` for the steps used to bootstrap a Django project from scratch.
