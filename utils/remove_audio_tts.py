"""
Script to completely remove all audio buttons and TTS references from all lessons in the database.
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

def clean_html(html):
    if not html:
        return html
    # Remove audio-play-btn buttons
    html = re.sub(r'<button class="audio-play-btn"[^>]*>.*?</button>', '', html)
    # Remove mentions of clicking the speaker icon
    html = re.sub(r'Нажимайте на значок 🔊[^\.<]*[\.\!]', '', html)
    html = re.sub(r'Натискайте на значок 🔊[^\.<]*[\.\!]', '', html)
    html = re.sub(r'Нажимайте 🔊[^\.<]*[\.\!]', '', html)
    html = re.sub(r'Натискайте 🔊[^\.<]*[\.\!]', '', html)
    html = re.sub(r'Click the 🔊 button[^\.<]*[\.\!]', '', html)
    html = re.sub(r'Cliquez sur le bouton 🔊[^\.<]*[\.\!]', '', html)
    return html

def remove_audio_from_all_lessons():
    lessons = Lesson.objects.all()
    count = 0
    for l in lessons:
        changed = False
        for field in ['content_html_ru', 'content_html_uk', 'content_html_en', 'content_html_fr']:
            val = getattr(l, field)
            cleaned = clean_html(val)
            if cleaned != val:
                setattr(l, field, cleaned)
                changed = True
        if changed:
            l.save()
            count += 1
            print(f"Cleaned audio from lesson: {l.data_lesson_id}")
    print(f"Finished cleaning audio from {count} lessons!")

if __name__ == '__main__':
    remove_audio_from_all_lessons()
