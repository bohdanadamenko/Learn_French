# 🇫🇷 Français Facile Belgium

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CKEditor](https://img.shields.io/badge/CKEditor-5-0287D0?style=for-the-badge&logo=ckeditor&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)

**🎓 Interactive platform for learning French**

*Modern web application with multilingual support and responsive design*

[🚀 Demo](#-quick-start) • [📖 Documentation](#-project-structure) • [🛠️ Installation](#installation)

</div>

---

## ✨ Features

| 🌍 Multilingual | 🎨 Modern UI | 📱 Responsive |
|:---:|:---:|:---:|
| RU • UK • EN • FR | Glassmorphism & Dark Mode | Desktop & Mobile |

- 🎯 **French Lessons** with interactive quizzes
- 📝 **CKEditor 5** for rich-text content in admin
- 🔐 **Jazzmin Admin** — beautiful and functional admin panel
- 🌙 **Dark/Light Theme** with smooth transitions
- ⌨️ **Hotkeys** for quick navigation
- 🔍 **Real-time Lesson Search**

---

## 🚀 Quick Start

### Requirements

- 🐍 Python 3.10+
- 📦 pip

### Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/bohdanadamenko/Learn_French.git
cd francais-facile-be

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
EOF

# 5️⃣ Apply migrations
python manage.py migrate

# 6️⃣ Create a superuser
python manage.py createsuperuser

# 7️⃣ Run the server
python manage.py runserver
```

🌐 Open: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
📦 francais-facile-be/
├── 📂 lessons/                  # 🎓 Main application
│   ├── 📂 locale/              # 🌍 Translations (RU/UK/EN/FR)
│   ├── 📂 management/          # ⚙️ Django commands
│   ├── 📂 migrations/          # 🗄️ DB Migrations
│   ├── 📂 static/lessons/      # 🎨 CSS, JS files
│   ├── 📂 templates/           # 📄 HTML templates
│   ├── 📄 models.py            # 📊 Data models
│   ├── 📄 admin.py             # 🔧 Admin settings
│   └── 📄 views.py             # 👁️ Views
├── 📂 project_valerie/         # ⚙️ Django settings
├── 📄 .env                     # 🔐 Secrets (not in git!)
├── 📄 requirements.txt         # 📦 Dependencies
└── 📄 manage.py                # 🚀 Django CLI
```

---

## 🛠️ Technologies

| Backend | Frontend | Database | Admin |
|:-------:|:--------:|:--------:|:-----:|
| ![Django](https://img.shields.io/badge/-Django%205.2-092E20?logo=django) | ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black) | ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite) | ![Jazzmin](https://img.shields.io/badge/-Jazzmin-purple) |
| ![Python](https://img.shields.io/badge/-Python%203.10-3776AB?logo=python&logoColor=white) | ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3) | | ![CKEditor5](https://img.shields.io/badge/-CKEditor%205-0287D0?logo=ckeditor) |

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
| 🌐 | `ALLOWED_HOSTS` restricted |
| 🔐 | Passwords validated by Django |

---

## 📄 License

```
© 2024 Project Valerie. All rights reserved.
Proprietary License - not for distribution
```

---

<div align="center">

### 👨‍💻 Development

**Project Valerie Team** 🇧🇪

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)](https://github.com/bohdanadamenko)

</div>
