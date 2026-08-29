"""
Script to equip all key lessons across curriculum with dynamic interactive Flip Cards (ФМ / Flashcards).
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson

lesson_flashcards_data = {
    "lesson-negation": [
        ("Я не знаю", "Je ne sais pas", "[жьо ньо се па]"),
        ("Я не хочу", "Je ne veux pas", "[жьо ньо вьо па]"),
        ("Я не студент", "Je ne suis pas étudiant", "[жьо ньо сюі па]")
    ],
    "lesson-time": [
        ("Котра година?", "Quelle heure est-il ?", "[кель йор е-т-іль]"),
        ("Зараз 8:30", "Il est huit heures et demie", "[іль е юіт йор е дьмі]"),
        ("Зараз полудень", "Il est midi", "[іль е міді]")
    ],
    "lesson-cafe": [
        ("Рахунок, будь ласка", "L'addition, s'il vous plaît", "[лядісьон сіль ву пле]"),
        ("Для мене круасан", "Pour moi, un croissant", "[пур муа ен круасан]"),
        ("Столик на двох", "Une table pour deux", "[юн табль пур дьо]")
    ],
    "lesson-shopping": [
        ("Скільки це коштує?", "Combien ça coûte ?", "[комб'єн са кут]"),
        ("Я можу поміряти?", "Je peux essayer ?", "[жьо пьо есейє]"),
        ("Чи є менший розмір?", "Vous avez une taille en dessous ?", "[ву-з-аве юн тай]")
    ],
    "lesson-transport": [
        ("Один квиток до Брюсселя", "Un billet pour Bruxelles", "[ен бійє пур брюсель] 🇧🇪"),
        ("Де знаходиться вокзал?", "Où est la gare ?", "[у е ля гар]"),
        ("Який це поїзд?", "Quel est ce train ?", "[кель е сьо трен]")
    ],
    "lesson-directions": [
        ("Прямо", "Tout droit", "[ту друа]"),
        ("Ліворуч / Праворуч", "À gauche / À droite", "[а гош / а друат]"),
        ("Поруч зі станцією", "À côté de la gare", "[а коте дьо ля гар]")
    ],
    "lesson-doctor-be": [
        ("У мене болить голова", "J'ai mal à la tête", "[же маль а ля тет]"),
        ("Мені потрібен рецепт", "J'ai besoin d'une ordonnance", "[же безуен дюн ордонанс]"),
        ("Картка Mutuelle", "La carte de mutuelle", "[ля карт дьо мютюель] 🇧🇪")
    ],
    "lesson-commune": [
        ("Я хочу зареєструватися", "Je veux m'inscrire à la commune", "[жьо вьо менскрір] 🇧🇪"),
        ("Мій дозвіл на проживання", "Mon titre de séjour", "[мон тітр дьо сежур]"),
        ("Довідка про місце проживання", "La composition de ménage", "[ля композісьон] 🇧🇪")
    ],
    "lesson-weather": [
        ("Сьогодні сонячно", "Il y a du soleil", "[іль і а дю солей]"),
        ("Йде дощ", "Il pleut", "[іль пльо]"),
        ("Дуже спекотно", "Il fait très chaud", "[іль фе тре шо]")
    ],
    "lesson-house-rooms": [
        ("Вітальня", "Le salon", "[льйо салон]"),
        ("Кухня", "La cuisine", "[ля кюізін]"),
        ("Спальня", "La chambre", "[ля шамбр]")
    ],
    "lesson-clothes": [
        ("Куртка / Пальто", "Le manteau", "[льйо манто]"),
        ("Взуття", "Les chaussures", "[ле шосюр]"),
        ("Штани", "Le pantalon", "[льйо панталон]")
    ]
}

def make_cards_html(cards):
    items = []
    for front, back_fr, back_tr in cards:
        items.append(f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-blue);">{front}</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">{back_fr}</strong>
                    <span style="font-size:0.8rem; margin-top:4px;">{back_tr}</span>
                </div>
            </div>
        </div>
        """)
    return f"""
    <h3>🃏 Інтерактивні флеш-картки (ФМ) для самоперевірки</h3>
    <p>Натискайте на картку, щоб перевернути її та перевірити себе:</p>
    <div class="flip-grid">
        {"".join(items)}
    </div>
    """

def add_flashcards_everywhere():
    count = 0
    for lesson_id, cards in lesson_flashcards_data.items():
        lesson = Lesson.objects.filter(data_lesson_id=lesson_id).first()
        if not lesson:
            continue
        
        cards_html = make_cards_html(cards)
        
        # Check if already has flip cards
        if "flip-card" not in (lesson.content_html_uk or ""):
            lesson.content_html_uk = (lesson.content_html_uk or "") + "\n" + cards_html
        if "flip-card" not in (lesson.content_html_ru or ""):
            lesson.content_html_ru = (lesson.content_html_ru or "") + "\n" + cards_html
        lesson.save()
        count += 1
        print(f"Added dynamic flip cards to: {lesson.data_lesson_id}")
        
    print(f"Successfully added dynamic flashcards to {count} lessons!")

if __name__ == '__main__':
    add_flashcards_everywhere()
