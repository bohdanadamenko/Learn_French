"""
Script to adapt and expand French lessons specifically for living in Belgium (Belgian French, Culture, Daily Life, and Belgicismes).
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

def enrich_belgian_content():
    # 1. Update lesson-be (Бельгийские особенности) with rich real-life Belgian guide
    lesson_be = Lesson.objects.filter(data_lesson_id="lesson-be").first()
    if lesson_be:
        lesson_be.title_uk = "🇧🇪 Бельгійські особливості та бельгіцизми"
        lesson_be.title_ru = "🇧🇪 Бельгийские особенности и бельгицизмы"
        lesson_be.title_en = "🇧🇪 Belgian French & Belgicisms"
        lesson_be.title_fr = "🇧🇪 Le français de Belgique et belgicismes"

        lesson_be.content_html_ru = """
        <h2>Французский в Бельгии: практический гид</h2>
        <p>Бельгийский французский более логичен и дружелюбен, чем парижский! Вот главные правила, которые нужно знать с первого дня в Бельгии:</p>

        <h3>1. Главные числа: 70 и 90</h3>
        <p>В Бельгии не используют французские уравнения 60+10 и 80+10. Здесь всё логично:</p>
        <div class="example-box">
            <p>70 — <strong>Septante</strong> [септант] (а не <em>soixante-dix</em>)</p>
            <p>90 — <strong>Nonante</strong> [нонант] (а не <em>quatre-vingt-dix</em>)</p>
            <p><em>(80 в Бельгии остаётся quatre-vingts [катр-вэн]).</em></p>
        </div>

        <h3>2. Приёмы пищи (Важно не перепутать!)</h3>
        <div class="conjugation-grid">
            <div><strong>🕗 Утро:</strong><br><strong>Le déjeuner</strong><br>Завтрак</div>
            <div><strong>🕛 День:</strong><br><strong>Le dîner</strong><br>Обед</div>
            <div><strong>🕕 Вечер:</strong><br><strong>Le souper</strong><br>Ужин</div>
        </div>
        <div class="example-box warning">
            <strong>Осторожно:</strong> Во Франции <em>déjeuner</em> — это обед, а <em>dîner</em> — ужин. В Бельгии, если вас зовут на <em>déjeuner</em>, это приглашение на утренний кофе с круассанами!
        </div>

        <h3>3. «S'il vous plaît» при передаче предметов</h3>
        <p>В магазине или кафе, когда бельгиец отдаёт вам сдачу, чек или товар, он говорит: <strong>«S'il vous plaît !»</strong> (в значении <em>«Вот, пожалуйста / держите»</em>). Вы отвечаете: <strong>«Merci !»</strong>.</p>

        <h3>4. «Savoir» вместо «Pouvoir»</h3>
        <p>В Бельгии для вежливой просьбы часто используют глагол <strong>savoir</strong> (знать/уметь) вместо <em>pouvoir</em> (мочь):</p>
        <div class="example-box">
            <p><strong>Tu sais me passer le sel ?</strong> = Можешь передать мне соль?</p>
            <p><strong>Vous savez m'aider ?</strong> = Вы можете мне помочь?</p>
        </div>

        <h3>5. Популярные бельгийские слова в быту:</h3>
        <ul>
            <li><strong>Un GSM</strong> [же-эс-эм] — Мобильный телефон (во Франции: <em>un portable</em>).</li>
            <li><strong>Un pistolet</strong> — Круглая хрустящая булочка для завтрака/ланча.</li>
            <li><strong>Un essuie</strong> (de bain / de vaisselle) — Полотенце (во Франции: <em>serviette / torchon</em>).</li>
            <li><strong>Une drache</strong> — Сильный проливной дождь (<em>«Il drache !»</em> — Льет как из ведра!).</li>
            <li><strong>Un kot</strong> — Студенческая комната / студия в аренду.</li>
            <li><strong>Un brol</strong> — Беспорядок, куча мелких вещей, барахолка.</li>
        </ul>
        """

        lesson_be.content_html_uk = """
        <h2>Французька в Бельгії: практичний путівник</h2>
        <p>Бельгійська французька простіша, логічніша та дуже привітна! Ось головні правила, які обов'язково треба знати в Бельгії:</p>

        <h3>1. Головні числа: 70 та 90</h3>
        <div class="example-box">
            <p>70 — <strong>Septante</strong> [септант] (замість <em>soixante-dix</em>)</p>
            <p>90 — <strong>Nonante</strong> [нонант] (замість <em>quatre-vingt-dix</em>)</p>
            <p><em>(80 у Бельгії залишається quatre-vingts).</em></p>
        </div>

        <h3>2. Прийоми їжі протягом дня</h3>
        <div class="conjugation-grid">
            <div><strong>🕗 Ранок:</strong><br><strong>Le déjeuner</strong><br>Сніданок</div>
            <div><strong>🕛 День:</strong><br><strong>Le dîner</strong><br>Обід</div>
            <div><strong>🕕 Вечір:</strong><br><strong>Le souper</strong><br>Вечеря</div>
        </div>

        <h3>3. «S'il vous plaît» під час передачі речей</h3>
        <p>У бельгійській крамниці, коли касир передає решту чи чек, він каже: <strong>«S'il vous plaît !»</strong> (у значенні <em>«Ось, тримайте, будь ласка»</em>). У відповідь кажіть: <strong>«Merci !»</strong>.</p>

        <h3>4. «Savoir» замість «Pouvoir»</h3>
        <p>У Бельгії для прохання вживають <strong>savoir</strong> замість <em>pouvoir</em>:</p>
        <div class="example-box">
            <p><strong>Tu sais me passer le sel ?</strong> = Можеш передати мені сіль?</p>
            <p><strong>Vous savez m'aider ?</strong> = Ви можете мені допомогти?</p>
        </div>

        <h3>5. Популярні бельгіцизми:</h3>
        <ul>
            <li><strong>Un GSM</strong> — Мобільний телефон (у Франції: <em>un portable</em>).</li>
            <li><strong>Un pistolet</strong> — Традиційна хрустка кругла булочка.</li>
            <li><strong>Un essuie</strong> — Рушник.</li>
            <li><strong>Une drache</strong> — Сильна злива (<em>«Il drache !»</em> — Ллє як з відра!).</li>
            <li><strong>Un kot</strong> — Орендована студентська кімната.</li>
            <li><strong>Un brol</strong> — Дрібниці, мотлох, безлад.</li>
        </ul>
        """
        lesson_be.save()
        print("Updated lesson-be with rich Belgian details.")

    topic4 = Topic.objects.get(order=4) # 🌍 Лексика та теми

    # 2. Add New Belgian Lessons:
    new_belgian_lessons = [
        {
            "order": 25,
            "data_lesson_id": "lesson-friterie",
            "topic": topic4,
            "title_uk": "🍟 Бельгійська фритюрня та гастрономія",
            "title_ru": "🍟 Бельгийская фритюрня и гастрономия",
            "title_en": "🍟 Belgian Friterie & Gastronomy",
            "title_fr": "🍟 La friterie et la gastronomie belge",
            "content_html_ru": """
            <h2>Как делать заказ в бельгийской фритюрне (La Friterie)</h2>
            <p>Фритюрня (<em>la friterie / fritkot</em>) — сердце бельгийской уличной кухни. Картофель фри здесь обжаривают дважды в говяжьем жире до золотистой корочки!</p>

            <div class="example-box">
                <p><strong>« Bonjour ! Un cornet de frites moyen avec sauce andalouse, s'il vous plaît. »</strong></p>
                <p>Здравствуйте! Средний кулек картофеля фри с соусом андалуз, пожалуйста.</p>
            </div>

            <h3>Популярные соусы в Бельгии:</h3>
            <ul>
                <li><strong>Sauce Andalouse</strong> — Легендарный бельгийский соус (майонез, томаты, специи).</li>
                <li><strong>Sauce Samouraï</strong> — Острый соус с перцем чили.</li>
                <li><strong>Sauce Brazil / Riche</strong> — Сладковато-пряный соус с ананасом/карри.</li>
                <li><strong>Tartare maison</strong> — Домашний соус тартар с травами.</li>
                <li><strong>Mayonnaise</strong> — Классический густой бельгийский майонез.</li>
            </ul>

            <h3>Мясные закуски (Les snacks) :</h3>
            <ul>
                <li><strong>Une fricadelle</strong> [фрикадель] — Традиционная продолговатая мясная колбаска.</li>
                <li><strong>Une mitraillette</strong> [митрайет] — Знаменитый бельгийский багет, начиненный мясом, горой картошки фри и соусом.</li>
                <li><strong>Des boulets liégeois</strong> — Мясные тефтели в кисло-сладком соусе из Льежского сиропа.</li>
            </ul>

            <h3>Вафли: Льежские vs Брюссельские</h3>
            <div class="conjugation-grid">
                <div><strong>Gaufre de Liège:</strong><br>Круглая, плотная, с кусочками карамелизованного сахара. Едят тёплой без начинок прямо на ходу!</div>
                <div><strong>Gaufre de Bruxelles:</strong><br>Прямоугольная, лёгкая и хрустящая. Подается на тарелке с сахарной пудрой, клубникой или взбитыми сливками.</div>
            </div>
            """,
            "content_html_uk": """
            <h2>Як замовляти у бельгійській фритюрні (La Friterie)</h2>
            <p>Фритюрня (<em>la friterie / fritkot</em>) — культове місце бельгійської гастрономії. Фрі тут смажать двічі до хрусткої скоринки!</p>

            <div class="example-box">
                <p><strong>« Bonjour ! Un grand cornet de frites avec sauce andalouse, s'il vous plaît. »</strong></p>
                <p>Добрий день! Великий кульок фрі з соусом андалуз, будь ласка.</p>
            </div>

            <h3>Культові бельгійські соуси :</h3>
            <ul>
                <li><strong>Sauce Andalouse</strong> — Фірмовий соус (майонез, томати, перчик).</li>
                <li><strong>Sauce Samouraï</strong> — Гострий соус з чилі.</li>
                <li><strong>Tartare maison</strong> — Домашній тартар з травами.</li>
            </ul>

            <h3>Вафлі: Льєжські чи Брюссельські?</h3>
            <div class="conjugation-grid">
                <div><strong>Gaufre de Liège:</strong><br>Щільна, з перлинним цукром. Їдять теплою без добавок.</div>
                <div><strong>Gaufre de Bruxelles:</strong><br>Прямокутна, повітряна, хрустка, з цукровою пудрою.</div>
            </div>
            """,
            "content_html_en": """
            <h2>Ordering at a Belgian Friterie</h2>
            <p>The <em>friterie</em> (or <em>fritkot</em>) is an essential part of Belgian culture!</p>
            <div class="example-box">
                <p><strong>« Un cornet de frites avec sauce andalouse, s'il vous plaît. »</strong></p>
            </div>
            <h3>Famous Belgian Sauces:</h3>
            <ul>
                <li><strong>Sauce Andalouse</strong> — Creamy, tomato-based spiced sauce.</li>
                <li><strong>Sauce Samouraï</strong> — Spicy chili mayo.</li>
                <li><strong>Sauce Brazil</strong> — Sweet pineapple-curry sauce.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>À la friterie belge</h2>
            <div class="example-box">
                <p><strong>« Un cornet de frites avec sauce andalouse et une fricadelle, s'il vous plaît ! »</strong></p>
            </div>
            <ul>
                <li><strong>Gaufre de Liège</strong> : dense avec du sucre perlé.</li>
                <li><strong>Gaufre de Bruxelles</strong> : légère et rectangulaire.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какая разница между льежской и брюссельской вафлями?",
                    "text_uk": "У чому різниця між льєжською та брюссельською вафлями?",
                    "text_en": "What is the difference between Liège and Brussels waffles?",
                    "text_fr": "Quelle est la particularité de la gaufre de Liège ?",
                    "choices": [
                        {"text": "Льежская — плотная с карамельным сахаром; Брюссельская — лёгкая прямоугольная", "correct": True},
                        {"text": "Они абсолютно одинаковые", "correct": False},
                        {"text": "Льежская делается только из шоколада", "correct": False}
                    ]
                },
                {
                    "text_ru": "Какой знаменитый бельгийский соус готовят на основе майонеза, томатов и специй?",
                    "text_uk": "Який знаменитий бельгійський соус готують на основі майонезу, томатів та прянощів?",
                    "text_en": "Which famous Belgian sauce is made of mayonnaise, tomatoes, and mild spices?",
                    "text_fr": "Quelle sauce belge typique est à base de mayonnaise, tomates et épices ?",
                    "choices": [
                        {"text": "Sauce Andalouse", "correct": True},
                        {"text": "Ketchup", "correct": False},
                        {"text": "Sauce Soja", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 26,
            "data_lesson_id": "lesson-commune",
            "topic": topic4,
            "title_uk": "🏛️ Комуна, житло та документи в Бельгії",
            "title_ru": "🏛️ Коммуна, жильё и документы в Бельгии",
            "title_en": "🏛️ Commune, Housing & Admin in Belgium",
            "title_fr": "🏛️ La commune, le logement et les démarches",
            "content_html_ru": """
            <h2>Жизнь в Бельгии: Коммуна, Жилье и Здравоохранение</h2>
            <p>В Бельгии вся административная жизнь района сосредоточена в <strong>Коммуне (L'administration communale / La maison communale)</strong>.</p>

            <h3>1. Документы в коммуне:</h3>
            <ul>
                <li><strong>La carte de séjour / Titre de séjour</strong> — Вид на жительство (ID-карта резидента).</li>
                <li><strong>Le Registre National (Numéro National)</strong> — Персональный номер в национальном регистре (формат: ГГ.ММ.ДД-ХХХ.ХХ). Ключ ко всем услугам!</li>
                <li><strong>La composition de ménage</strong> — Справка о составе семьи.</li>
                <li><strong>Prendre rendez-vous</strong> — Записаться на прием в коммуну (онлайн).</li>
            </ul>

            <div class="example-box">
                <p><strong>« Bonjour, j'ai rendez-vous pour mon inscription à la commune. »</strong></p>
                <p>Здравствуйте, у меня запись на регистрацию в коммуне.</p>
            </div>

            <h3>2. Аренда жилья (Le logement):</h3>
            <ul>
                <li><strong>Le bail</strong> [бай] — Договор аренды жилья (обычно <em>bail de 3 ans</em> или <em>9 ans</em>).</li>
                <li><strong>La garantie locative</strong> — Залог за квартиру (обычно на блокированном банковском счете <em>compte bloqué</em>).</li>
                <li><strong>L'état des lieux</strong> — Акт приема-передачи квартиры с описью состояния.</li>
                <li><strong>Les charges</strong> — Коммунальные платежи (отопление, вода, консьерж).</li>
            </ul>

            <h3>3. Медицина и страховка (La Mutuelle):</h3>
            <p>В Бельгии обязательно состоять в страховой кассе <strong>La Mutuelle</strong> (Partenamut, Mutualité Chrétienne, Solidaris и др.):</p>
            <ul>
                <li><strong>Le médecin traitant</strong> — Ваш семейный / участковый врач.</li>
                <li><strong>Le remboursement</strong> — Возмещение стоимости медицинских услуг на банковский счет.</li>
                <li><strong>La vignette jaune</strong> — Наклейка от вашей мутюэль со штрихкодом.</li>
                <li><strong>La pharmacie de garde</strong> — Дежурная ночная аптека.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Життя в Бельгії: Комуна, Оренда та Медицина</h2>
            <p>Уся адміністративна реєстрація в Бельгії проходить через <strong>Комуну (La maison communale)</strong>.</p>

            <h3>1. Документи :</h3>
            <ul>
                <li><strong>Le titre de séjour</strong> — Посвідка на проживання (картка резидента).</li>
                <li><strong>Le Numéro National</strong> — Ідентифікаційний номер національного реєстру.</li>
                <li><strong>La composition de ménage</strong> — Довідка про склад сім'ї.</li>
            </ul>

            <h3>2. Оренда житла (Le logement) :</h3>
            <ul>
                <li><strong>Le bail</strong> — Договір оренди.</li>
                <li><strong>La garantie locative</strong> — Гарантійний заставний депозит.</li>
                <li><strong>L'état des lieux</strong> — Акт перевірки стану житла.</li>
            </ul>

            <h3>3. Медицина (La Mutuelle) :</h3>
            <ul>
                <li><strong>La mutuelle</strong> — Медична страхова організація.</li>
                <li><strong>Le médecin traitant</strong> — Сімейний лікар.</li>
                <li><strong>La pharmacie de garde</strong> — Чергова цілодобова аптека.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Living in Belgium: Administration, Housing & Healthcare</h2>
            <p>Every resident in Belgium interacts regularly with the local <strong>Commune (La maison communale)</strong>.</p>
            <h3>Key Concepts:</h3>
            <ul>
                <li><strong>Le titre de séjour</strong> — Residence permit card.</li>
                <li><strong>Le Numéro National</strong> — National Register ID number.</li>
                <li><strong>Le bail</strong> — Rental lease contract.</li>
                <li><strong>La mutuelle</strong> — Health insurance fund.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les démarches administratives en Belgique</h2>
            <ul>
                <li><strong>La commune</strong> : inscription et carte de séjour.</li>
                <li><strong>Le numéro national</strong> : indispensable pour le travail et la santé.</li>
                <li><strong>Le bail et la garantie locative</strong> pour le logement.</li>
                <li><strong>La mutuelle</strong> pour le remboursement des soins.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Что означает 'La composition de ménage' в бельгийской коммуне?",
                    "text_uk": "Що означає 'La composition de ménage' у бельгійській комуні?",
                    "text_en": "What does 'La composition de ménage' mean in Belgium?",
                    "text_fr": "Que signifie 'La composition de ménage' ?",
                    "choices": [
                        {"text": "Справка о составе семьи / домохозяйства", "correct": True},
                        {"text": "Рецепт приготовления блюда", "correct": False},
                        {"text": "Счет за электроэнергию", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 27,
            "data_lesson_id": "lesson-belgian-expressions",
            "topic": topic4,
            "title_uk": "🗣️ Розмовні бельгійські фрази та сленг",
            "title_ru": "🗣️ Разговорные бельгийские фразы и сленг",
            "title_en": "🗣️ Belgian Expressions & Daily Slang",
            "title_fr": "🗣️ Expressions belges et argot du quotidien",
            "content_html_ru": """
            <h2>Фразы, которые сделают вас своим в Бельгии</h2>
            <p>Если вы хотите звучать естественно в Брюсселе, Льеже, Намюре или Валлонии, запомните эти разговорные формулы:</p>

            <div class="example-box">
                <p><strong>« À tantôt ! »</strong> [а тан-то]</p>
                <p>— До скорой встречи сегодня! (Увидимся позже днем). Самое популярное бельгийское прощание.</p>
            </div>

            <h3>Ключевые выражения :</h3>
            <ul>
                <li><strong>Ça va d'aller !</strong> — Всё будет хорошо! / Прорвёмся! (Любимая бельгийская фраза оптимизма).</li>
                <li><strong>Tu viens ou bien ?</strong> — Добавление «ou bien ?» в конце вопроса: <em>«Ты идешь или как?»</em>.</li>
                <li><strong>Tirer son plan</strong> — Справляться самостоятельно, выпутываться (<em>«Ne t'inquiète pas, je vais tirer mon plan !»</em>).</li>
                <li><strong>Avoir un coup de pompe</strong> — Сильно устать, обессилеть.</li>
                <li><strong>Brosser les cours</strong> — Прогуливать занятия / пары в университете.</li>
                <li><strong>Faire des rawettes</strong> — Дать небольшой довесок / чуть-чуть сверху.</li>
                <li><strong>Être fada / être zinneke</strong> — Быть немного чудаковатым (в Брюсселе: <em>un Zinneke</em> — настоящий житель города разных культур!).</li>
            </ul>

            <div class="example-box warning">
                <strong>Погода в Бельгии:</strong>
                <p>Когда начинается знаменитый затяжной бельгийский ливень, говорят: <strong>« Quelle drache ! Il drache national ! »</strong>.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Фрази, з якими ви будете своїм у Бельгії</h2>
            <div class="example-box">
                <p><strong>« À tantôt ! »</strong> [а тан-то]</p>
                <p>— До зустрічі пізніше сьогодні! (Найпопулярніше бельгійське прощання).</p>
            </div>

            <h3>Популярні вирази :</h3>
            <ul>
                <li><strong>Ça va d'aller !</strong> — Все буде добре! Все вийде!</li>
                <li><strong>Tirer son plan</strong> — Впоратися самостійно.</li>
                <li><strong>Brosser les cours</strong> — Прогулювати уроки.</li>
                <li><strong>Il drache !</strong> — Ллє сильний дощ!</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Belgian Expressions You Must Know</h2>
            <ul>
                <li><strong>À tantôt !</strong> — See you later today!</li>
                <li><strong>Ça va d'aller !</strong> — Everything will be fine!</li>
                <li><strong>Il drache !</strong> — It is pouring rain!</li>
                <li><strong>Tirer son plan</strong> — To manage on one's own.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Expressions belges incontournables</h2>
            <ul>
                <li><strong>À tantôt !</strong> : à plus tard dans la journée.</li>
                <li><strong>Ça va d'aller !</strong> : tout ira bien.</li>
                <li><strong>Il drache !</strong> : il pleut fort.</li>
                <li><strong>Tirer son plan</strong> : se débrouiller seul.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Что означает типичное бельгийское прощание 'À tantôt !'?",
                    "text_uk": "Що означає типове бельгійське прощання 'À tantôt !'?",
                    "text_en": "What does the typical Belgian farewell 'À tantôt !' mean?",
                    "text_fr": "Que signifie l'expression 'À tantôt !' ?",
                    "choices": [
                        {"text": "До встречи позже сегодня (Увидимся днем)", "correct": True},
                        {"text": "Прощай навсегда", "correct": False},
                        {"text": "Приятного аппетита", "correct": False}
                    ]
                }
            ]
        }
    ]

    for l_data in new_belgian_lessons:
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
    enrich_belgian_content()
    print("Belgian content enrichment complete!")
