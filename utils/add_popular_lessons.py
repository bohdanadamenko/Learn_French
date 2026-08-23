"""
Script to seed popular French starter lessons with full 4-language support and interactive quizzes.
"""
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Topic, Lesson
from apps.quizzes.models import Question, Choice

def seed_lessons():
    topic1 = Topic.objects.get(order=1) # 🚀 Основи та перші кроки
    topic3 = Topic.objects.get(order=3) # ⚡ Дієслова, часи та запитання
    topic4 = Topic.objects.get(order=4) # 🌍 Лексика та теми

    lessons_data = [
        {
            "order": 19,
            "data_lesson_id": "lesson-time",
            "topic": topic1,
            "title_uk": "⏰ Котра година? (Час)",
            "title_ru": "⏰ Который час? (Время)",
            "title_en": "⏰ What Time is it? (Time)",
            "title_fr": "⏰ Quelle heure est-il ?",
            "content_html_uk": """
            <h2>Як сказати котра година</h2>
            <p>У французькій мові для позначення часу завжди використовується безособова конструкція <strong>Il est...</strong></p>
            <div class="example-box">
                <p><strong>Quelle heure est-il ?</strong> [кель йор е-т-іль] — Котра година?</p>
                <p><strong>Il est huit heures.</strong> — Зараз 8 годин.</p>
            </div>
            <h3>Головні конструкції :</h3>
            <ul>
                <li><strong>Il est midi</strong> — Зараз полудень (12:00 дня).</li>
                <li><strong>Il est minuit</strong> — Зараз північ (00:00 ночі).</li>
                <li><strong>... et quart</strong> — ... з чвертю (наприклад: <em>Il est 8h et quart</em> = 08:15).</li>
                <li><strong>... et demie</strong> — ... з половиною (наприклад: <em>Il est 8h et demie</em> = 08:30).</li>
                <li><strong>... moins le quart</strong> — за чверть (наприклад: <em>Il est 9h moins le quart</em> = 08:45).</li>
            </ul>
            <div class="example-box warning">
                <strong>Важливо :</strong> Слово <strong>heure</strong> обов'язково вимовляється зі зв'язуванням (liaison): <em>deux heures</em> [де-зер], <em>trois heures</em> [труа-зер].
            </div>
            """,
            "content_html_ru": """
            <h2>Как сказать который час</h2>
            <p>Во французском языке для указания времени всегда используется безличная конструкция <strong>Il est...</strong></p>
            <div class="example-box">
                <p><strong>Quelle heure est-il ?</strong> [кэль ёр э-т-иль] — Который час?</p>
                <p><strong>Il est huit heures.</strong> — Сейчас 8 часов.</p>
            </div>
            <h3>Основные конструкции:</h3>
            <ul>
                <li><strong>Il est midi</strong> — Сейчас полдень (12:00 дня).</li>
                <li><strong>Il est minuit</strong> — Сейчас полночь (00:00 ночи).</li>
                <li><strong>... et quart</strong> — ... с четвертью (например: <em>Il est 8h et quart</em> = 08:15).</li>
                <li><strong>... et demie</strong> — ... с половиной (например: <em>Il est 8h et demie</em> = 08:30).</li>
                <li><strong>... moins le quart</strong> — без четверти (например: <em>Il est 9h moins le quart</em> = 08:45).</li>
            </ul>
            <div class="example-box warning">
                <strong>Важно:</strong> Слово <strong>heure</strong> обязательно произносится со связыванием (liaison): <em>deux heures</em> [де-зёр], <em>trois heures</em> [труа-зёр].
            </div>
            """,
            "content_html_en": """
            <h2>How to Tell the Time in French</h2>
            <p>In French, to state the time, we always use the impersonal phrase <strong>Il est...</strong></p>
            <div class="example-box">
                <p><strong>Quelle heure est-il ?</strong> — What time is it?</p>
                <p><strong>Il est huit heures.</strong> — It is eight o'clock.</p>
            </div>
            <h3>Key Expressions:</h3>
            <ul>
                <li><strong>Il est midi</strong> — It is noon (12:00 PM).</li>
                <li><strong>Il est minuit</strong> — It is midnight (12:00 AM).</li>
                <li><strong>... et quart</strong> — quarter past (e.g. <em>Il est 8h et quart</em> = 8:15).</li>
                <li><strong>... et demie</strong> — half past (e.g. <em>Il est 8h et demie</em> = 8:30).</li>
                <li><strong>... moins le quart</strong> — quarter to (e.g. <em>Il est 9h moins le quart</em> = 8:45).</li>
            </ul>
            <div class="example-box warning">
                <strong>Tip:</strong> The word <strong>heure</strong> requires a liaison: <em>deux heures</em> [deuh-zeur], <em>trois heures</em> [trwah-zeur].
            </div>
            """,
            "content_html_fr": """
            <h2>Comment dire l'heure en français</h2>
            <p>En français, on utilise toujours la structure impersonnelle <strong>Il est...</strong> pour indiquer l'heure.</p>
            <div class="example-box">
                <p><strong>Quelle heure est-il ?</strong> — Demander l'heure.</p>
                <p><strong>Il est huit heures.</strong> — Il est 8h00.</p>
            </div>
            <h3>Expressions essentielles :</h3>
            <ul>
                <li><strong>Il est midi</strong> — 12h00 le jour.</li>
                <li><strong>Il est minuit</strong> — 00h00 la nuit.</li>
                <li><strong>... et quart</strong> — + 15 minutes (ex. <em>Il est 8h et quart</em> = 08:15).</li>
                <li><strong>... et demie</strong> — + 30 minutes (ex. <em>Il est 8h et demie</em> = 08:30).</li>
                <li><strong>... moins le quart</strong> — - 15 minutes (ex. <em>Il est 9h moins le quart</em> = 08:45).</li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Як французькою сказати 'Зараз 8:30 (пів на дев'яту)'?",
                    "text_ru": "Как по-французски сказать 'Сейчас 8:30 (полдевятого)'?",
                    "text_en": "How do you say 'It is 8:30 (half past eight)' in French?",
                    "text_fr": "Comment dit-on '08h30' en français courant ?",
                    "choices": [
                        {"text": "Il est huit heures et demie", "correct": True},
                        {"text": "Il est huit heures et quart", "correct": False},
                        {"text": "Il est neuf heures moins le quart", "correct": False}
                    ]
                },
                {
                    "text_uk": "Що означає фраза 'Il est midi'?",
                    "text_ru": "Что означает фраза 'Il est midi'?",
                    "text_en": "What does 'Il est midi' mean?",
                    "text_fr": "Que signifie 'Il est midi' ?",
                    "choices": [
                        {"text": "Зараз 12:00 дня (полудень) / It is noon", "correct": True},
                        {"text": "Зараз 00:00 ночі (північ) / It is midnight", "correct": False},
                        {"text": "Зараз 13:00 / It is 1 PM", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 20,
            "data_lesson_id": "lesson-numbers-100",
            "topic": topic1,
            "title_uk": "🔢 Числа 1-100",
            "title_ru": "🔢 Числа 1-100",
            "title_en": "🔢 Numbers 1-100",
            "title_fr": "🔢 Les nombres de 1 à 100",
            "content_html_uk": """
            <h2>Десятки та логіка рахунку</h2>
            <p>Французькі числа мають унікальну систему рахунку після 60. Давайте розберемося!</p>
            <div class="conjugation-grid">
                <div><strong>10</strong> — Dix</div>
                <div><strong>20</strong> — Vingt</div>
                <div><strong>30</strong> — Trente</div>
                <div><strong>40</strong> — Quarante</div>
                <div><strong>50</strong> — Cinquante</div>
                <div><strong>60</strong> — Soixante</div>
            </div>
            <h3>Особливості 70, 80, 90 у Франції :</h3>
            <ul>
                <li><strong>70</strong> = 60 + 10 : <em>Soixante-dix</em></li>
                <li><strong>80</strong> = 4 × 20 : <em>Quatre-vingts</em></li>
                <li><strong>90</strong> = 4 × 20 + 10 : <em>Quatre-vingt-dix</em></li>
                <li><strong>100</strong> = <em>Cent</em></li>
            </ul>
            <div class="example-box">
                <strong>🇧🇪 У Бельгії та Швейцарії все простіше :</strong>
                <p>70 = <strong>Septante</strong>, 90 = <strong>Nonante</strong> !</p>
            </div>
            """,
            "content_html_ru": """
            <h2>Десятки и логика счёта</h2>
            <p>Во французском языке числа после 60 имеют математическую логику:</p>
            <div class="conjugation-grid">
                <div><strong>10</strong> — Dix [дис]</div>
                <div><strong>20</strong> — Vingt [вэн]</div>
                <div><strong>30</strong> — Trente [трант]</div>
                <div><strong>40</strong> — Quarante [карант]</div>
                <div><strong>50</strong> — Cinquante [сэнкант]</div>
                <div><strong>60</strong> — Soixante [суасант]</div>
            </div>
            <h3>Французская математика (70, 80, 90):</h3>
            <ul>
                <li><strong>70</strong> = 60 + 10 : <em>Soixante-dix</em> [суасант-дис]</li>
                <li><strong>80</strong> = 4 × 20 : <em>Quatre-vingts</em> [катр-вэн]</li>
                <li><strong>90</strong> = 4 × 20 + 10 : <em>Quatre-vingt-dix</em> [катр-вэн-дис]</li>
                <li><strong>100</strong> = <em>Cent</em> [сан]</li>
            </ul>
            <div class="example-box">
                <strong>🇧🇪 В Бельгии и Швейцарии говорят проще:</strong>
                <p>70 = <strong>Septante</strong>, 90 = <strong>Nonante</strong>!</p>
            </div>
            """,
            "content_html_en": """
            <h2>Tens and Number Logic</h2>
            <p>French numbers after 60 follow an interesting mathematical pattern:</p>
            <div class="conjugation-grid">
                <div><strong>10</strong> — Dix</div>
                <div><strong>20</strong> — Vingt</div>
                <div><strong>30</strong> — Trente</div>
                <div><strong>40</strong> — Quarante</div>
                <div><strong>50</strong> — Cinquante</div>
                <div><strong>60</strong> — Soixante</div>
            </div>
            <h3>The 70, 80, 90 Logic in Standard French:</h3>
            <ul>
                <li><strong>70</strong> = 60 + 10 : <em>Soixante-dix</em></li>
                <li><strong>80</strong> = 4 × 20 : <em>Quatre-vingts</em></li>
                <li><strong>90</strong> = (4 × 20) + 10 : <em>Quatre-vingt-dix</em></li>
                <li><strong>100</strong> = <em>Cent</em></li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les dizaines et le calcul</h2>
            <div class="conjugation-grid">
                <div><strong>10</strong> — Dix</div>
                <div><strong>20</strong> — Vingt</div>
                <div><strong>30</strong> — Trente</div>
                <div><strong>40</strong> — Quarante</div>
                <div><strong>50</strong> — Cinquante</div>
                <div><strong>60</strong> — Soixante</div>
            </div>
            <h3>En France :</h3>
            <ul>
                <li><strong>70</strong> : Soixante-dix</li>
                <li><strong>80</strong> : Quatre-vingts</li>
                <li><strong>90</strong> : Quatre-vingt-dix</li>
                <li><strong>100</strong> : Cent</li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Як у Франції сказати число 80?",
                    "text_ru": "Как во Франции сказать число 80?",
                    "text_en": "How do you say 80 in standard French?",
                    "text_fr": "Comment s'écrit le nombre 80 en français standard ?",
                    "choices": [
                        {"text": "Quatre-vingts", "correct": True},
                        {"text": "Huitante", "correct": False},
                        {"text": "Soixante-vingt", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 21,
            "data_lesson_id": "lesson-aller",
            "topic": topic3,
            "title_uk": "🚶 Дієслово Aller (Іти / Їхати)",
            "title_ru": "🚶 Глагол Aller (Идти / Ехать)",
            "title_en": "🚶 Verb Aller (To go)",
            "title_fr": "🚶 Le verbe Aller",
            "content_html_uk": """
            <h2>Головне дієслово руху</h2>
            <p>Дієслово <strong>Aller</strong> (іти / їхати / прямувати) — це неправильне дієслово 3-ї групи, яке використовується щодня.</p>
            <div class="conjugation-grid">
                <div><strong>Je vais</strong> [же ве]<br>Я йду / їду</div>
                <div><strong>Tu vas</strong> [тю ва]<br>Ти йдеш</div>
                <div><strong>Il / Elle va</strong> [іль ва]<br>Він / Вона йде</div>
                <div><strong>Nous allons</strong> [ну за-лон]<br>Ми йдемо</div>
                <div><strong>Vous allez</strong> [ву за-ле]<br>Ви йдете</div>
                <div><strong>Ils vont</strong> [іль вон]<br>Вони йдуть</div>
            </div>
            <h3>Куди ви прямуєте? (Прийменники):</h3>
            <ul>
                <li><strong>à + le = AU</strong> (ч.р.) : <em>Je vais <strong>au</strong> cinéma.</em> (Я йду в кіно)</li>
                <li><strong>à + la = À LA</strong> (ж.р.) : <em>Je vais <strong>à la</strong> plage.</em> (Я йду на пляж)</li>
                <li><strong>à + les = AUX</strong> (мн.) : <em>Je vais <strong>aux</strong> toilettes.</em></li>
                <li><strong>EN</strong> (країни ж.р.) : <em>Je vais <strong>en</strong> France.</em></li>
            </ul>
            """,
            "content_html_ru": """
            <h2>Главный глагол движения</h2>
            <p>Глагол <strong>Aller</strong> (идти / ехать / направляться) — неправильный глагол 3-й группы, используемый повсеместно.</p>
            <div class="conjugation-grid">
                <div><strong>Je vais</strong> [жэ вэ]<br>Я иду / еду</div>
                <div><strong>Tu vas</strong> [тю ва]<br>Ты идёшь</div>
                <div><strong>Il / Elle va</strong> [иль ва]<br>Он / Она идёт</div>
                <div><strong>Nous allons</strong> [ну за-лон]<br>Мы идём</div>
                <div><strong>Vous allez</strong> [ву за-ле]<br>Вы идёте</div>
                <div><strong>Ils vont</strong> [иль вон]<br>Они идут</div>
            </div>
            <h3>Предлоги направления (куда?):</h3>
            <ul>
                <li><strong>à + le = AU</strong> (м.р.): <em>Je vais <strong>au</strong> restaurant.</em> (Я иду в ресторан)</li>
                <li><strong>à + la = À LA</strong> (ж.р.): <em>Je vais <strong>à la</strong> pharmacie.</em> (Я иду в аптеку)</li>
                <li><strong>à + les = AUX</strong> (мн.ч.): <em>Je vais <strong>aux</strong> magasins.</em></li>
                <li><strong>EN</strong> (страны ж.р.): <em>Je vais <strong>en</strong> Belgique / en France.</em></li>
            </ul>
            """,
            "content_html_en": """
            <h2>The Key Verb of Movement</h2>
            <p>The verb <strong>Aller</strong> (to go) is an irregular 3rd group verb essential for daily communication.</p>
            <div class="conjugation-grid">
                <div><strong>Je vais</strong><br>I go</div>
                <div><strong>Tu vas</strong><br>You go</div>
                <div><strong>Il / Elle va</strong><br>He / She goes</div>
                <div><strong>Nous allons</strong><br>We go</div>
                <div><strong>Vous allez</strong><br>You go</div>
                <div><strong>Ils vont</strong><br>They go</div>
            </div>
            <h3>Direction Prepositions:</h3>
            <ul>
                <li><strong>à + le = AU</strong> (masc.): <em>Je vais <strong>au</strong> café.</em></li>
                <li><strong>à + la = À LA</strong> (fem.): <em>Je vais <strong>à la</strong> gare.</em></li>
                <li><strong>à + les = AUX</strong> (plural): <em>Je vais <strong>aux</strong> États-Unis.</em></li>
                <li><strong>EN</strong> (fem. countries): <em>Je vais <strong>en</strong> France.</em></li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le verbe Aller au présent</h2>
            <div class="conjugation-grid">
                <div><strong>Je vais</strong></div>
                <div><strong>Tu vas</strong></div>
                <div><strong>Il / Elle va</strong></div>
                <div><strong>Nous allons</strong></div>
                <div><strong>Vous allez</strong></div>
                <div><strong>Ils / Elles vont</strong></div>
            </div>
            <h3>Les prépositions de lieu :</h3>
            <ul>
                <li><strong>AU</strong> + nom masculin : <em>Je vais au cinéma.</em></li>
                <li><strong>À LA</strong> + nom féminin : <em>Je vais à la banque.</em></li>
                <li><strong>AUX</strong> + nom pluriel : <em>Je vais aux Pays-Bas.</em></li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Оберіть правильну форму: 'Nous ___ au supermarché.'",
                    "text_ru": "Выберите правильную форму: 'Nous ___ au supermarché.'",
                    "text_en": "Choose the correct form: 'Nous ___ au supermarché.'",
                    "text_fr": "Choisissez la bonne forme : 'Nous ___ au supermarché.'",
                    "choices": [
                        {"text": "allons", "correct": True},
                        {"text": "vont", "correct": False},
                        {"text": "allez", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 22,
            "data_lesson_id": "lesson-cafe",
            "topic": topic4,
            "title_uk": "🥐 У кафе та ресторані",
            "title_ru": "🥐 В кафе и ресторане",
            "title_en": "🥐 At the Café and Restaurant",
            "title_fr": "🥐 Au café et au restaurant",
            "content_html_uk": """
            <h2>Як зробити замовлення французькою</h2>
            <p>Французький етикет у ресторані дуже ввічливий. Головна чарівна фраза: <strong>Je voudrais...</strong> (Я хотів(ла) би...).</p>
            <div class="example-box">
                <p><strong>Bonjour, je voudrais un café, s'il vous plaît.</strong></p>
                <p>Добрий день, я хотів би каву, будь ласка.</p>
            </div>
            <h3>Корисні фрази :</h3>
            <ul>
                <li><strong>Une table pour deux, s'il vous plaît.</strong> — Столик на двох, будь ласка.</li>
                <li><strong>La carte / Le menu</strong> — Меню.</li>
                <li><strong>Le plat du jour</strong> — Страва дня.</li>
                <li><strong>Une carafe d'eau, s'il vous plaît.</strong> — Графин безкоштовної води з-під крана.</li>
                <li><strong>L'addition, s'il vous plaît !</strong> — Рахунок, будь ласка!</li>
            </ul>
            """,
            "content_html_ru": """
            <h2>Как сделать заказ во французском заведении</h2>
            <p>Французский этикет в ресторанах очень вежлив. Ключевая волшебная фраза: <strong>Je voudrais...</strong> (Я хотел(а) бы...).</p>
            <div class="example-box">
                <p><strong>Bonjour, je voudrais un croissant et un café, s'il vous plaît.</strong></p>
                <p>Здравствуйте, я хотел бы круассан и кофе, пожалуйста.</p>
            </div>
            <h3>Полезные фразы:</h3>
            <ul>
                <li><strong>Une table pour deux, s'il vous plaît.</strong> — Столик на двоих, пожалуйста.</li>
                <li><strong>La carte / Le menu</strong> — Меню.</li>
                <li><strong>Le plat du jour</strong> — Блюдо дня.</li>
                <li><strong>Une carafe d'eau, s'il vous plaît.</strong> — Графин бесплатной столовой воды.</li>
                <li><strong>L'addition, s'il vous plaît !</strong> — Счёт, пожалуйста!</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Ordering at a French Café or Restaurant</h2>
            <p>Politeness is key in French dining culture. The magic phrase is <strong>Je voudrais...</strong> (I would like...).</p>
            <div class="example-box">
                <p><strong>Bonjour, je voudrais un café, s'il vous plaît.</strong></p>
                <p>Hello, I would like a coffee, please.</p>
            </div>
            <h3>Essential Phrases:</h3>
            <ul>
                <li><strong>Une table pour deux, s'il vous plaît.</strong> — A table for two, please.</li>
                <li><strong>Le plat du jour</strong> — Dish of the day.</li>
                <li><strong>Une carafe d'eau, s'il vous plaît.</strong> — A jug of tap water (free).</li>
                <li><strong>L'addition, s'il vous plaît !</strong> — The bill, please!</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Commander au restaurant</h2>
            <div class="example-box">
                <p><strong>Je voudrais... s'il vous plaît.</strong></p>
            </div>
            <h3>Vocabulaire utile :</h3>
            <ul>
                <li><strong>Une table pour deux personnes.</strong></li>
                <li><strong>Le plat du jour.</strong></li>
                <li><strong>Une carafe d'eau.</strong></li>
                <li><strong>L'addition, s'il vous plaît !</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Як чемно попросити рахунок у ресторані?",
                    "text_ru": "Как вежливо попросить счёт в ресторане?",
                    "text_en": "How do you politely ask for the bill in a French restaurant?",
                    "text_fr": "Comment demande-t-on l'addition poliment ?",
                    "choices": [
                        {"text": "L'addition, s'il vous plaît !", "correct": True},
                        {"text": "Donnez-moi l'argent !", "correct": False},
                        {"text": "Combien de café ?", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 23,
            "data_lesson_id": "lesson-shopping",
            "topic": topic4,
            "title_uk": "🛍️ Покупки та магазин",
            "title_ru": "🛍️ Покупки и магазин",
            "title_en": "🛍️ Shopping & Groceries",
            "title_fr": "🛍️ Faire les courses et shopping",
            "content_html_uk": """
            <h2>Як купувати та дізнаватися ціну</h2>
            <div class="example-box">
                <p><strong>Combien ça coûte ?</strong> [комб'ян са кут] — Скільки це коштує?</p>
                <p><strong>C'est combien ?</strong> [се комб'ян] — Почім це?</p>
            </div>
            <h3>Корисні фрази в магазині :</h3>
            <ul>
                <li><strong>Je cherche...</strong> — Я шукаю...</li>
                <li><strong>Avez-vous la taille M ?</strong> — У вас є розмір M?</li>
                <li><strong>Je peux essayer ?</strong> — Можна поміряти?</li>
                <li><strong>Les cabines d'essayage</strong> — Примірочні кабінки.</li>
            </ul>
            <h3>Способи оплати :</h3>
            <ul>
                <li><strong>Par carte (bancaire)</strong> — Карткою.</li>
                <li><strong>En espèces / En liquide</strong> — Готівкою.</li>
                <li><strong>Sans contact</strong> — Безконтактна оплата.</li>
            </ul>
            """,
            "content_html_ru": """
            <h2>Как совершать покупки и узнавать цену</h2>
            <div class="example-box">
                <p><strong>Combien ça coûte ?</strong> [комбьян са кут] — Сколько это стоит?</p>
                <p><strong>C'est combien ?</strong> [сэ комбьян] — Сколько с меня?</p>
            </div>
            <h3>Полезные фразы в магазине:</h3>
            <ul>
                <li><strong>Je cherche...</strong> — Я ищу...</li>
                <li><strong>Avez-vous la taille M ?</strong> — У вас есть размер M?</li>
                <li><strong>Je peux essayer ?</strong> — Могу я примерить?</li>
                <li><strong>Les cabines d'essayage</strong> — Примерочные кабины.</li>
            </ul>
            <h3>Способы оплаты:</h3>
            <ul>
                <li><strong>Par carte</strong> — Картой.</li>
                <li><strong>En espèces</strong> — Наличными.</li>
                <li><strong>Sans contact</strong> — Бесконтактно.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Shopping in French</h2>
            <div class="example-box">
                <p><strong>Combien ça coûte ?</strong> — How much does it cost?</p>
                <p><strong>C'est combien ?</strong> — How much is it?</p>
            </div>
            <h3>Useful Expressions:</h3>
            <ul>
                <li><strong>Je cherche...</strong> — I am looking for...</li>
                <li><strong>Je peux essayer ?</strong> — Can I try this on?</li>
                <li><strong>Par carte / En espèces</strong> — By card / In cash.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Faire les magasins</h2>
            <div class="example-box">
                <p><strong>Combien ça coûte ?</strong> — Demander le prix.</p>
            </div>
            <ul>
                <li><strong>Je cherche...</strong></li>
                <li><strong>Puis-je essayer ?</strong></li>
                <li><strong>Paiement par carte ou en espèces.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Як запитати 'Скільки це коштує?'",
                    "text_ru": "Как спросить 'Сколько это стоит?'",
                    "text_en": "How do you ask 'How much does it cost?' in French?",
                    "text_fr": "Comment demander le prix d'un article ?",
                    "choices": [
                        {"text": "Combien ça coûte ?", "correct": True},
                        {"text": "Où est la gare ?", "correct": False},
                        {"text": "Quelle heure est-il ?", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 24,
            "data_lesson_id": "lesson-directions",
            "topic": topic4,
            "title_uk": "🗺️ Орієнтація в місті та маршрути",
            "title_ru": "🗺️ Ориентация в городе и маршруты",
            "title_en": "🗺️ Asking for Directions",
            "title_fr": "🗺️ Demander son chemin en ville",
            "content_html_uk": """
            <h2>Як не заблукати в місті</h2>
            <div class="example-box">
                <p><strong>Pardon, où est la station de métro ?</strong></p>
                <p>Вибачте, де станція метро?</p>
            </div>
            <h3>Вказівки руху :</h3>
            <ul>
                <li><strong>Allez tout droit.</strong> [але ту друа] — Ідіть прямо.</li>
                <li><strong>Tournez à droite.</strong> [турне а друат] — Поверніть праворуч.</li>
                <li><strong>Tournez à gauche.</strong> [турне а гош] — Поверніть ліворуч.</li>
                <li><strong>C'est près d'ici.</strong> — Це близько звідси.</li>
                <li><strong>C'est loin.</strong> — Це далеко.</li>
                <li><strong>À côté de...</strong> — Поруч із...</li>
            </ul>
            """,
            "content_html_ru": """
            <h2>Как не потеряться в городе</h2>
            <div class="example-box">
                <p><strong>Pardon, où est la gare ?</strong></p>
                <p>Простите, где вокзал?</p>
            </div>
            <h3>Указания направления:</h3>
            <ul>
                <li><strong>Allez tout droit.</strong> [алэ ту друа] — Идите прямо.</li>
                <li><strong>Tournez à droite.</strong> [турнэ а друат] — Поверните направо.</li>
                <li><strong>Tournez à gauche.</strong> [турнэ а гош] — Поверните налево.</li>
                <li><strong>C'est près d'ici.</strong> — Это близко отсюда.</li>
                <li><strong>C'est loin.</strong> — Это далеко.</li>
                <li><strong>À côté de...</strong> — Рядом с...</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Asking for and Giving Directions</h2>
            <div class="example-box">
                <p><strong>Pardon, où est la gare ?</strong> — Excuse me, where is the station?</p>
            </div>
            <h3>Directions:</h3>
            <ul>
                <li><strong>Allez tout droit.</strong> — Go straight ahead.</li>
                <li><strong>Tournez à droite.</strong> — Turn right.</li>
                <li><strong>Tournez à gauche.</strong> — Turn left.</li>
                <li><strong>C'est près / C'est loin.</strong> — It is near / It is far.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Demander son chemin</h2>
            <div class="example-box">
                <p><strong>Pardon, où est la gare ?</strong></p>
            </div>
            <ul>
                <li><strong>Allez tout droit.</strong></li>
                <li><strong>Tournez à droite / à gauche.</strong></li>
                <li><strong>C'est tout près.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_uk": "Що означає 'Tournez à gauche'?",
                    "text_ru": "Что означает 'Tournez à gauche'?",
                    "text_en": "What does 'Tournez à gauche' mean?",
                    "text_fr": "Que signifie 'Tournez à gauche' ?",
                    "choices": [
                        {"text": "Поверніть ліворуч / Turn left", "correct": True},
                        {"text": "Поверніть праворуч / Turn right", "correct": False},
                        {"text": "Ідіть прямо / Go straight", "correct": False}
                    ]
                }
            ]
        }
    ]

    for l_data in lessons_data:
        questions = l_data.pop("questions")
        topic = l_data.pop("topic")
        lesson, created = Lesson.objects.update_or_create(
            data_lesson_id=l_data["data_lesson_id"],
            defaults={
                "topic": topic,
                "order": l_data["order"],
                "title": l_data["title_uk"],
                "title_uk": l_data["title_uk"],
                "title_ru": l_data["title_ru"],
                "title_en": l_data["title_en"],
                "title_fr": l_data["title_fr"],
                "content_html": l_data["content_html_uk"],
                "content_html_uk": l_data["content_html_uk"],
                "content_html_ru": l_data["content_html_ru"],
                "content_html_en": l_data["content_html_en"],
                "content_html_fr": l_data["content_html_fr"],
            }
        )
        print(f"{'Created' if created else 'Updated'} lesson: {lesson.title_ru} (Order: {lesson.order})")

        # Create or update questions
        for q_idx, q_data in enumerate(questions, 1):
            choices = q_data.pop("choices")
            question, _ = Question.objects.get_or_create(
                lesson=lesson,
                order=q_idx,
                defaults={
                    "text": q_data.get("text_uk"),
                    "text_uk": q_data.get("text_uk"),
                    "text_ru": q_data.get("text_ru"),
                    "text_en": q_data.get("text_en"),
                    "text_fr": q_data.get("text_fr"),
                }
            )
            for c_data in choices:
                Choice.objects.get_or_create(
                    question=question,
                    text=c_data["text"],
                    defaults={
                        "text_uk": c_data["text"],
                        "text_ru": c_data["text"],
                        "text_en": c_data["text"],
                        "text_fr": c_data["text"],
                        "is_correct": c_data["correct"],
                    }
                )

if __name__ == '__main__':
    seed_lessons()
    print("Done!")
