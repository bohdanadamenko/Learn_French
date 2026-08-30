"""
Script to rename all flashcard headers to clean and professional titles:
UK: <h3>🃏 Картки для запам'ятовування</h3>
RU: <h3>🃏 Карточки для запоминания</h3>
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson

def clean_uk(html):
    if not html:
        return html
    html = re.sub(
        r'<h3>[0-9\.\s]*🃏\s*Інтерактивні\s+флеш-картки(?:\s*\(ФМ\))?[^<]*</h3>',
        '<h3>🃏 Картки для запам\'ятовування</h3>',
        html,
        flags=re.IGNORECASE
    )
    html = re.sub(
        r'<h3>[0-9\.\s]*🃏\s*Флеш-картки[^<]*</h3>',
        '<h3>🃏 Картки для запам\'ятовування</h3>',
        html,
        flags=re.IGNORECASE
    )
    return html

def clean_ru(html):
    if not html:
        return html
    html = re.sub(
        r'<h3>[0-9\.\s]*🃏\s*Интерактивные\s+флеш-карточки(?:\s*\(ФМ\))?[^<]*</h3>',
        '<h3>🃏 Карточки для запоминания</h3>',
        html,
        flags=re.IGNORECASE
    )
    html = re.sub(
        r'<h3>[0-9\.\s]*🃏\s*Флеш-карточки[^<]*</h3>',
        '<h3>🃏 Карточки для запоминания</h3>',
        html,
        flags=re.IGNORECASE
    )
    return html

def rename_all():
    lessons = Lesson.objects.all()
    count = 0
    for l in lessons:
        changed = False
        new_uk = clean_uk(l.content_html_uk)
        if new_uk != l.content_html_uk:
            l.content_html_uk = new_uk
            changed = True
            
        new_ru = clean_ru(l.content_html_ru)
        if new_ru != l.content_html_ru:
            l.content_html_ru = new_ru
            changed = True
            
        if changed:
            l.save()
            count += 1
            print(f"Renamed in lesson: {l.data_lesson_id}")
            
    print(f"Renamed headers across {count} lessons!")

if __name__ == '__main__':
    rename_all()
