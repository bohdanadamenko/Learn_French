# 🇧🇪 Français Facile Belgium

<div align="center">

<a href="#"><img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"></a>
<a href="#"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
<a href="#"><img src="https://img.shields.io/badge/CKEditor-5-0287D0?style=for-the-badge&logo=ckeditor&logoColor=white" alt="CKEditor"></a>
<a href="#"><img src="https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge" alt="License"></a>

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
├── 📂 apps/                    # 🧩 Application Domains
│   ├── 📂 core/                # 🏠 Core logic (Views, Templates, Static)
│   ├── 📂 lessons/             # 🎓 Lessons Domain (Models, Selectors)
│   └── 📂 quizzes/             # ❓ Quizzes Domain (Models, Selectors)
├── 📂 learn_french/            # ⚙️ Django settings
├── 📂 locale/                  # 🌍 Global Translations
├── 📂 utils/                   # 🛠️ Utility scripts
├── 📄 .env                     # 🔐 Secrets (not in git!)
├── 📄 requirements.txt         # 📦 Dependencies
└── 📄 manage.py                # 🚀 Django CLI
```

---

## 🛠️ Technologies

| Backend | Frontend | Database | Admin |
|:-------:|:--------:|:--------:|:-----:|
| <a href="#"><img src="https://img.shields.io/badge/-Django%205.2-092E20?logo=django" alt="Django"></a> | <a href="#"><img src="https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript"></a> | <a href="#"><img src="https://img.shields.io/badge/-SQLite-003B57?logo=sqlite" alt="SQLite"></a> | <a href="#"><img src="https://img.shields.io/badge/-Jazzmin-black" alt="Jazzmin"></a> |
| <a href="#"><img src="https://img.shields.io/badge/-Python%203.10-3776AB?logo=python&logoColor=white" alt="Python"></a> | <a href="#"><img src="https://img.shields.io/badge/-CSS3-1572B6?logo=css3" alt="CSS3"></a> | | <a href="#"><img src="https://img.shields.io/badge/-CKEditor%205-0287D0?logo=ckeditor" alt="CKEditor 5"></a> |

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
© 2025 Learn French. All rights reserved.
Proprietary License - not for distribution
```

---

<div align="center">

### 👨‍💻 Development

**Learn French Team** 🇧🇪

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)](https://github.com/bohdanadamenko)

</div>
