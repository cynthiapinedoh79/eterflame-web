# 🔥 ETERFLAME — Django Web Application

**Live Site:** https://eterflame-web-ab680e12c17d.herokuapp.com/
**GitHub:** https://github.com/cynthiapinedoh79/eterflame-web

Eterflame is a dual-brand creative platform combining **Eterflame Works** (Creative & Digital Production studio) and **Aythnyk** (Poetry & Music by Cynthia Pinedo). Built with Django, it serves as both a professional services platform and a literary/music experience for Spanish-language poetry lovers.

---

## 🧩 Badges

![GitHub repo size](https://img.shields.io/github/repo-size/cynthiapinedoh79/eterflame-web)
![GitHub last commit](https://img.shields.io/github/last-commit/cynthiapinedoh79/eterflame-web)
[![View Demo](https://img.shields.io/badge/View-Demo-brightgreen)](https://eterflame-web-ab680e12c17d.herokuapp.com/)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![Heroku](https://img.shields.io/badge/Heroku-Deploy-purple)
![SendGrid](https://img.shields.io/badge/SendGrid-Email-blue)
![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-orange)

---

## 📋 Table of Contents

- [🧾 Project Overview](#-project-overview)
- [🔗 Live Demo](#-live-demo)
- [📱 Am I Responsive?](#-am-i-responsive)
- [🖼️ Screenshots](#️-screenshots)
- [🎯 UX](#-ux)
- [🧑‍💼 User Stories](#-user-stories)
- [🎨 Design Choices](#-design-choices)
- [🏛️ Architecture](#️-architecture-django-mvt)
- [🛠️ Technologies & Tools](#️-technologies--tools)
- [📦 Project Setup](#-project-setup)
- [⚙️ Environment Variables](#️-environment-variables)
- [🗂️ Project Structure](#️-project-structure)
- [✅ Testing & Validators](#-testing--validators)
- [🐞 Bugs and Issues Log](#-bugs-and-issues-log)
- [📥 Deployment](#-deployment)
- [🌿 Branch Workflow](#-branch-workflow)
- [🙏 Credits & Acknowledgements](#-credits--acknowledgements)

---

## 🧾 Project Overview

Eterflame is built around two complementary brands:

**Eterflame Works** — A creative & digital production studio offering:
- Works Home — services overview
- EF Design — web design & development
- EF Media — media production
- EF Studio — creative studio
- Works Resources (`/works/resources/`) — B2B affiliate tools
- Contact — project enquiry form
- About — team & collaborate form

**Aythnyk** — A Spanish-language poetry & music experience featuring:
- Poems — curated collections with ES/EN toggle, favorites, PDF sales
- Blog — creative writing & reflections
- Shop (`/shop/`) — digital products via Gumroad
- Sonic — songs with YouTube, streaming & reels
- Tools (`/aythnyk/tools/`) — ElevenLabs, DistroKid, Canva and more
- AI Chat — AI assistant
- Favorites — authenticated users saved poems

**Core Technologies:**
1. **Django 5.2 (Python 3.11)** — Full-stack web framework
2. **PostgreSQL** — Production database (Heroku)
3. **SendGrid HTTP API** — Email delivery (not SMTP — Heroku blocks SMTP)
4. **Cloudinary** — Media storage
5. **WeasyPrint** — PDF generation
6. **Bootstrap 5** — Responsive frontend
7. **Django Allauth** — Auth with Google & Facebook OAuth
8. **Google Analytics GA4** — Traffic analytics

##### Back to [top](#-table-of-contents)

---

## 🔗 Live Demo

**Live Site:** https://eterflame-web-ab680e12c17d.herokuapp.com/
**Admin Panel:** https://eterflame-web-ab680e12c17d.herokuapp.com/admin/

##### Back to [top](#-table-of-contents)

---

## 📱 Am I Responsive?

All pages are designed with **Mobile-First Responsive Design** across all screen sizes.

| Page | Screenshot |
|---|---|
| Eterflame Works Home | *Add screenshot* |
| Aythnyk Home | *Add screenshot* |
| Poem Detail | *Add screenshot* |
| Song Detail | *Add screenshot* |
| EF Design | *Add screenshot* |
| Shop | *Add screenshot* |
| Blog | *Add screenshot* |
| About | *Add screenshot* |

##### Back to [top](#-table-of-contents)

---

## 🖼️ Screenshots

### Eterflame Works
<details>
<summary>View Works screenshots</summary>

#### Works Home
![Works Home](static/images/readme/screenshots/works_home.png)

#### EF Design
![EF Design](static/images/readme/screenshots/ef_design.png)

#### EF Media
![EF Media](static/images/readme/screenshots/ef_media.png)

#### EF Studio
![EF Studio](static/images/readme/screenshots/ef_studio.png)

#### Works Resources (`/works/resources/`)
![Works Resources](static/images/readme/screenshots/works_resources.png)

#### Contact Form
![Contact](static/images/readme/screenshots/contact.png)

</details>

### Aythnyk — Poetry
<details>
<summary>View Poetry screenshots</summary>

#### Poem List
![Poem List](static/images/readme/screenshots/poem_list.png)

#### Poem Detail (Pergamino)
![Poem Detail](static/images/readme/screenshots/poem_detail.png)

#### Poem Detail — Mobile
![Poem Detail Mobile](static/images/readme/screenshots/poem_detail_mobile.png)

#### Favorites
![Favorites](static/images/readme/screenshots/favorites.png)

</details>

### Aythnyk — Sonic (Songs)
<details>
<summary>View Songs screenshots</summary>

#### Song List
![Song List](static/images/readme/screenshots/song_list.png)

#### Song Detail
![Song Detail](static/images/readme/screenshots/song_detail.png)

</details>

### Aythnyk — Shop
<details>
<summary>View Shop screenshots</summary>

#### Shop Home
![Shop](static/images/readme/screenshots/shop.png)

#### PDF Purchase Modal
![Shop Modal](static/images/readme/screenshots/shop_modal.png)

</details>

### Aythnyk — Tools (`/aythnyk/tools/`)
<details>
<summary>View Tools screenshots</summary>

*Tools used by Aythnyk — ElevenLabs, DistroKid, Canva and more*

#### Aythnyk Tools
![Aythnyk Tools](static/images/readme/screenshots/aythnyk_tools.png)

</details>

### Aythnyk — Blog
<details>
<summary>View Blog screenshots</summary>

#### Blog List
![Blog](static/images/readme/screenshots/blog.png)

#### Blog Post Detail
![Blog Post](static/images/readme/screenshots/blog_detail.png)

</details>

### Aythnyk — About
<details>
<summary>View About screenshots</summary>

#### About Page
![About](static/images/readme/screenshots/about.png)

#### Collaborate Form
![Collaborate](static/images/readme/screenshots/collaborate.png)

</details>

### AI Chat
<details>
<summary>View AI Chat screenshots</summary>

#### AI Chat Assistant
![AI Chat](static/images/readme/screenshots/ai_chat.png)

</details>

### Aythnyk — Tools & Resources
<details>
<summary>View Tools screenshots</summary>

#### Aythnyk Tools (`/aythnyk/tools/`)
*ElevenLabs, DistroKid, Canva — herramientas que usa Aythnyk*
![Tools](static/images/readme/screenshots/aythnyk_tools.png)

#### Works Resources (`/works/resources/`)
*Affiliate links for B2B tools*
![Resources](static/images/readme/screenshots/works_resources.png)

</details>

### AI Chat
<details>
<summary>View AI Chat screenshots</summary>

#### AI Chat Assistant
![AI Chat](static/images/readme/screenshots/ai_chat.png)

</details>

### Auth Flow
<details>
<summary>View Auth screenshots</summary>

#### Login
![Login](static/images/readme/screenshots/login.png)

#### Register
![Register](static/images/readme/screenshots/register.png)

#### Google OAuth
![Google Login](static/images/readme/screenshots/login_google.png)

#### Facebook OAuth
![Facebook Login](static/images/readme/screenshots/login_facebook.png)

</details>

##### Back to [top](#-table-of-contents)

---

## 🎯 UX

### Target Audience

**Two primary audiences:**

1. **Potential clients of Eterflame Works** — Businesses and creatives looking for web design, media, and digital production services.
2. **Spanish-language poetry & music lovers** — Readers and listeners who follow Aythnyk's creative work.

### Core UX Goals

1. **Clear brand separation** — Works (professional, gold/dark) vs Aythnyk (editorial, crimson/dark)
2. **Prioritize readability** — Poetry rendered with intention, premium pergamino design
3. **Protect premium content** — Poem detail pages are `noindex` — poems sell as PDFs
4. **Encourage social sharing** — Songs have full og:image support for social media
5. **Seamless contact** — Real emails via SendGrid from both contact forms

### User Goals by Frequency

#### First-Time Visitor Goals
1. Understand the dual-brand platform (Works + Aythnyk)
2. Explore poetry and music content
3. Find contact/collaboration path
4. Be visually engaged by the dark editorial design

#### Returning Visitor Goals
1. Discover new poems and songs
2. Login to manage favorites
3. Purchase poem PDFs

#### Frequent User Goals
1. Manage favorite poems list
2. Follow new collections and songs
3. Share song links on social media

##### Back to [top](#-table-of-contents)

---

## 🧑‍💼 User Stories

### Core User Stories

| User Story | Priority | Status |
|---|---|---|
| As a visitor, I can explore Eterflame Works services | Must-Have | ✅ Done |
| As a visitor, I can browse and read poems | Must-Have | ✅ Done |
| As a visitor, I can listen to songs and see streaming links | Must-Have | ✅ Done |
| As a visitor, I can submit a project enquiry via contact form | Must-Have | ✅ Done |
| As a visitor, I can submit a collaboration request | Must-Have | ✅ Done |
| As a user, I can register, login, and logout | Must-Have | ✅ Done |
| As a user, I can login with Google or Facebook | Should-Have | ✅ Done |
| As a logged-in user, I can favorite poems | Should-Have | ✅ Done |
| As a visitor, I can toggle poems between ES/EN | Should-Have | ✅ Done |
| As a visitor, I can purchase poem PDFs | Could-Have | ✅ Done |
| As a visitor, I can explore the digital shop | Could-Have | ✅ Done |
| As a visitor, I can see Aythnyk's creative tools | Could-Have | ✅ Done |
| As a visitor, I can explore Works affiliate resources | Could-Have | ✅ Done |
| As a visitor, I can use the AI chat assistant | Could-Have | ✅ Done |
| As an admin, I can generate PDFs via staff tool | Must-Have | ✅ Done |
| As a visitor, I can read the blog | Should-Have | ✅ Done |
| As a visitor, I can view the about/team page | Should-Have | ✅ Done |

### Testing User Stories

#### Works Contact Form
- **AC1** User fills name, email, service, description and submits
- **AC2** Email arrives at `studio@eterflame.com` via SendGrid
- **AC3** Success message displays on the page
- **Result** ✅ Passed

#### Collaborate Form (About)
- **AC1** User fills name, email, message and submits
- **AC2** Request saved to database (visible in admin)
- **AC3** Email notification sent to `studio@eterflame.com`
- **Result** ✅ Passed

#### Poem Favorites
- **AC1** Authenticated user sees heart icon on poem detail
- **AC2** Click toggles favorite state
- **AC3** Poem appears in `/aythnyk/poems/favorites/`
- **Result** ✅ Passed

#### PDF Purchase Flow
- **AC1** User sees "Descargar PDF" button on song/poem panel
- **AC2** Modal opens with price and buy link
- **AC3** Gumroad link opens in new tab
- **Result** ✅ Passed

### Features Left to Implement

| Feature | Priority | Status |
|---|---|---|
| More Printful products (posters, t-shirts) | Could-Have | Backlog |
| PDF improvements — page 2+ breathing room | Could-Have | Backlog |
| EF Media / EF Studio full content | Should-Have | Backlog |
| Google Analytics data visible | Should-Have | In Progress (24-48hr wait) |

##### Back to [top](#-table-of-contents)

---

## 🎨 Design Choices

### Brand Identity

Eterflame uses two distinct visual identities within one platform:

| Brand | Primary Color | Secondary | Background |
|---|---|---|---|
| Eterflame Works | Gold `#c49a40` | Dark `#0a0804` | Dark editorial |
| Aythnyk | Crimson `#c8102e` | Gold `#c49a40` | Dark `#0a0804` |

### Typography

| Font | Usage |
|---|---|
| **Cormorant Garamond** | Display / Poetry titles / Song titles |
| **DM Sans** | Body / UI / Labels |
| **Courier Prime** | Monospace / Series tags / Footer |

### Color Palette

<details>
<summary>View color palette details</summary>

- **Crimson** `#c8102e` — Primary accent for Aythnyk, hover states, active elements
- **Gold** `#c49a40` — Secondary accent, poem titles, Eterflame Works CTAs
- **Dark** `#0a0804` — Background base
- **Cream** `#f5e6c8` — Primary text on dark
- **Muted** `#6b5f45` — Secondary text, subtitles

</details>

### SEO Strategy

| Page | SEO Treatment |
|---|---|
| Poem detail | `noindex, nofollow` — protected premium content |
| Song detail | Full `og:title`, `og:description`, `og:image`, `og:type` |
| Works / Aythnyk home | Indexable |
| Blog posts | Indexable |

##### Back to [top](#-table-of-contents)

---

## 🏛️ Architecture (Django MVT)

### App Responsibilities

**🏢 Eterflame Works**

| App | Purpose |
|---|---|
| `works` | Works home, contact form, resources (`/works/resources/`) |
| `design_app` | EF Design division |
| `media_app` | EF Media division |
| `studio_app` | EF Studio division |

**🔥 Aythnyk**

| App | Purpose |
|---|---|
| `aythnyk` | Aythnyk home, navigation hub |
| `poetry` | Poems, collections, favorites, PDF generator, tools (`/aythnyk/tools/`) |
| `songs` | Sonic — songs, streaming, reels |
| `blog` | Blog posts |
| `shop` | Digital shop (Gumroad) |
| `about` | About page, collaborate form |
| `chat` | AI chat assistant |

**⚙️ Shared**

| App | Purpose |
|---|---|
| `core` | Shared utilities, OAuth adapters |
| `facebook_integration` | Facebook OAuth helpers |

### URL Map

**🏢 Eterflame Works**

| Path | App | Public? |
|---|---|---|
| `/` | works | ✅ Public |
| `/works/design/` | design_app | ✅ Public |
| `/works/media/` | media_app | ✅ Public |
| `/works/studio/` | studio_app | ✅ Public |
| `/works/resources/` | works | ✅ Public |
| `/contact/` | works | ✅ Public |
| `/about/` | about | ✅ Public |

**🔥 Aythnyk**

| Path | App | Public? |
|---|---|---|
| `/aythnyk/` | aythnyk | ✅ Public |
| `/aythnyk/poems/` | poetry | ✅ Public |
| `/aythnyk/poems/<slug>/` | poetry | ✅ Public |
| `/aythnyk/poems/favorites/` | poetry | 🔒 Auth |
| `/aythnyk/songs/` | songs | ✅ Public |
| `/aythnyk/songs/<slug>/` | songs | ✅ Public |
| `/blog/` | blog | ✅ Public |
| `/shop/` | shop | ✅ Public |
| `/aythnyk/tools/` | poetry | ✅ Public |
| `/aythnyk/pdf-tool/` | poetry | 🔒 Staff only |

**⚙️ System**

| Path | App | Public? |
|---|---|---|
| `/admin/` | Django admin | 🔒 Admin |
| `/accounts/` | allauth | ✅ Public |

### CRUD Map

| Model | Create | Read | Update | Delete |
|---|---|---|---|---|
| Poem | ✅ Admin | ✅ Public | ✅ Admin | ✅ Admin |
| Song | ✅ Admin | ✅ Public | ✅ Admin | ✅ Admin |
| Blog Post | ✅ Admin | ✅ Public | ✅ Admin | ✅ Admin |
| Favorites | ✅ User | ✅ User | ❌ N/A | ✅ User |
| CollaborateRequest | ✅ Public | ✅ Admin | ❌ N/A | ✅ Admin |
| Product (Shop) | ✅ Admin | ✅ Public | ✅ Admin | ✅ Admin |

### Data Models (ERD)

#### Poem Model (poetry app)

| Field | Type | Notes |
|---|---|---|
| `slug` | SlugField | Unique, URL-safe |
| `author` | ForeignKey → Author | CASCADE |
| `collection` | ForeignKey → Collection | SET_NULL |
| `favorites` | ManyToManyField → User | related_name='favorite_poems' |
| `title_es` / `title_en` | CharField | Bilingual |
| `body_es` / `body_en` | TextField | Bilingual |
| `featured_image` | CloudinaryField | |

#### Song Model (songs app)

| Field | Type | Notes |
|---|---|---|
| `slug` | SlugField | Unique |
| `poem` | ForeignKey → Poem | SET_NULL |
| `series` | CharField | Emotional/Lyric/Dramatic/Cinematic |
| `spotify_url` | URLField | |
| `youtube_url` | URLField | |
| `pdf_price` | DecimalField | |
| `pdf_buy_url` | URLField | Gumroad link |
| `reel_thumbnail` | CloudinaryField | For og:image |

#### CollaborateRequest Model (about app)

| Field | Type | Notes |
|---|---|---|
| `name` | CharField | |
| `email` | EmailField | |
| `message` | TextField | |
| `read` | BooleanField | Default False — admin tracking |

### Forms & Validation

| Form | Model | Key Fields |
|---|---|---|
| Contact form (Works) | None (email only) | name, email, service, budget, timeline, description |
| CollaborateForm | CollaborateRequest | name, email, message |
| Login / Register | User (allauth) | email, username, password |

##### Back to [top](#-table-of-contents)

---

## 🛠️ Technologies & Tools

### Languages

| Language | Role |
|---|---|
| **Python 3.11** | Backend logic, views, models |
| **HTML5** | Templates structure |
| **CSS3** | Custom design system |
| **JavaScript** | Quote banner, PDF modal, poem toggle |

### Frameworks & Libraries

| Tool | Purpose |
|---|---|
| **Django 5.2** | Web framework |
| **Bootstrap 5** | Responsive grid & components |
| **django-allauth** | Auth + Google/Facebook OAuth |
| **django-sendgrid-v5** | Email via SendGrid HTTP API |
| **WeasyPrint** | PDF generation |
| **django-summernote** | Rich text editor |
| **django-crispy-forms** | Form styling |
| **Cloudinary** | Media storage |
| **WhiteNoise** | Static files on Heroku |
| **Gunicorn** | WSGI server |
| **dj-database-url** | Database URL parsing |
| **python-dotenv** | Local env variables |

### Services

| Service | Purpose |
|---|---|
| **Heroku** | Deployment & hosting |
| **PostgreSQL** | Production database |
| **Cloudinary** | Image & media hosting |
| **SendGrid** | Email delivery (HTTP API) |
| **Gumroad** | Digital product sales |
| **Printful** | Print-on-demand products |
| **Google Analytics GA4** | Traffic analytics (G-QNBJ6BH1ZK) |
| **Google OAuth** | Social login |
| **Facebook OAuth** | Social login |

### Development Tools

| Tool | Purpose |
|---|---|
| **Gitpod** | Cloud IDE |
| **VS Code** | Local IDE |
| **GitHub** | Version control |
| **Claude Code** | AI coding assistant |

##### Back to [top](#-table-of-contents)

---

## 📦 Project Setup

```bash
# Clone the repository
git clone https://github.com/cynthiapinedoh79/eterflame-web.git
cd eterflame-web

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file (see Environment Variables section)

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

##### Back to [top](#-table-of-contents)

---

## ⚙️ Environment Variables

### `.env` file (local only — never commit)

```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgresql://...
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
SENDGRID_API_KEY=SG.xxx
CONTACT_EMAIL=studio@eterflame.com
DEFAULT_FROM_EMAIL=studio@eterflame.com
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret
DJANGO_SETTINGS_MODULE=eterflame.settings
```

### Heroku Config Vars

| Variable | Purpose | Required |
|---|---|---|
| `SECRET_KEY` | Django security | ✅ Required |
| `DEBUG` | Set `False` in production | ✅ Required |
| `DATABASE_URL` | PostgreSQL connection | ✅ Required |
| `CLOUDINARY_URL` | Media storage | ✅ Required |
| `SENDGRID_API_KEY` | Email delivery | ✅ Required |
| `CONTACT_EMAIL` | Email recipient | ✅ Required |
| `DEFAULT_FROM_EMAIL` | Email sender | ✅ Required |
| `GOOGLE_CLIENT_ID` | Google OAuth | Optional |
| `GOOGLE_CLIENT_SECRET` | Google OAuth | Optional |
| `FACEBOOK_APP_ID` | Facebook OAuth | Optional |
| `FACEBOOK_APP_SECRET` | Facebook OAuth | Optional |

##### Back to [top](#-table-of-contents)

---

## 🗂️ Project Structure

<details>
<summary>View full project structure</summary>

```text
eterflame-web/
│
├── eterflame/               # Django settings package
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── works/                   # Eterflame Works home + contact
├── design_app/              # EF Design division
├── media_app/               # EF Media division
├── studio_app/              # EF Studio division
│
├── aythnyk/                 # Aythnyk home hub
├── poetry/                  # Poems, collections, PDF, favorites
├── songs/                   # Songs, streaming, reels
├── blog/                    # Blog posts
├── shop/                    # Digital shop (Gumroad)
├── about/                   # About page + collaborate form
├── core/                    # Shared utilities + OAuth adapters
├── chat/                    # AI chat feature
├── facebook_integration/    # Facebook OAuth helpers
│
├── static/
│   ├── css/
│   │   ├── base.css         # Global styles + navbar
│   │   ├── aythnyk.css      # Aythnyk home
│   │   ├── poetry.css       # Poems list + detail
│   │   ├── songs.css        # Songs + poem-with-panel grid
│   │   ├── design.css       # EF Design page
│   │   ├── works.css        # Works home
│   │   ├── about.css        # About page
│   │   ├── blog.css         # Blog
│   │   └── shop.css         # Shop
│   ├── js/
│   │   ├── script.js        # Global JS
│   │   ├── chat.js          # AI chat
│   │   ├── quote_banner.js  # Sliding quote banner
│   │   └── poem_toggle.js   # ES/EN poem toggle
│   └── images/
│
├── staticfiles/             # Collected static (Heroku deployment)
│
├── templates/
│   ├── base.html            # Global base — navbar + footer + GA4
│   ├── account/             # Custom allauth templates
│   ├── allauth/             # Allauth element overrides
│   ├── works/
│   ├── poetry/
│   ├── songs/
│   ├── blog/
│   ├── about/
│   └── shop/
│
├── requirements.txt
├── Procfile                 # web: gunicorn eterflame.wsgi
├── runtime.txt
└── .env                     # Local only — in .gitignore
```

</details>

##### Back to [top](#-table-of-contents)

---

## ✅ Testing & Validators

### Browser & Device Testing

| Browser / Device | Status |
|---|---|
| Chrome Desktop | ✅ Passed |
| Firefox Desktop | ✅ Passed |
| Safari Desktop | ✅ Passed |
| Mobile (iPhone) | ✅ Passed |
| Mobile (Android) | ✅ Passed |
| Tablet | ✅ Passed |

### W3C HTML Validator

<details>
<summary>View HTML validation results</summary>

| Page | Result |
|---|---|
| Works Home `/` | ✅ Passed |
| Aythnyk Home `/aythnyk/` | ✅ Passed |
| Poem List | ✅ Passed |
| Poem Detail | ✅ Passed |
| Song Detail | ✅ Passed |
| About | ✅ Passed |
| Blog | ✅ Passed |

*Add W3C validator screenshots here*

</details>

### W3C CSS Validator

<details>
<summary>View CSS validation results</summary>

| File | Result |
|---|---|
| base.css | ✅ Passed |
| poetry.css | ✅ Passed |
| songs.css | ✅ Passed |
| aythnyk.css | ✅ Passed |
| works.css | ✅ Passed |

*Add W3C CSS validator screenshots here*

</details>

### Python — PEP8 / pycodestyle

<details>
<summary>View Python validation results</summary>

| File | Result |
|---|---|
| eterflame/settings.py | ✅ Passed |
| works/views.py | ✅ Passed |
| poetry/views.py | ✅ Passed |
| songs/views.py | ✅ Passed |
| about/views.py | ✅ Passed |
| about/models.py | ✅ Passed |
| about/forms.py | ✅ Passed |

*Add pep8ci screenshots here*

</details>

### SEO & Meta Tags

| Page | Test | Result |
|---|---|---|
| Poem detail | `noindex, nofollow` present in `<head>` | ✅ Verified |
| Song detail | `og:title`, `og:description`, `og:type`, `og:url` | ✅ Verified |
| All pages | GA4 tag `G-QNBJ6BH1ZK` present | ✅ Verified |

### Email Testing

| Form | Email received at | Result |
|---|---|---|
| Works contact form | `studio@eterflame.com` | ✅ Working |
| About collaborate form | `studio@eterflame.com` | ✅ Working |

### Lighthouse

<details>
<summary>View Lighthouse results</summary>

*Add Lighthouse screenshots here for:*
- Works Home
- Aythnyk Home
- Poem List
- Poem Detail
- Song Detail
- About

</details>

##### Back to [top](#-table-of-contents)

---

## 🐞 Bugs and Issues Log

### Solved Issues

| Problem | Cause | Fix |
|---|---|---|
| Email not sending on Heroku | Heroku blocks SMTP ports 25/465/587 on all dynos | Switched to **SendGrid HTTP API** (`django-sendgrid-v5`) — uses HTTPS not SMTP |
| SendGrid domain verification failing | Wrong CNAME record (`em2147` vs correct `em9736`) | Updated DNS in Squarespace with correct CNAME from SendGrid |
| Poem detail `noindex` not rendering | `{% block extra_head %}` missing in `base.html` | Added `{% block extra_head %}{% endblock %}` to `base.html` before `</head>` |
| Poem with panel offset on tablet 481-960px | `.poem-main-container { margin: 0 auto }` conflicting with tablet media query | Set `margin: 0 !important` in `@media (max-width: 960px)` |
| EF Design watermark logo not visible | CSS used hardcoded `/static/` URL — fails on Heroku | Moved URL to template `style="background-image: url('{% static ... %}')"` |
| Navbar active class inconsistent across apps | Each nav item used different path detection | Standardized to `in request.path` for Works, Aythnyk, About, Contact |
| Allauth manage pages had no navbar | `base_manage.html` extended allauth's own stripped base | Made `base_manage.html` extend site `base.html` |
| About collaborate form returning 500 | `fail_silently=False` + SMTP blocked on Heroku | Switched to SendGrid HTTP API |
| Merge conflict in requirements.txt | Duplicate `weasyprint` and `sendgrid` entries from two branches | Cleaned to one versioned entry per package |
| SSH push failing in Gitpod | SSH agent resets on workspace restart | Run `eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519` each session |
| Heroku app name confusion | Two URLs: old `eterfalame-web-3348815acb0e` and new `eterflame-web-ab680e12c17d` | Confirmed correct app name is `eterflame-web` |

### Known Issues

| Issue | Status |
|---|---|
| GA4 "tag not detected" warning in Google Analytics setup | Cosmetic — analytics works fine, Google needs live traffic to detect automatically |

##### Back to [top](#-table-of-contents)

---

## 📥 Deployment

### ⚙️ Procfile

```
web: gunicorn eterflame.wsgi
```

### Heroku Deployment

```bash
# 1. Create app
heroku create eterflame-web

# 2. Add PostgreSQL
# Heroku Dashboard → Resources → Heroku Postgres

# 3. Set Config Vars (see Environment Variables)
heroku config:set SECRET_KEY=xxx --app eterflame-web
heroku config:set SENDGRID_API_KEY=SG.xxx --app eterflame-web
# ... etc

# 4. Push
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
git push origin main

# 5. Run migrations
heroku run python manage.py migrate --app eterflame-web

# 6. Create superuser
heroku run python manage.py createsuperuser --app eterflame-web

# 7. Collect static
heroku run python manage.py collectstatic --noinput --app eterflame-web

# 8. Check logs
heroku logs --tail --app eterflame-web
```

### ⚠️ Critical — Email on Heroku

> Heroku blocks outbound SMTP connections on ports 25, 465, and 587 on all dynos.
> **Never use `smtp.EmailBackend` on Heroku — it will always fail.**
> Use SendGrid HTTP API instead:

```python
# settings.py — correct setup for Heroku
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = 'studio@eterflame.com'
CONTACT_EMAIL = 'studio@eterflame.com'
```

### 📧 SendGrid DNS Setup (Squarespace)

Domain `eterflame.com` verified with these DNS records:

| Type | Name | Value |
|---|---|---|
| CNAME | `em9736` | `u106481333.wl084.sendgrid.net` |
| CNAME | `s1._domainkey` | `s1.domainkey.u106481333.wl084.sendgrid.net` |
| CNAME | `s2._domainkey` | `s2.domainkey.u106481333.wl084.sendgrid.net` |
| TXT | `_dmarc` | `v=DMARC1; p=none;` |

### 📄 PDF Workflow (Staff Only)

1. Login → `/aythnyk/pdf-tool/`
2. Click "Generar PDF" → new tab opens
3. CMD+S → save file
4. Upload to Gumroad → copy link
5. Admin → Songs → set `pdf_buy_url` + `pdf_price`

##### Back to [top](#-table-of-contents)

---

## 🌿 Branch Workflow

```bash
# Start new feature
git checkout main && git pull origin main
git checkout -b feature/my-feature

# Work + commit
git add -A
git commit -m "feat: description"
git push origin feature/my-feature

# Merge to main
git checkout main
git merge feature/my-feature
git push origin main

# Clean up
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

### Naming Conventions

| Prefix | Use Case | Example |
|---|---|---|
| `feature/` | New features | `feature/blog-redesign` |
| `fix/` | Bug fixes | `fix/responsive-mobile` |
| `refactor/` | Code cleanup | `refactor/css-separation` |
| `chore/` | Maintenance | `chore/collectstatic` |
| `docs/` | Documentation only | `docs/update-readme` |

### SSH Push (required each Gitpod session)

```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
git push origin main
```

**Permanent fix** — add to `~/.bashrc`:
```bash
echo 'eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519 2>/dev/null' >> ~/.bashrc
```

##### Back to [top](#-table-of-contents)

---

## 🙏 Credits & Acknowledgements

- **Code Institute** — Learning materials and project foundation
- **Django Documentation** — Core reference
- **Heroku Documentation** — Deployment guidance
- **SendGrid Documentation** — Email setup
- **Cloudinary** — Media storage infrastructure
- **Bootstrap** — Frontend framework
- **Font Awesome** — Icons
- **Google Fonts** — Cormorant Garamond, DM Sans, Courier Prime
- **WeasyPrint** — PDF generation library
- **Claude Code** — AI coding assistant used throughout development
- **Mentor & Peer Feedback** — Continuous improvement
- **Slack & Discord Community** — Technical support and troubleshooting

---

*Eterflame © 2025 · All rights reserved*
*studio@eterflame.com · eterflame.com*

##### Back to [top](#-table-of-contents)
