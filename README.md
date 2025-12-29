# 🇫🇷 Français Facile Belgique

&lt;div align="center"&gt;

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&amp;logo=django&amp;logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white)
![CKEditor](https://img.shields.io/badge/CKEditor-5-0287D0?style=for-the-badge&amp;logo=ckeditor&amp;logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)

**🎓 Интерактивная платформа для изучения французского языка**

*Современное веб-приложение с мультиязычной поддержкой и адаптивным дизайном*

[🚀 Демо](#-быстрый-старт) • [📖 Документация](#-структура-проекта) • [🛠️ Установка](#установка)

&lt;/div&gt;

---

## ✨ Возможности

| 🌍 Мультиязычность | 🎨 Современный UI | 📱 Адаптивность |
|:---:|:---:|:---:|
| RU • UA • EN • FR | Glassmorphism & Dark Mode | Desktop & Mobile |

- 🎯 **Уроки французского** с интерактивными тестами
- 📝 **CKEditor 5** для rich-text контента в админке
- 🔐 **Jazzmin Admin** — красивая и функциональная админ-панель
- 🌙 **Темная/светлая тема** с плавными переходами
- ⌨️ **Горячие клавиши** для быстрой навигации
- 🔍 **Поиск по урокам** в реальном времени

---

## 🚀 Быстрый старт

### Требования

- 🐍 Python 3.10+
- 📦 pip

### Установка

```bash
# 1️⃣ Клонируйте репозиторий
git clone https://github.com/YOUR_USERNAME/francais-facile-be.git
cd francais-facile-be

# 2️⃣ Создайте виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3️⃣ Установите зависимости
pip install -r requirements.txt

# 4️⃣ Настройте переменные окружения
cat &gt; .env &lt;&lt; EOF
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EOF

# 5️⃣ Примените миграции
python manage.py migrate

# 6️⃣ Создайте суперпользователя
python manage.py createsuperuser

# 7️⃣ Запустите сервер
python manage.py runserver
```

🌐 Откройте: **http://127.0.0.1:8000**

---

## 📁 Структура проекта

```
📦 francais-facile-be/
├── 📂 lessons/                  # 🎓 Основное приложение
│   ├── 📂 locale/              # 🌍 Переводы (RU/UA/EN/FR)
│   ├── 📂 management/          # ⚙️ Django команды
│   ├── 📂 migrations/          # 🗄️ Миграции БД
│   ├── 📂 static/lessons/      # 🎨 CSS, JS файлы
│   ├── 📂 templates/           # 📄 HTML шаблоны
│   ├── 📄 models.py            # 📊 Модели данных
│   ├── 📄 admin.py             # 🔧 Настройки админки
│   └── 📄 views.py             # 👁️ Представления
├── 📂 project_valerie/         # ⚙️ Настройки Django
├── 📄 .env                     # 🔐 Секреты (не в git!)
├── 📄 requirements.txt         # 📦 Зависимости
└── 📄 manage.py                # 🚀 Django CLI
```

---

## 🛠️ Технологии

| Backend | Frontend | Database | Admin |
|:-------:|:--------:|:--------:|:-----:|
| ![Django](https://img.shields.io/badge/-Django%205.2-092E20?logo=django) | ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&amp;logoColor=black) | ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite) | ![Jazzmin](https://img.shields.io/badge/-Jazzmin-purple) |
| ![Python](https://img.shields.io/badge/-Python%203.10-3776AB?logo=python&amp;logoColor=white) | ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3) | | ![CKEditor5](https://img.shields.io/badge/-CKEditor%205-0287D0?logo=ckeditor) |

---

## ⌨️ Горячие клавиши

| Клавиша | Действие |
|:-------:|:---------|
| `→` | Следующий урок |
| `←` | Предыдущий урок |
| `/` | Быстрый поиск |
| `Esc` | Закрыть меню |

---

## 🔧 Управление контентом

Для редактирования уроков используйте **Django Admin**:

```
🔗 http://127.0.0.1:8000/admin
```

### Возможности админки:

- ✏️ Редактирование уроков на 4 языках
- 📊 Управление вопросами и тестами  
- 🖼️ Загрузка изображений через CKEditor 5
- 🏷️ Языковые вкладки для удобной работы

---

## 🔒 Безопасность

| Мера | Описание |
|:----:|:---------|
| 🔑 | `SECRET_KEY` хранится в `.env` файле |
| 🛡️ | `DEBUG=False` в продакшене |
| 🌐 | `ALLOWED_HOSTS` ограничен |
| 🔐 | Пароли валидируются Django |

---

## 📄 Лицензия

```
© 2024 Project Valerie. All rights reserved.
Proprietary License - не для распространения
```

---

&lt;div align="center"&gt;

### 👨‍💻 Разработка

**Project Valerie Team** 🇧🇪

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)](https://github.com/YOUR_USERNAME)

&lt;/div&gt;
