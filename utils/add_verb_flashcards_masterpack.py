"""
Master script to add interactive 3D flashcards across all verb lessons:
- lesson-er-verbs (Parler, Habiter, Travailler, Manger)
- lesson-ir-verbs (Finir, Choisir, Réussir)
- lesson-key-irregular-verbs (Prendre, Venir, Savoir, Voir, Mettre, Devoir)
- lesson-reflexive (Se lever, Se coucher, S'appeler, S'habiller)
- lesson-futur-proche (Je vais manger, On va partir)
- lesson-futur-simple (Je parlerai, Je serai, J'aurai, Je ferai)
- lesson-questions (Où, Quand, Comment, Pourquoi, Est-ce que)
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson

verb_cards_data = {
    "lesson-er-verbs": [
        ("Я розмовляю французькою", "Я говорю по-французски", "I speak French", "Je parle français", "[жьо парль франсе]"),
        ("Я живу в Брюсселі", "Я живу в Брюсселе", "I live in Brussels", "J'habite à Bruxelles", "[жабіт а брюсель] 🇧🇪"),
        ("Ми працюємо разом", "Мы работаем вместе", "We work together", "Nous travaillons ensemble", "[ну травайон ансамбль]"),
        ("Вони люблять шоколад", "Они любят шоколад", "They love chocolate", "Ils aiment le chocolat", "[іль-з-ем льо шоколя]")
    ],
    "lesson-ir-verbs": [
        ("Я закінчую роботу", "Я заканчиваю работу", "I finish the work", "Je finis le travail", "[жьо фіні льо травай]"),
        ("Ти вибираєш десерт", "Ты выбираешь десерт", "You choose the dessert", "Tu choisis le dessert", "[тю шуазі льо десер]"),
        ("Ми досягаємо успіху", "Мы добиваемся успеха", "We succeed", "Nous réussissons", "[ну реюсісон]"),
        ("Вони розмірковують", "Они размышляют", "They reflect / think", "Ils réfléchissent", "[іль рефлешіс]")
    ],
    "lesson-key-irregular-verbs": [
        ("Я беру поїзд / замовляю", "Я беру поезд / заказываю", "I take the train / order", "Je prends le train", "[жьо пран льо трен]"),
        ("Я щойно прийшов", "Я только что пришел", "I just arrived", "Je viens d'arriver", "[жьо в'єн даріве]"),
        ("Я знаю це правило", "Я знаю это правило", "I know this rule", "Je sais cette règle", "[жьо се сет регль]"),
        ("Я мушу йти", "Я должен идти", "I have to go", "Je dois partir", "[жьо дуа партір]")
    ],
    "lesson-reflexive": [
        ("Я прокидаюся о 7:00", "Я просыпаюсь в 7:00", "I wake up at 7:00", "Je me réveille à 7h", "[жьо мьо ревей а сет йор]"),
        ("Мене звати...", "Меня зовут...", "My name is...", "Je m'appelle...", "[жьо мапель]"),
        ("Ми готуємося", "Мы готовимся", "We are getting ready", "Nous nous préparons", "[ну ну препарон]"),
        ("Він лягає спати", "Он ложится спать", "He goes to bed", "Il se couche", "[іль сьо куш]")
    ],
    "lesson-futur-proche": [
        ("Я зараз поїм", "Я сейчас поем", "I am going to eat", "Je vais manger", "[жьо ве манже]"),
        ("Ми зараз підемо", "Мы сейчас уйдем", "We are going to leave", "Nous allons partir", "[ну-з-алон партір]"),
        ("Що ти збираєшся робити?", "Что ты собираешься делать?", "What are you going to do?", "Qu'est-ce que tu vas faire ?", "[кеске тю ва фер]")
    ],
    "lesson-futur-simple": [
        ("Я буду в Брюсселі завтра", "Я буду в Брюсселе завтра", "I will be in Brussels tomorrow", "Je serai à Bruxelles demain", "[жьо сьорé а брюсель дьомен] 🇧🇪"),
        ("У нас буде час", "У нас будет время", "We will have time", "Nous aurons le temps", "[ну-з-орон льо тан]"),
        ("Я зроблю це пізніше", "Я сделаю это позже", "I will do it later", "Je le ferai plus tard", "[жьо льо фьорé плю тар]")
    ],
    "lesson-questions": [
        ("Де знаходиться вокзал?", "Где находится вокзал?", "Where is the station?", "Où est la gare ?", "[у е ля гар]"),
        ("Коли прибуває поїзд?", "Когда прибывает поезд?", "When does the train arrive?", "Quand arrive le train ?", "[кан арів льо трен]"),
        ("Чому ти запізнився?", "Почему ты опоздал?", "Why are you late?", "Pourquoi es-tu en retard ?", "[пуркуа е-тю ан рьотар]"),
        ("Як це сказати?", "Как это сказать?", "How do you say this?", "Comment dit-on ?", "[коман ді-тон]")
    ]
}

def make_cards_block(cards, lang="uk"):
    items = []
    for uk_txt, ru_txt, en_txt, fr_txt, tr_txt in cards:
        if lang == "uk":
            front = uk_txt
            hint = "Натисніть для перекладу"
        elif lang == "ru":
            front = ru_txt
            hint = "Нажмите для перевода"
        elif lang == "en":
            front = en_txt
            hint = "Click to flip"
        else:
            front = fr_txt
            hint = "Cliquez pour retourner"

        items.append(f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.2rem; color:var(--accent-blue);">{front}</strong>
                    <span class="flip-hint">{hint}</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">{fr_txt}</strong>
                    <span style="font-size:0.8rem; margin-top:4px;">{tr_txt}</span>
                </div>
            </div>
        </div>
        """)

    title = {
        "uk": "<h3>🃏 Картки для запам'ятовування</h3>",
        "ru": "<h3>🃏 Карточки для запоминания</h3>",
        "en": "<h3>🃏 Practice Cards</h3>",
        "fr": "<h3>🃏 Cartes mémoire</h3>"
    }[lang]

    return f"""
    {title}
    <div class="flip-grid">
        {"".join(items)}
    </div>
    """

def apply_verb_flashcards():
    count = 0
    for lesson_id, cards in verb_cards_data.items():
        lesson = Lesson.objects.filter(data_lesson_id=lesson_id).first()
        if not lesson:
            continue

        if "flip-card" not in (lesson.content_html_uk or ""):
            lesson.content_html_uk = (lesson.content_html_uk or "") + "\n" + make_cards_block(cards, "uk")
        if "flip-card" not in (lesson.content_html_ru or ""):
            lesson.content_html_ru = (lesson.content_html_ru or "") + "\n" + make_cards_block(cards, "ru")
        if "flip-card" not in (lesson.content_html_en or ""):
            lesson.content_html_en = (lesson.content_html_en or "") + "\n" + make_cards_block(cards, "en")
        if "flip-card" not in (lesson.content_html_fr or ""):
            lesson.content_html_fr = (lesson.content_html_fr or "") + "\n" + make_cards_block(cards, "fr")

        lesson.save()
        count += 1
        print(f"Added interactive flashcards to verb lesson: {lesson.data_lesson_id}")

    print(f"Successfully added flashcards to {count} verb lessons!")

if __name__ == '__main__':
    apply_verb_flashcards()
