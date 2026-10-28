# FrenchLessons 🇫🇷🚀

![CI/CD Pipeline](https://github.com/bohdanadamenko/Learn_French/actions/workflows/deploy.yml/badge.svg)

An interactive platform for learning French, featuring lessons, quizzes, and progress tracking. Now with fully automated deployment to PythonAnywhere!
<div align="center">

<img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/CKEditor-5-0287D0?style=for-the-badge&logo=ckeditor&logoColor=white" alt="CKEditor">
<img src="https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge" alt="License">

*Modern web application with multilingual support and responsive design*

[🚀 Demo](#quick-start) • [📖 Documentation](#project-structure) • [🛠️ Installation](#installation)

</div>

---

## ✨ Features

| 🌍 Multilingual | 🎨 Modern UI | 📱 Responsive |
|:---:|:---:|:---:|
| RU • UK • EN • FR | Glassmorphism & Dark Mode | Desktop & Mobile |

- 🎯 **French Lessons** with interactive quizzes
- 🔐 **Google Authentication** — seamless login with automatic account linking
- 📝 **CKEditor 5** for rich-text content in admin
- 🔐 **Jazzmin Admin** — beautiful and functional admin panel
- 🌙 **Dark/Light Theme** with smooth transitions
- 🔐 **Premium Auth System** — Login and Signup with Email & Google OAuth
- 👤 **Enhanced User Menu** — accessible profile dropdown for all users
- 🌍 **Elegant Language Selection** — refined active states and transitions
- 🔍 **Real-time Lesson Search**
- ⌨️ **Hotkeys** for quick navigation
- 🧪 **Comprehensive Testing** — 26+ tests covering models, views, and template tags
- 🚀 **Production Ready** — configured with WhiteNoise for static files

---

## 🔐 Registration & Authentication

The platform offers multiple ways to access the content:

- 📧 **Email Registration**: Standard signup with email and password.
- 🌐 **Google OAuth 2.0**: Quick and secure login via your Google account.
- 🔗 **Automatic Linking**: Existing accounts are automatically linked to Google if the email addresses match.

---

## 🚀 Quick Start

### Requirements

- 🐍 Python 3.10+
- 📦 pip

### Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/bohdanadamenko/Learn_French.git
cd FrenchLessons

# 2️⃣ Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure environment variables
cat > .env << EOF
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
EOF

# 5️⃣ Apply migrations
python manage.py migrate

# 6️⃣ Create a superuser
python manage.py createsuperuser

# 7️⃣ Run the server
# 7️⃣ Run the server
python manage.py runserver

# 8️⃣ Run tests
python manage.py test apps -v 2
```

🌐 Open: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
📦 FrenchLessons/
├── 📂 apps/                    # 🧩 Application Domains
│   ├── 📂 core/                # 🏠 Core logic (Views, Templates, Static)
│   ├── 📂 lessons/             # 🎓 Lessons Domain (Models, Selectors)
│   └── 📂 quizzes/             # ❓ Quizzes Domain (Models, Selectors)
├── 📂 learn_french/            # ⚙️ Django settings
├── 📂 locale/                  # 🌍 Global Translations
├── 📂 templates/               # 🎨 Global Template Overrides
├── 📂 utils/                   # 🛠️ Utility scripts
├── 📄 .env                     # 🔐 Secrets (not in git!)
├── 📄 requirements.txt         # 📦 Dependencies
└── 📄 manage.py                # 🚀 Django CLI
```

---

## 🛠️ Technologies

| Backend | Frontend | Database | Admin |
|:-------:|:--------:|:--------:|:-----:|
| <img src="https://img.shields.io/badge/-Django%205.2-092E20?logo=django" alt="Django"> | <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript"> | <img src="https://img.shields.io/badge/-SQLite-003B57?logo=sqlite" alt="SQLite"> | <img src="https://img.shields.io/badge/-Jazzmin-black" alt="Jazzmin"> |
| <img src="https://img.shields.io/badge/-Python%203.10-3776AB?logo=python&logoColor=white" alt="Python"> | <img src="https://img.shields.io/badge/-CSS3-1572B6?logo=css3" alt="CSS3"> | | <img src="https://img.shields.io/badge/-CKEditor%205-0287D0?logo=ckeditor" alt="CKEditor 5"> |

---

## ⌨️ Hotkeys

| Key | Action |
|:-------:|:---------|
| `→` | Next lesson |
| `←` | Previous lesson |
| `/` | Quick search |
| `Esc` | Close menu |

---

## 🔧 Content Management

To edit lessons, use **Django Admin**:

```
🔗 http://127.0.0.1:8000/admin
```

### Admin Features:

- ✏️ Edit lessons in 4 languages
- 📊 Manage questions and quizzes
- 🖼️ Upload images via CKEditor 5
- 🏷️ Language tabs for convenient editing

---

## 🔒 Security

| Measure | Description |
|:----:|:---------|
| 🔑 | `SECRET_KEY` stored in `.env` file |
| 🛡️ | `DEBUG=False` in production |
| 🌐 | `ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS` restricted |
| 🔐 | Passwords validated by Django |
| 🛡️ | CSRF Protection enabled |

---

## 🔄 CI/CD & Automation

The project uses **GitHub Actions** for a fully automated CI/CD pipeline.

- **CI/CD Pipeline**: A single workflow that runs tests and deploys to PythonAnywhere automatically if tests pass.
- **Error Tracking**: Integrated with **Sentry** for real-time production error monitoring.

[![CI/CD Pipeline](https://github.com/bohdanadamenko/Learn_French/actions/workflows/deploy.yml/badge.svg)](https://github.com/bohdanadamenko/Learn_French/actions/workflows/deploy.yml)

---

## 💾 Database Management

### Restore Database from Backup
If you need to restore the database content (lessons, quizzes) from the backup file:

```bash
# 1️⃣ Make sure you have the backup file
# It should be named 'backup_data.json' in the root directory

# 2️⃣ Load data into the database
python manage.py loaddata backup_data.json
```

---

## 📄 License

```
© 2025 FrenchLessons. All rights reserved.
Proprietary License - not for distribution
```

---

<div align="center">

### 👨‍💻 Development

**FrenchLessons Team** 🇧🇪

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)](https://github.com/bohdanadamenko)

</div>
