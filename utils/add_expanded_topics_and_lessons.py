"""
Script to create Topics 6 & 7 with 8 new lessons on Everyday Conversation, Culture & Belgian Traditions.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Topic, Lesson
from apps.quizzes.models import Question, Choice

def seed_expanded_topics():
    # 1. Create Topic 6: Conversation & Real-Life Dialogues
    topic6, _ = Topic.objects.get_or_create(
        order=6,
        defaults={
            'title': 'Живое общение и диалоги',
            'title_uk': 'Живе спілкування та діалоги',
            'title_ru': 'Живое общение и диалоги',
            'title_en': 'Everyday Conversation & Dialogues',
            'title_fr': 'Conversation courante et situations réelles',
            'emoji': '💬'
        }
    )
    print("Topic 6 created/updated:", topic6.title_ru)

    # 2. Create Topic 7: Culture & Belgian Traditions
    topic7, _ = Topic.objects.get_or_create(
        order=7,
        defaults={
            'title': 'Культура, традиции и комиксы Бельгии',
            'title_uk': 'Культура, традиції та комікси Бельгії',
            'title_ru': 'Культура, традиции и комиксы Бельгии',
            'title_en': 'Belgian Culture, Traditions & Comics',
            'title_fr': 'Culture, traditions et patrimoine belge',
            'emoji': '🎭'
        }
    )
    print("Topic 7 created/updated:", topic7.title_ru)

    lessons_data = [
        # --- Topic 6: Conversation ---
        {
            "order": 33,
            "data_lesson_id": "lesson-self-presentation",
            "topic": topic6,
            "title_uk": "🤝 Знайомство та розповідь про себе",
            "title_ru": "🤝 Знакомство и рассказ о себе",
            "title_en": "🤝 Introducing Yourself & Making Friends",
            "title_fr": "🤝 Se présenter et faire connaissance",
            "content_html_ru": """
            <h2>Как уверенно рассказать о себе по-французски</h2>
            <p>Шаблон самопрезентации для работы, учебы, вечеринки или новых знакомств в Бельгии:</p>

            <div class="example-box">
                <p><strong>« Bonjour ! Je m'appelle Maxime. J'ai 32 ans et je viens d'Ukraine. J'habite à Bruxelles depuis six mois. Je travaille comme développeur web. Pendant mon temps libre, j'aime voyager, lire et faire du vélo. Et vous, comment vous vous appelez ? »</strong></p>
            </div>

            <h3>Ключевые конструкции:</h3>
            <div class="conjugation-grid">
                <div><strong>Имя:</strong><br><em>Je m'appelle... / Mon prénom est...</em></div>
                <div><strong>Возраст:</strong><br><em>J'ai 28 ans</em> (с глаголом <strong>avoir</strong>, а не être!)</div>
                <div><strong>Происхождение:</strong><br><em>Je viens d'Ukraine / Je suis ukrainien(ne)</em></div>
                <div><strong>Проживание:</strong><br><em>J'habite à Liège / à Namur depuis 1 an</em></div>
                <div><strong>Профессия:</strong><br><em>Je suis comptable / médecin / étudiant</em></div>
                <div><strong>Хобби:</strong><br><em>J'aime la musique / le sport / la cuisine</em></div>
            </div>

            <h3>Вопросы собеседнику:</h3>
            <ul>
                <li><strong>« Et vous, d'où venez-vous ? »</strong> — А вы откуда?</li>
                <li><strong>« Qu'est-ce que vous faites dans la vie ? »</strong> — Чем вы занимаетесь по жизни (кем работаете)?</li>
                <li><strong>« Enchanté(e) ! »</strong> — Очень приятно познакомиться!</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Як впевнено розповісти про себе</h2>
            <div class="example-box">
                <p><strong>« Bonjour ! Je m'appelle Olena. J'ai 26 ans et je viens d'Ukraine. J'habite à Bruxelles. Enchantée ! »</strong></p>
            </div>
            <h3>Головні фрази :</h3>
            <ul>
                <li><strong>Вік:</strong> <em>J'ai ... ans</em> (з дієсловом avoir!).</li>
                <li><strong>Місто:</strong> <em>J'habite à Bruxelles depuis 6 mois.</em></li>
                <li><strong>Знайомство:</strong> <em>Enchanté(e) !</em> — Дуже приємно!</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Introducing Yourself in French</h2>
            <div class="example-box">
                <p><strong>« Bonjour, je m'appelle... J'ai ... ans. Je viens d'Ukraine. Enchanté(e) ! »</strong></p>
            </div>
            <h3>Key Phrases:</h3>
            <ul>
                <li><strong>Age:</strong> Use <em>J'ai ... ans</em> (verb avoir).</li>
                <li><strong>Profession:</strong> <em>Je suis ingénieur / designer.</em></li>
                <li><strong>Meeting:</strong> <em>Enchanté(e) !</em> (Nice to meet you!).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Se présenter et faire connaissance</h2>
            <ul>
                <li><strong>Je m'appelle...</strong></li>
                <li><strong>J'ai ... ans.</strong></li>
                <li><strong>J'habite à Bruxelles.</strong></li>
                <li><strong>Enchanté(e) !</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "С каким глаголом во французском языке называют свой возраст?",
                    "text_uk": "З яким дієсловом у французькій мові називають свій вік?",
                    "text_en": "Which verb is used in French to state your age?",
                    "text_fr": "Quel verbe utilise-t-on pour donner son âge en français ?",
                    "choices": [
                        {"text": "Avoir (J'ai ... ans)", "correct": True},
                        {"text": "Être (Je suis ... ans)", "correct": False},
                        {"text": "Faire (Je fais ... ans)", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 34,
            "data_lesson_id": "lesson-phone-calls",
            "topic": topic6,
            "title_uk": "📱 Телефонні розмови та повідомлення",
            "title_ru": "📱 Телефонные разговоры и сообщения",
            "title_en": "📱 Phone Calls & Voicemails",
            "title_fr": "📱 Téléphoner et laisser un message",
            "content_html_ru": """
            <h2>Как общаться по телефону на французском</h2>
            <p>Телефонный разговор часто пугает новичков, потому что нет визуального контакта. Разберем ключевые фразы-шаблоны:</p>

            <h3>1. Начало звонка:</h3>
            <div class="example-box">
                <p><strong>Принятие звонка:</strong> « Allô ? Bonjour ! »</p>
                <p><strong>Представиться:</strong> « Bonjour, c'est Maxime à l'appareil. » <em>(Здравствуйте, это Максим у аппарата.)</em></p>
                <p><strong>Узнать кто звонит:</strong> « C'est de la part de qui ? » <em>(Кто звонит / от кого?)</em></p>
            </div>

            <h3>2. Попросить к телефону нужного человека:</h3>
            <ul>
                <li><strong>« Est-ce que je pourrais parler à Monsieur Martin, s'il vous plaît ? »</strong> <em>(Могу ли я поговорить с господином Мартеном?)</em></li>
                <li><strong>« Je vous appelle au sujet de mon rendez-vous / de l'annonce pour l'appartement. »</strong> <em>(Я звоню по поводу моей записи / объявления о квартире.)</em></li>
                <li><strong>« Un instant, je vous prie. Ne quittez pas. »</strong> <em>(Один момент, пожалуйста. Не вешайте трубку.)</em></li>
            </ul>

            <h3>3. Спасительные фразы при плохой слышимости:</h3>
            <div class="example-box warning">
                <p><strong>« Pourriez-vous répéter plus lentement, s'il vous plaît ? »</strong> — Не могли бы вы повторить медленнее?</p>
                <p><strong>« La ligne est mauvaise, je vous entends mal. »</strong> — Связь плохая, я вас плохо слышу.</p>
                <p><strong>« Pourriez-vous épeler votre nom ? »</strong> — Продиктуйте ваше имя по буквам, пожалуйста.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Телефонні розмови французькою</h2>
            <div class="example-box">
                <p><strong>« Allô ? C'est Maxime à l'appareil. »</strong> — Алло, це Максим біля телефону.</p>
                <p><strong>« Pourriez-vous répéter plus lentement, s'il vous plaît ? »</strong> — Повторіть повільніше, будь ласка.</p>
            </div>
            """,
            "content_html_en": """
            <h2>Making Phone Calls in French</h2>
            <ul>
                <li><strong>« Allô ? C'est ... à l'appareil. »</strong> — Hello, this is ... speaking.</li>
                <li><strong>« C'est de la part de qui ? »</strong> — Who is calling, please?</li>
                <li><strong>« Ne quittez pas. »</strong> — Please hold the line.</li>
                <li><strong>« Pourriez-vous répéter plus lentement ? »</strong> — Could you speak more slowly?</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Au téléphone en français</h2>
            <ul>
                <li><strong>« Allô ? C'est ... à l'appareil. »</strong></li>
                <li><strong>« Un instant, ne quittez pas. »</strong></li>
                <li><strong>« Pourriez-vous répéter plus lentement ? »</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Как вежливо попросить собеседника говорить медленнее по телефону?",
                    "text_uk": "Як чемно попросити співрозмовника говорити повільніше телефоном?",
                    "text_en": "How do you politely ask someone to speak more slowly on the phone?",
                    "text_fr": "Comment demander poliment de parler plus lentement au téléphone ?",
                    "choices": [
                        {"text": "Pourriez-vous répéter plus lentement, s'il vous plaît ?", "correct": True},
                        {"text": "Parlez plus fort !", "correct": False},
                        {"text": "Au revoir et merci", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 35,
            "data_lesson_id": "lesson-invitations",
            "topic": topic6,
            "title_uk": "🎉 Запрошення, свята та зустрічі",
            "title_ru": "🎉 Приглашения, праздники и встречи",
            "title_en": "🎉 Invitations, Holidays & Socializing",
            "title_fr": "🎉 Inviter, fêtes et rencontres",
            "content_html_ru": """
            <h2>Как пригласить друзей и отметить праздник в Бельгии</h2>
            <p>Бельгийцы очень ценят дружеские посиделки за бокалом пива или кофе. Вот как организовать встречу:</p>

            <h3>1. Приглашение на встречу:</h3>
            <div class="example-box">
                <p><strong>« Ça te dit d'aller boire un verre ce soir ? »</strong> <em>(Не хочешь пойти выпить по бокалу сегодня вечером?)</em></p>
                <p><strong>« On se voit ce week-end ? »</strong> <em>(Увидимся на этих выходных?)</em></p>
                <p><strong>« Tu es libre vendredi soir ? »</strong> <em>(Ты свободен(на) в пятницу вечером?)</em></p>
            </div>

            <h3>2. Как ответить:</h3>
            <div class="conjugation-grid">
                <div><strong>Согласие:</strong><br><em>« Avec grand plaisir ! »</em> (С большим удовольствием!)<br><em>« Ça marche ! / C'est d'accord ! »</em> (Договорились!)</div>
                <div><strong>Вежливый отказ:</strong><br><em>« Je suis désolé(e), je ne suis pas libre. »</em><br><em>« Une autre fois avec plaisir ! »</em> (С удовольствием в другой раз!)</div>
            </div>

            <h3>3. Главные бельгийские праздники и поздравления:</h3>
            <ul>
                <li><strong>La Saint-Nicolas (6 декабря)</strong> — Главный детский праздник в Бельгии! Святой Николай дарит детям мандарины, пряники <em>spéculoos</em> и фигурки из шоколада.</li>
                <li><strong>Joyeux anniversaire !</strong> — С днём рождения!</li>
                <li><strong>Joyeux Noël et Bonne Année !</strong> — Счастливого Рождества и Нового года!</li>
                <li><strong>Santé ! / À la vôtre ! / À la tienne !</strong> — Ваше здоровье! (Тост при звоне бокалов — обязательно смотреть в глаза!).</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Запрошення та свята в Бельгії</h2>
            <div class="example-box">
                <p><strong>« Ça te dit d'aller boire un verre ? »</strong> — Як щодо піти випити кави/напою?</p>
                <p><strong>« Santé ! »</strong> — Будьмо! (Тост за здоров'я).</p>
                <p><strong>La Saint-Nicolas (6 грудня)</strong> — День Святого Миколая (головне свято малечі в Бельгії).</p>
            </div>
            """,
            "content_html_en": """
            <h2>Socializing & Invitations in Belgium</h2>
            <ul>
                <li><strong>« Ça te dit d'aller boire un verre ? »</strong> — Fancy grabbing a drink?</li>
                <li><strong>« Avec plaisir ! »</strong> — With pleasure!</li>
                <li><strong>« Santé ! »</strong> — Cheers!</li>
                <li><strong>Saint-Nicolas (Dec 6)</strong>: Iconic Belgian holiday with spéculoos and chocolate.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Inviter et célébrer en Belgique</h2>
            <ul>
                <li><strong>« Ça te dit d'aller boire un verre ? »</strong></li>
                <li><strong>« Avec grand plaisir ! »</strong></li>
                <li><strong>« Santé ! »</strong></li>
                <li><strong>La Saint-Nicolas le 6 décembre.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какая фраза используется как тост при чоканье бокалами?",
                    "text_uk": "Яка фраза використовується як тост під час цокання келихами?",
                    "text_en": "Which word is said as a toast when clinking glasses?",
                    "text_fr": "Que dit-on pour trinquer en français ?",
                    "choices": [
                        {"text": "Santé ! / À la tienne !", "correct": True},
                        {"text": "Bon appétit !", "correct": False},
                        {"text": "Bonne chance !", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 36,
            "data_lesson_id": "lesson-emergencies",
            "topic": topic6,
            "title_uk": "⚠️ Екстрені ситуації та екстрена допомога",
            "title_ru": "⚠️ Экстренные ситуации и экстренная помощь",
            "title_en": "⚠️ Emergencies & Seeking Help",
            "title_fr": "⚠️ Urgences et demander de l'aide",
            "content_html_ru": """
            <h2>Экстренные номера и вызов помощи в Бельгии</h2>
            <p>Номера экстренных служб, которые должен знать каждый житель Бельгии:</p>

            <div class="conjugation-grid">
                <div><strong>📞 112</strong><br>Единый европейский номер экстренной помощи (бесплатно, работает на фр./англ./нидерл.)</div>
                <div><strong>📞 101</strong><br>Полиция Бельгии (Police secours)</div>
                <div><strong>📞 100</strong><br>Скорая помощь и пожарные (Ambulance / Pompiers)</div>
                <div><strong>📞 070 245 245</strong><br>Антидот / Токсикологический центр (Centre Antipoisons)</div>
            </div>

            <h3>Ключевые фразы при опасности и вызове помощи:</h3>
            <div class="example-box warning">
                <p><strong>« Au secours ! / À l'aide ! »</strong> — На помощь!</p>
                <p><strong>« Il y a eu un accident grave au coin de la rue. »</strong> — Произошла серьезная авария на углу улицы.</p>
                <p><strong>« Quelqu'un est blessé / est tombé inconscient. »</strong> — Кто-то ранен / потерял сознание.</p>
                <p><strong>« J'ai besoin d'une ambulance immédiatement. »</strong> — Мне срочно нужна скорая помощь.</p>
                <p><strong>« J'ai perdu mon passeport et mon portefeuille. »</strong> — Я потерял свой паспорт и кошелек.</p>
                <p><strong>« On m'a volé mon téléphone / mon sac. »</strong> — У меня украли телефон / сумку.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Екстрені служби та допомога в Бельгії</h2>
            <h3>Головні номери :</h3>
            <ul>
                <li><strong>112</strong> — Загальний екстрений номер допомоги.</li>
                <li><strong>101</strong> — Поліція.</li>
            </ul>
            <div class="example-box">
                <p><strong>« Au secours ! »</strong> — Допоможіть!</p>
                <p><strong>« J'ai besoin d'une ambulance. »</strong> — Мені потрібна швидка допомога.</p>
            </div>
            """,
            "content_html_en": """
            <h2>Emergency Numbers & Asking for Help in Belgium</h2>
            <ul>
                <li><strong>112</strong>: General European emergency number.</li>
                <li><strong>101</strong>: Belgian Police emergency.</li>
                <li><strong>« Au secours ! / À l'aide ! »</strong>: Help!</li>
                <li><strong>« J'ai besoin d'une ambulance immédiatement. »</strong>: I need an ambulance right away.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Numéros d'urgence en Belgique</h2>
            <ul>
                <li><strong>112</strong> : Urgences européennes.</li>
                <li><strong>101</strong> : Police secours.</li>
                <li><strong>« Au secours ! / À l'aide ! »</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какой единый европейский номер экстренных служб действует в Бельгии?",
                    "text_uk": "Який єдиний європейський номер екстрених служб діє в Бельгії?",
                    "text_en": "What is the single European emergency number in Belgium?",
                    "text_fr": "Quel est le numéro d'urgence européen en Belgique ?",
                    "choices": [
                        {"text": "112", "correct": True},
                        {"text": "911", "correct": False},
                        {"text": "999", "correct": False}
                    ]
                }
            ]
        },

        # --- Topic 7: Belgian Culture & Heritage ---
        {
            "order": 37,
            "data_lesson_id": "lesson-chocolate-beer",
            "topic": topic7,
            "title_uk": "🍫 Бельгійський шоколад, пиво та гастрономія",
            "title_ru": "🍫 Бельгийский шоколад, пиво и гастрономия",
            "title_en": "🍫 Belgian Chocolate, Beer & Culinary Heritage",
            "title_fr": "🍫 Le chocolat, la bière et la gastronomie belge",
            "content_html_ru": """
            <h2>Шоколад и пиво — гордость Бельгии</h2>
            <p>Бельгия признана мировой столицей шоколада и пивоварения с вековыми традициями:</p>

            <h3>1. Бельгийский шоколад и пралине:</h3>
            <p>В 1912 году в Брюсселе Жан Нойхаус (<strong>Jean Neuhaus</strong>) изобрел <strong>пралине (la praline)</strong> — шоколадную конфету с нежной начинкой из орехов, карамели или ганаша.</p>
            <ul>
                <li><strong>Les maîtres chocolatiers</strong> — Знаменитые шоколадные дома: <em>Neuhaus, Leonidas, Pierre Marcolini, Godiva, Côte d'Or</em>.</li>
                <li><strong>Un ballotin</strong> — Фирменная коробочка для конфет-пралине, защищающая их форму.</li>
                <li><strong>Chocolat noir / au lait / blanc</strong> — Черный / молочный / белый шоколад.</li>
            </ul>

            <h3>2. Бельгийская пивная культура (ЮНЕСКО):</h3>
            <p>Бельгийская пивная культура внесена в список нематериального культурного наследия ЮНЕСКО! В стране производят более 1500 сортов пива:</p>
            <ul>
                <li><strong>Bières trappistes</strong> — Траппистские монастырские эли (<em>Chimay, Orval, Westmalle, Rochefort, Westvleteren</em>).</li>
                <li><strong>La Gueuze / Kriek</strong> — Пиво спонтанного брожения (ламбик) с вишней или малиной.</li>
                <li><strong>Le calice / Le verre adapté</strong> — У каждого бельгийского пива свой уникальный бокал! Наливать пиво в чужой бокал в Бельгии считается святотатством.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Шоколад та пиво Бельгії (Спадщина ЮНЕСКО)</h2>
            <ul>
                <li><strong>La praline</strong> — Шоколадна цукерка з начинкою (винайдена в Брюсселі в 1912 р.).</li>
                <li><strong>Un ballotin</strong> — Фірмова коробочка для цукерок.</li>
                <li><strong>Bières trappistes</strong> — Трапістські монастирські елі (Orval, Chimay).</li>
                <li><strong>Gueuze / Kriek</strong> — Традиційний брюссельський ламбік з вишнею.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Belgian Chocolate & Beer Culture</h2>
            <ul>
                <li><strong>Pralines</strong>: Filled chocolate bites invented in Brussels in 1912 by Neuhaus.</li>
                <li><strong>Trappist Beers</strong>: Authentic monastery-brewed ales (Chimay, Orval, Westmalle).</li>
                <li><strong>UNESCO Heritage</strong>: Belgian beer culture with unique glasses for every single beer!</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le chocolat et la bière en Belgique</h2>
            <ul>
                <li><strong>La praline</strong> inventée en 1912 à Bruxelles.</li>
                <li><strong>Les bières trappistes</strong> (Chimay, Orval, Westmalle).</li>
                <li><strong>Patrimoine immatériel de l'UNESCO.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "В каком городе в 1912 году было изобретено шоколадное пралине (la praline)?",
                    "text_uk": "У якому місті в 1912 році було винайдено шоколадне праліне (la praline)?",
                    "text_en": "In which city was the chocolate praline invented in 1912?",
                    "text_fr": "Dans quelle ville la praline a-t-elle été inventée en 1912 ?",
                    "choices": [
                        {"text": "В Брюсселе (Bruxelles)", "correct": True},
                        {"text": "В Париже (Paris)", "correct": False},
                        {"text": "В Женеве (Genève)", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 38,
            "data_lesson_id": "lesson-belgian-comics",
            "topic": topic7,
            "title_uk": "🎨 Бельгійський комікс: Тінтін, Смурфики та графічні романи",
            "title_ru": "🎨 Бельгийский комикс: Тинтин, Смурфики и BD",
            "title_en": "🎨 Belgian Comics (BD): Tintin, Smurfs & Franco-Belgian Heritage",
            "title_fr": "🎨 La bande dessinée belge (BD) : Tintin et les Schtroumpfs",
            "content_html_ru": """
            <h2>Бельгия — мировая столица комиксов (La BD)</h2>
            <p>В Бельгии комиксы называют <strong>Le 9e Art (Девятое искусство)</strong>. Это национальная гордость и важная часть франкоязычной культуры:</p>

            <h3>1. Легендарные герои и авторы:</h3>
            <ul>
                <li><strong>Tintin (Тинтин)</strong> — Молодой репортер и его верный фокстерьер Милу (<em>Milou</em>), созданные брюссельским художником Эрже (<strong>Hergé</strong>).</li>
                <li><strong>Les Schtroumpfs (Смурфики)</strong> — Синие сказочные гномики, придуманные бельгийцем Пейо (<strong>Peyo</strong>).</li>
                <li><strong>Lucky Luke (Счастливчик Люк)</strong> — Ковбой, который стреляет быстрее своей тени, от автора Морриса (<strong>Morris</strong>).</li>
                <li><strong>Gaston Lagaffe (Гастон Лагафф)</strong> — Добрый и неуклюжий офисный изобретатель от Франкена (<strong>Franquin</strong>).</li>
            </ul>

            <h3>2. Брюссель — музей комиксов под открытым небом:</h3>
            <div class="example-box">
                <p><strong>Le Parcours BD</strong> — В Брюсселе более 60 огромных граффити-фресок на стенах домов с персонажами бельгийских комиксов!</p>
                <p><strong>Le CBBD (Centre Belge de la Bande Dessinée)</strong> — Знаменитый музей комиксов в здании стиля модерн архитектора Виктора Орта.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Бельгія — столиця коміксів (La BD)</h2>
            <p>Комікси в Бельгії — це 9-те мистецтво (<em>Le 9e Art</em>):</p>
            <ul>
                <li><strong>Tintin</strong> від художника Hergé.</li>
                <li><strong>Les Schtroumpfs (Смурфики)</strong> від Peyo.</li>
                <li><strong>Lucky Luke</strong> від Morris.</li>
                <li><strong>Le Parcours BD</strong> — Маршрут фресок на фасадах Брюсселя.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Belgian Comic Strips (La Bande Dessinée)</h2>
            <ul>
                <li><strong>Tintin & Snowy (Milou)</strong> by Hergé.</li>
                <li><strong>The Smurfs (Les Schtroumpfs)</strong> by Peyo.</li>
                <li><strong>Lucky Luke</strong> by Morris.</li>
                <li><strong>Comic Strip Route</strong>: Over 60 giant murals on buildings across Brussels.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>La bande dessinée belge (Le 9e Art)</h2>
            <ul>
                <li><strong>Tintin</strong> d'Hergé.</li>
                <li><strong>Les Schtroumpfs</strong> de Peyo.</li>
                <li><strong>Le Centre Belge de la BD à Bruxelles.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Кто создал всемирно известного персонажа комиксов Тинтина (Tintin)?",
                    "text_uk": "Хто створив всесвітньо відомого персонажа коміксів Тінтіна (Tintin)?",
                    "text_en": "Who created the famous comic book character Tintin?",
                    "text_fr": "Qui est le créateur de Tintin ?",
                    "choices": [
                        {"text": "Hergé (Эрже)", "correct": True},
                        {"text": "Peyo (Пейо)", "correct": False},
                        {"text": "Victor Horta (Виктор Орта)", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 39,
            "data_lesson_id": "lesson-festivals-folklore",
            "topic": topic7,
            "title_uk": "🎭 Карнавали та фольклор Бельгії: Бінш, Монс та Гент",
            "title_ru": "🎭 Карнавалы и фольклор Бельгии: Бинш, Монс и Гент",
            "title_en": "🎭 Belgian Carnivals & Folklore: Binche, Mons & Ghent",
            "title_fr": "🎭 Carnavals et folklore belge : Binche et Mons",
            "content_html_ru": """
            <h2>Фольклорные традиции и карнавалы Бельгии</h2>
            <p>Бельгийский фольклор — один из самых красочных и живых в Европе:</p>

            <h3>1. Карнавал в Бинше (Le Carnaval de Binche):</h3>
            <p>Признан шедевром устного и нематериального наследия ЮНЕСКО. В Жирный вторник (<em>Mardi Gras</em>) на улицы выходят <strong>Жилли (Les Gilles)</strong> в восковых масках, пышных костюмах со страусиными перьями и бросают в толпу спелые апельсины на счастье!</p>

            <h3>2. Дюкасс в Монсе (La Ducasse de Mons / Le Doudou):</h3>
            <p>Традиционный праздник в городе Монс, где рыцарь Святой Георгий сражается с огромным зеленым Драконом (<em>Combat du Lumeçon</em>). Зрители пытаются сорвать волос с хвоста Дракона на удачу.</p>

            <h3>3. Гентские праздники и Омеганг в Брюсселе:</h3>
            <ul>
                <li><strong>Gentse Feesten</strong> — 10-дневный грандиозный музыкально-театральный фестиваль под открытым небом.</li>
                <li><strong>L'Ommegang</strong> — Историческая реконструкция въезда императора Карла V на Гран-Плас в Брюсселе в 1549 году.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Фольклор та карнавали Бельгії (ЮНЕСКО)</h2>
            <ul>
                <li><strong>Carnaval de Binche</strong> — Жилі (Gilles) у масках, що кидають апельсини на щастя.</li>
                <li><strong>Le Doudou à Mons</strong> — Битва Святого Георгія з Драконом.</li>
                <li><strong>L'Ommegang</strong> — Історична процесія на Grand-Place у Брюсселі.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Belgian Folklore & Festivals</h2>
            <ul>
                <li><strong>Carnival of Binche</strong>: UNESCO-listed carnival where Gilles in wax masks throw blood oranges.</li>
                <li><strong>Ducasse de Mons (Le Doudou)</strong>: Historic battle of Saint George against the Dragon.</li>
                <li><strong>L'Ommegang</strong>: Renaissance pageant on the Grand-Place in Brussels.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le folklore et les traditions en Belgique</h2>
            <ul>
                <li><strong>Le Carnaval de Binche</strong> et les Gilles (UNESCO).</li>
                <li><strong>Le Doudou de Mons.</strong></li>
                <li><strong>L'Ommegang de Bruxelles.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Что бросают зрителям персонажи 'Жилли' (Les Gilles) на карнавале в Бинше на счастье?",
                    "text_uk": "Що кидають глядачам персонажі 'Жилі' (Les Gilles) на карнавалі в Бінші на щастя?",
                    "text_en": "What do the Gilles throw to the crowd for good luck at the Binche Carnival?",
                    "text_fr": "Que lancent les Gilles de Binche à la foule ?",
                    "choices": [
                        {"text": "Апельсины (Des oranges)", "correct": True},
                        {"text": "Конфеты (Des bonbons)", "correct": False},
                        {"text": "Монеты (Des pièces de monnaie)", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 40,
            "data_lesson_id": "lesson-belgian-cities",
            "topic": topic7,
            "title_uk": "🏰 Міста та перлини Бельгії: Брюссель, Брюгге, Гент, Льєж",
            "title_ru": "🏰 Города и жемчужины Бельгии: Брюссель, Брюгге, Гент, Льеж",
            "title_en": "🏰 Belgian Cities & Landmarks: Brussels, Bruges, Ghent & Liège",
            "title_fr": "🏰 Les villes belges : Bruxelles, Bruges, Gand et Liège",
            "content_html_ru": """
            <h2>Путешествия по Бельгии: главные города и достопримечательности</h2>
            <p>Бельгия компактна: за 1–2 часа на поезде можно добраться до любого исторического центра!</p>

            <h3>1. Bruxelles (Брюссель):</h3>
            <ul>
                <li><strong>La Grand-Place</strong> — Одна из красивейших площадей мира с Ратушей (<em>Hôtel de Ville</em>) и Домом Короля.</li>
                <li><strong>Manneken-Pis</strong> — Знаменитая бронзовая статуя-фонтан с гардеробом из более чем 1000 костюмов.</li>
                <li><strong>L'Atomium</strong> — Символ Всемирной выставки 1958 года, увеличенная в 165 миллиардов раз молекула железа.</li>
            </ul>

            <h3>2. Bruges & Gand (Брюгге и Гент):</h3>
            <ul>
                <li><strong>Bruges (Брюгге)</strong> — «Северная Венеция» с живописными каналами, мостиками и башней Беффруа (<em>Le Beffroi</em>).</li>
                <li><strong>Gand (Гент)</strong> — Студенческий город со средневековым замком графов Фландрии (<em>Château des Comtes / Gravensteen</em>).</li>
            </ul>

            <h3>3. Liège, Namur & Dinant (Валлония):</h3>
            <ul>
                <li><strong>Liège (Льеж)</strong> — Город с впечатляющим футуристическим вокзалом архитектора Калатравы (<em>Liège-Guillemins</em>) и лестницей Монтань-де-Бюрен (374 ступени!).</li>
                <li><strong>Dinant (Динан)</strong> — Живописный город на реке Маас со скальной Цитаделью, родина изобретателя саксофона Адольфа Сакса (<strong>Adolphe Sax</strong>).</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Міста та перлини Бельгії</h2>
            <ul>
                <li><strong>Брюссель:</strong> Grand-Place, Manneken-Pis, Atomium.</li>
                <li><strong>Брюгге:</strong> «Північна Венеція» з каналами та дзвіницею Беффруа.</li>
                <li><strong>Гент:</strong> Замок графів Фландрії (Gravensteen).</li>
                <li><strong>Динан:</strong> Батьківщина саксофона (Адольф Сакс) та скельна цитадель.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Belgian Cities and Must-See Gems</h2>
            <ul>
                <li><strong>Brussels</strong>: Grand-Place, Manneken-Pis, Atomium.</li>
                <li><strong>Bruges</strong>: The Venice of the North with canals and belfry.</li>
                <li><strong>Dinant</strong>: Birthplace of the saxophone (Adolphe Sax) beneath the cliffside citadel.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les joyaux de la Belgique</h2>
            <ul>
                <li><strong>Bruxelles</strong> : Grand-Place, Manneken-Pis, Atomium.</li>
                <li><strong>Bruges et Gand</strong> : canaux et châteaux flamands.</li>
                <li><strong>Dinant</strong> : patrie d'Adolphe Sax, inventeur du saxophone.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "В каком бельгийском городе родился изобретатель саксофона Адольф Сакс?",
                    "text_uk": "У якому бельгійському місті народився винахідник саксофона Адольф Сакс?",
                    "text_en": "In which Belgian city was saxophone inventor Adolphe Sax born?",
                    "text_fr": "Dans quelle ville belge l'inventeur du saxophone Adolphe Sax est-il né ?",
                    "choices": [
                        {"text": "Динан (Dinant)", "correct": True},
                        {"text": "Брюгге (Bruges)", "correct": False},
                        {"text": "Антверпен (Anvers)", "correct": False}
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

        Question.objects.filter(lesson=lesson).delete()
        for q_idx, q_data in enumerate(questions, 1):
            choices = q_data.pop("choices")
            question = Question.objects.create(
                lesson=lesson,
                order=q_idx,
                text=q_data.get("text_ru"),
                text_uk=q_data.get("text_uk"),
                text_ru=q_data.get("text_ru"),
                text_en=q_data.get("text_en"),
                text_fr=q_data.get("text_fr"),
            )
            for c_data in choices:
                Choice.objects.create(
                    question=question,
                    text=c_data["text"],
                    text_uk=c_data["text"],
                    text_ru=c_data["text"],
                    text_en=c_data["text"],
                    text_fr=c_data["text"],
                    is_correct=c_data["correct"],
                )

if __name__ == '__main__':
    seed_expanded_topics()
    print("Expanded topics and lessons successfully added!")
