# Blog-Django

A Django blog project. This README explains **how a page shows up in the browser**
and gives you a repeatable recipe for adding new pages.

---

## The big idea: every page needs 3 things

To make ONE page appear at a URL, you connect three pieces:

| # | Piece        | File                          | Its job                                        |
|---|--------------|-------------------------------|------------------------------------------------|
| 1 | **Template** | `templates/pages/NAME.html`   | The HTML — what the page *looks like*.         |
| 2 | **View**     | `pages/views.py`              | A Python function that grabs the template.     |
| 3 | **URL**      | `pages/urls.py`               | The web address that points to the view.       |

**How a request flows:**

```
Browser asks for /about/
      ↓
config/urls.py  →  hands "" (everything) to pages/urls.py
      ↓
pages/urls.py   →  matches "about/" and calls the about view
      ↓
pages/views.py  →  render(request, "pages/about.html")
      ↓
Browser shows about.html
```

---

## Project structure (the important parts)

```
Blog/
├── config/              ← project settings (the "control room")
│   ├── settings.py      ← lists installed apps + where templates live
│   └── urls.py          ← the MAIN url map; sends "" to pages/urls.py
├── pages/               ← our app that holds page logic
│   ├── views.py         ← the view FUNCTIONS (home, about, ...)
│   └── urls.py          ← the URL routes for this app
├── templates/
│   └── pages/           ← the actual HTML files
│       ├── home.html
│       └── about.html
├── static/              ← CSS, JS, images
└── manage.py            ← the command you run Django with
```

Two settings make this work (already done):
- `config/settings.py` → `INSTALLED_APPS` contains `'pages'`
- `config/settings.py` → `TEMPLATES['DIRS']` includes the `templates` folder
- `config/urls.py` → `path("", include("pages.urls"))` hands routing to the app

---

## ✅ Recipe: how to add a NEW page (do this every time)

Say you want a **Contact** page at `/contact/`. Three steps, one per piece:

### Step 1 — Make the template (the HTML)
Create `templates/pages/contact.html` with your HTML.

### Step 2 — Make the view (the Python that serves it)
In `pages/views.py`, add a function:

```python
def contact(request):
    return render(request, "pages/contact.html")
```

### Step 3 — Make the URL (the address)
In `pages/urls.py`, add a line inside `urlpatterns`:

```python
path("contact/", views.contact, name="contact"),
```

### Step 4 — See it
Start the server and open the address:

```bash
python manage.py runserver
```
Then visit **http://127.0.0.1:8000/contact/**

That's the whole loop. Template → View → URL → run server → visit. Repeat for
every page.

---

## Linking between pages

Inside any template, link using the URL's `name=` (not a hard-coded path):

```html
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'about' %}">About</a>
```

---

## Running the project

```bash
# 1. Activate the virtual environment (once per terminal session)
source venv/bin/activate

# 2. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser. Stop the server with `Ctrl + C`.

Current pages:
- `/`         → Home  (`pages/views.py` → `home`  → `templates/pages/home.html`)
- `/about/`   → About (`pages/views.py` → `about` → `templates/pages/about.html`)
