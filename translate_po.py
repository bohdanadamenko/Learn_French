import os
import re

translations = {
    'en': {
        "Урок": "Lesson",
        "Уроки": "Lessons",
        "Вопрос": "Question",
        "Вопросы": "Questions",
        "Вариант ответа": "Answer Choice",
        "Варианты ответов": "Answer Choices",
        "Порядок сортировки": "Sort Order",
        "Дата создания": "Date Created",
        "Порядок": "Order",
        "Это правильный ответ?": "Is this correct?",
        "Заголовок (RU)": "Title (RU)",
        "Заголовок (UA)": "Title (UA)",
        "Заголовок (EN)": "Title (EN)",
        "Заголовок (FR)": "Title (FR)",
        "Контент (RU)": "Content (RU)",
        "Контент (UA)": "Content (UA)",
        "Контент (EN)": "Content (EN)",
        "Контент (FR)": "Content (FR)",
        "Текст вопроса (RU)": "Question Text (RU)",
        "Текст вопроса (UA)": "Question Text (UA)",
        "Текст вопроса (EN)": "Question Text (EN)",
        "Текст вопроса (FR)": "Question Text (FR)",
        "Текст ответа (RU)": "Answer Text (RU)",
        "Текст ответа (UA)": "Answer Text (UA)",
        "Текст ответа (EN)": "Answer Text (EN)",
        "Текст ответа (FR)": "Answer Text (FR)",
        "Django site admin": "Django Administration",
        "Django administration": "Site Administration",
        "Урок (RU)": "Lesson (RU)",
        "Урок (UA)": "Lesson (UA)",
        "Урок (EN)": "Lesson (EN)",
        "Урок (FR)": "Lesson (FR)",
        "Связь": "Connection",
        "Основные настройки": "Main Settings",
        "Русский язык (RU)": "Russian (RU)",
        "Українська мова (UA)": "Ukrainian (UA)",
        "English (EN)": "English (EN)",
        "Français (FR)": "French (FR)",
        "Старые поля (для справки)": "Legacy Fields (Reference)",
    },
    'fr': {
        "Урок": "Leçon",
        "Уроки": "Leçons",
        "Вопрос": "Question",
        "Вопросы": "Questions",
        "Вариант ответа": "Choix de réponse",
        "Варианты ответов": "Choix de réponses",
        "Порядок сортировки": "Ordre de tri",
        "Дата создания": "Date de création",
        "Порядок": "Ordre",
        "Это правильный ответ?": "Est-ce correct ?",
        "Заголовок (RU)": "Titre (RU)",
        "Заголовок (UA)": "Titre (UA)",
        "Заголовок (EN)": "Titre (EN)",
        "Заголовок (FR)": "Titre (FR)",
        "Контент (RU)": "Contenu (RU)",
        "Контент (UA)": "Contenu (UA)",
        "Контент (EN)": "Contenu (EN)",
        "Контент (FR)": "Contenu (FR)",
        "Текст вопроса (RU)": "Texte de la question (RU)",
        "Текст вопроса (UA)": "Texte de la question (UA)",
        "Текст вопроса (EN)": "Texte de la question (EN)",
        "Текст вопроса (FR)": "Texte de la question (FR)",
        "Текст ответа (RU)": "Texte de la réponse (RU)",
        "Текст ответа (UA)": "Texte de la réponse (UA)",
        "Текст ответа (EN)": "Texte de la réponse (EN)",
        "Текст ответа (FR)": "Texte de la réponse (FR)",
        "Django site admin": "Administration du site",
        "Django administration": "Administration",
        "Урок (RU)": "Leçon (RU)",
        "Урок (UA)": "Leçon (UA)",
        "Урок (EN)": "Leçon (EN)",
        "Урок (FR)": "Leçon (FR)",
        "Связь": "Connexion",
        "Основные настройки": "Paramètres principaux",
        "Русский язык (RU)": "Russe (RU)",
        "Українська мова (UA)": "Ukrainien (UA)",
        "English (EN)": "Anglais (EN)",
        "Français (FR)": "Français (FR)",
        "Старые поля (для справки)": "Anciens champs (Référence)",
    },
    'uk': {
        "Урок": "Урок",
        "Уроки": "Уроки",
        "Вопрос": "Питання",
        "Вопросы": "Питання",
        "Вариант ответа": "Варіант відповіді",
        "Варианты ответов": "Варіанти відповідей",
        "Порядок сортировки": "Порядок сортування",
        "Дата создания": "Дата створення",
        "Порядок": "Порядок",
        "Это правильный ответ?": "Це правильна відповідь?",
        "Заголовок (RU)": "Заголовок (RU)",
        "Заголовок (UA)": "Заголовок (UA)",
        "Заголовок (EN)": "Заголовок (EN)",
        "Заголовок (FR)": "Заголовок (FR)",
        "Контент (RU)": "Вміст (RU)",
        "Контент (UA)": "Вміст (UA)",
        "Контент (EN)": "Вміст (EN)",
        "Контент (FR)": "Вміст (FR)",
        "Текст вопроса (RU)": "Текст питання (RU)",
        "Текст вопроса (UA)": "Текст питання (UA)",
        "Текст вопроса (EN)": "Текст питання (EN)",
        "Текст вопроса (FR)": "Текст питання (FR)",
        "Текст ответа (RU)": "Текст відповіді (RU)",
        "Текст ответа (UA)": "Текст відповіді (UA)",
        "Текст ответа (EN)": "Текст відповіді (EN)",
        "Текст ответа (FR)": "Текст відповіді (FR)",
        "Django site admin": "Адміністрування сайту",
        "Django administration": "Адміністрування",
        "Урок (RU)": "Урок (RU)",
        "Урок (UA)": "Урок (UA)",
        "Урок (EN)": "Урок (EN)",
        "Урок (FR)": "Урок (FR)",
        "Связь": "Зв'язок",
        "Основные настройки": "Основні налаштування",
        "Русский язык (RU)": "Російська мова (RU)",
        "Українська мова (UA)": "Українська мова (UA)",
        "English (EN)": "Англійська мова (EN)",
        "Français (FR)": "Французька мова (FR)",
        "Старые поля (для справки)": "Старі поля (для довідки)",
    }
}

base_dir = 'lessons/locale'

for lang, trans_map in translations.items():
    po_file = os.path.join(base_dir, lang, 'LC_MESSAGES', 'django.po')
    if not os.path.exists(po_file):
        print(f"File not found: {po_file}")
        continue

    with open(po_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple replacement strategy: find msgid "..." followed by msgstr "" and replace msgstr
    # This is a bit fragile but works for generated files
    
    for msgid, msgstr in trans_map.items():
        # Escape quotes in msgid for regex
        escaped_msgid = re.escape(msgid)
        pattern = f'msgid "{escaped_msgid}"\nmsgstr ""'
        replacement = f'msgid "{msgid}"\nmsgstr "{msgstr}"'
        
        if pattern in content:
            content = content.replace(pattern, replacement)
        else:
            print(f"Warning: msgid '{msgid}' not found or already translated in {lang}")

    with open(po_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {lang}")
