"""
Script to add 5 essential practical Belgian French lessons with quizzes and 4-language translations.
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

def seed_belgian_mega_pack():
    topic_be = Topic.objects.get(order=5) # 🇧🇪 Жизнь и французский в Бельгии

    lessons_data = [
        {
            "order": 28,
            "data_lesson_id": "lesson-transport-be",
            "topic": topic_be,
            "title_uk": "🚆 Транспорт у Бельгії: STIB, SNCB, MoBIB та квитки",
            "title_ru": "🚆 Транспорт в Бельгии: STIB, SNCB, MoBIB и билеты",
            "title_en": "🚆 Transport in Belgium: STIB, SNCB, MoBIB & Tickets",
            "title_fr": "🚆 Les transports en Belgique : STIB, SNCB et MoBIB",
            "content_html_ru": """
            <h2>Общественный транспорт в Бельгии: полный гид</h2>
            <p>В Бельгии транспортная система очень удобная, но разделена между национальным ж/д оператором и региональными компаниями:</p>

            <h3>1. Транспортные операторы:</h3>
            <ul>
                <li><strong>SNCB / NMBS</strong> — Национальные поезда по всей Бельгии (поезда IC, P, S-train).</li>
                <li><strong>STIB / MIVB</strong> — Метро, трамваи и автобусы в Брюсселе.</li>
                <li><strong>TEC</strong> — Автобусы и трамваи в Валлонии (Шарлеруа, Льеж, Намюр).</li>
                <li><strong>De Lijn</strong> — Автобусы и трамваи во Фландрии (Антверпен, Гент, Брюгге).</li>
            </ul>

            <h3>2. Оплата и карта MoBIB:</h3>
            <div class="example-box">
                <p><strong>La carte MoBIB</strong> — Единая бесконтактная карта для всех видов транспорта в Бельгии (на неё загружаются проездные <em>abonnements</em> или поездки <em>10 voyages</em>).</p>
                <p>В транспорте STIB в Брюсселе также можно просто приложить банковскую карту (<em>paiement sans contact</em>) к серым валидаторам на входе.</p>
            </div>

            <h3>3. Полезные фразы на вокзале и в метро:</h3>
            <div class="conjugation-grid">
                <div><strong>Un aller-retour</strong><br>Билет туда и обратно</div>
                <div><strong>Un aller simple</strong><br>Билет в одну сторону</div>
                <div><strong>La voie / Le quai</strong><br>Железнодорожный путь / Платформа</div>
                <div><strong>La correspondance</strong><br>Пересадка</div>
                <div><strong>Le retard</strong><br>Опоздание (<em>«Le train a 10 min de retard»</em>)</div>
                <div><strong>Weekend Ticket</strong><br>Билет выходного дня SNCB (-50% стоимости!)</div>
            </div>

            <div class="example-box warning">
                <strong>Важные диалоги на вокзале:</strong>
                <p><strong>« Bonjour, un aller-retour pour Liège-Guillemins, s'il vous plaît. »</strong><br>— Здравствуйте, билет туда и обратно до Льежа, пожалуйста.</p>
                <p><strong>« À quelle voie part le train pour Namur ? »</strong><br>— С какого пути отправляется поезд на Намюр?</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Громадський транспорт у Бельгії</h2>
            <p>Транспорт у Бельгії дуже пунктуальний і зручний. Ось головні оператори:</p>

            <h3>Оператори та системи :</h3>
            <ul>
                <li><strong>SNCB / NMBS</strong> — Залізниця по всій Бельгії.</li>
                <li><strong>STIB / MIVB</strong> — Метро, трамваї та автобуси Брюсселя.</li>
                <li><strong>TEC</strong> — Автобуси у Валлонії.</li>
                <li><strong>De Lijn</strong> — Автобуси та трамваї у Фландрії.</li>
                <li><strong>Carte MoBIB</strong> — Універсальна безконтактна картка для проїзду.</li>
            </ul>

            <h3>Корисні фрази :</h3>
            <div class="example-box">
                <p><strong>Un aller-retour</strong> — Квиток в обидва боки.</p>
                <p><strong>La voie / Le quai</strong> — Колія / Платформа.</p>
                <p><strong>« Bonjour, un billet pour Bruxelles-Central, s'il vous plaît. »</strong></p>
            </div>
            """,
            "content_html_en": """
            <h2>Public Transport in Belgium</h2>
            <p>Mastering public transit across Brussels, Wallonia, and Flanders:</p>
            <ul>
                <li><strong>SNCB / NMBS</strong>: Belgian national railways.</li>
                <li><strong>STIB / MIVB</strong>: Brussels metro, tram, and bus network.</li>
                <li><strong>MoBIB card</strong>: Universal contactless smartcard.</li>
                <li><strong>Weekend Ticket</strong>: 50% discount on return train tickets from Friday 19:00 to Sunday.</li>
            </ul>
            <div class="example-box">
                <p><strong>« Un aller-retour pour Bruges, s'il vous plaît. »</strong> — Return ticket to Bruges, please.</p>
            </div>
            """,
            "content_html_fr": """
            <h2>Les transports publics en Belgique</h2>
            <ul>
                <li><strong>SNCB</strong> : trains nationaux.</li>
                <li><strong>STIB</strong> : réseau bruxellois (métro, tram, bus).</li>
                <li><strong>Carte MoBIB</strong> : carte rechargeable pour tous les transports.</li>
                <li><strong>Weekend ticket</strong> : réduction de 50% le week-end.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какая скидка действует на билеты туда-обратно на поездах SNCB по выходным (Weekend Ticket)?",
                    "text_uk": "Яка знижка діє на квитки туди-назад на поїзди SNCB у вихідні (Weekend Ticket)?",
                    "text_en": "What discount does the SNCB Weekend Ticket offer on return trips?",
                    "text_fr": "Quelle est la réduction du Weekend Ticket de la SNCB ?",
                    "choices": [
                        {"text": "-50% стоимости билета туда-обратно", "correct": True},
                        {"text": "-10% только для студентов", "correct": False},
                        {"text": "Билет бесплатный", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 29,
            "data_lesson_id": "lesson-supermarket-be",
            "topic": topic_be,
            "title_uk": "🛒 У бельгійському супермаркеті та Bancontact",
            "title_ru": "🛒 В бельгийском супермаркете и Bancontact",
            "title_en": "🛒 Belgian Supermarkets & Bancontact",
            "title_fr": "🛒 Au supermarché en Belgique et Bancontact",
            "content_html_ru": """
            <h2>Покупки в супермаркетах Бельгии (Colruyt, Delhaize, Carrefour, Aldi, Lidl)</h2>
            <p>Походы за продуктами в Бельгии имеют свой колорит и особенности этикета:</p>

            <h3>1. Оплата: Система Bancontact</h3>
            <p><strong>Bancontact</strong> [банконтакт] — бельгийский национальный стандарт дебетовых карт. Он работает везде (в терминалах, через приложение Payconiq или бесконтактно <em>sans contact</em>).</p>

            <h3>2. На кассе супермаркета:</h3>
            <div class="example-box">
                <p><strong>Кассир:</strong> « Bonjour ! Vous avez la carte du magasin ? » <em>(У вас есть карта магазина?)</em></p>
                <p><strong>Вы:</strong> « Oui, la voici ! » / « Non, je n'en ai pas. »</p>
                <p><strong>Кассир:</strong> « Ça vous fera 42 euros et nonante centimes, s'il vous plaît. »</p>
                <p><strong>Вы:</strong> « Par carte / Sans contact, s'il vous plaît. »</p>
                <p><strong>Кассир:</strong> « Voulez-vous le ticket de caisse ? » <em>(Вам нужен чек?)</em></p>
                <p><strong>Вы:</strong> « Oui, merci ! Bonne journée ! »</p>
            </div>

            <h3>3. Бельгийские продукты и словарь:</h3>
            <ul>
                <li><strong>Le caddie / Le chariot</strong> — Тележка для покупок (нужна монетка 50 центов, 1€ или 2€).</li>
                <li><strong>Le sachet / Le sac réutilisable</strong> — Пакет для покупок.</li>
                <li><strong>Les chicons</strong> — Эндивий / цикорий (традиционный бельгийский овощ).</li>
                <li><strong>Le spéculoos</strong> — Знаменитое пряное хрустящее бельгийское печенье (Lotus).</li>
                <li><strong>Américain préparé</strong> — Популярный бельгийский мясной тартар со специями для сэндвичей (<em>baguette / pistolet</em>).</li>
                <li><strong>La vidange</strong> — Залоговая стоимость стеклянных бутылок и ящиков (возвращается через автомат в магазине).</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Покупки в супермаркетах Бельгії</h2>
            <p>Особливості покупок у Delhaize, Colruyt, Carrefour, Lidl:</p>

            <h3>На касі :</h3>
            <div class="example-box">
                <p><strong>« Par carte / Sans contact, s'il vous plaît. »</strong> — Оплата карткою / безконтактно.</p>
                <p><strong>« Voulez-vous le ticket de caisse ? »</strong> — Чи потрібен вам чек?</p>
                <p><strong>Bancontact</strong> — Національна платіжна система Бельгії.</p>
            </div>

            <h3>Бельгійські продукти :</h3>
            <ul>
                <li><strong>Les chicons</strong> — Цикорій (ендівій).</li>
                <li><strong>Le spéculoos</strong> — Традиційне пряне печиво.</li>
                <li><strong>La vidange</strong> — Повернення тари (застава за скляні пляшки).</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Shopping in Belgian Supermarkets</h2>
            <ul>
                <li><strong>Bancontact</strong>: The primary payment method in Belgium.</li>
                <li><strong>La vidange</strong>: Bottle deposit return system.</li>
                <li><strong>Le caddie</strong>: Shopping cart (requires a 1€ coin or token).</li>
                <li><strong>Chicons, Spéculoos, Pistolets</strong>: Iconic Belgian staples.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Faire ses courses en Belgique</h2>
            <div class="example-box">
                <p><strong>« Paiement par Bancontact / sans contact. »</strong></p>
                <p><strong>La vidange</strong> : consigne pour les bouteilles en verre.</p>
            </div>
            """,
            "questions": [
                {
                    "text_ru": "Что означает термин 'La vidange' в бельгийском супермаркете?",
                    "text_uk": "Що означає термін 'La vidange' у бельгійському супермаркеті?",
                    "text_en": "What does 'La vidange' mean in a Belgian supermarket?",
                    "text_fr": "Que signifie 'La vidange' au supermarché ?",
                    "choices": [
                        {"text": "Возврат залога за сданные стеклянные бутылки / тару", "correct": True},
                        {"text": "Скидочный купон на свежую выпечку", "correct": False},
                        {"text": "Платный пластиковый пакет", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 30,
            "data_lesson_id": "lesson-doctor-be",
            "topic": topic_be,
            "title_uk": "🏥 Візит до лікаря, аптека та Mutuelle",
            "title_ru": "🏥 Визит к врачу, аптека и Mutuelle в Бельгии",
            "title_en": "🏥 Doctor Visit, Pharmacy & Mutuelle in Belgium",
            "title_fr": "🏥 Chez le médecin, à la pharmacie et la Mutuelle",
            "content_html_ru": """
            <h2>Здравоохранение и визит к врачу в Бельгии</h2>
            <p>Медицинская система Бельгии — одна из лучших в Европе. Вот как устроена запись и визит:</p>

            <h3>1. Запись к врачу (Prendre rendez-vous):</h3>
            <p>В Бельгии врачи общей практики называются <strong>Médecin généraliste (médecin traitant)</strong>. Записаться онлайн можно через платформы <strong>Rosa.be</strong> или <strong>Doctena.be</strong>.</p>

            <h3>2. Диалог у врача (Chez le médecin):</h3>
            <div class="example-box">
                <p><strong>Врач:</strong> « Bonjour, qu'est-ce qui vous amène ? / Où avez-vous mal ? » <em>(Что вас беспокоит? Где болит?)</em></p>
                <p><strong>Вы:</strong> « J'ai de la fièvre et très mal à la gorge depuis deux jours. » <em>(У меня температура и сильно болит горло уже 2 дня.)</em></p>
                <p><strong>Вы:</strong> « J'ai mal au ventre / à la tête / au dos. » <em>(Болит живот / голова / спина.)</em></p>
                <p><strong>Врач:</strong> « Je vais vous ausculter. Voici une ordonnance pour la pharmacie. » <em>(Я вас послушаю. Вот рецепт в аптеку.)</em></p>
            </div>

            <h3>3. Возмещение от Mutuelle (Le remboursement):</h3>
            <ul>
                <li>После приема врач выдает электронную квитанцию <strong>e-Attestation</strong> или бумажный листок <em>attestation de soins</em>.</li>
                <li>Ваша <strong>Mutuelle</strong> автоматически возмещает большую часть стоимости консультации прямо на ваш бельгийский банковский счет (IBAN).</li>
                <li>Пациент оплачивает только небольшую личную долю — <strong>Le ticket modérateur</strong> (обычно 4–6 € за прием).</li>
            </ul>

            <h3>4. В аптеке (À la pharmacie):</h3>
            <div class="example-box">
                <p><strong>« Bonjour, j'ai une ordonnance du médecin. »</strong> <em>(Здравствуйте, у меня рецепт от врача.)</em></p>
                <p><strong>« Avez-vous quelque chose contre le rhume / la toux ? »</strong> <em>(Есть что-то от простуды / кашля?)</em></p>
                <p><strong>La pharmacie de garde</strong> — Дежурная аптека, работающая ночью и в воскресенье (поиск на <em>pharmacie.be</em>).</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Медицина та візит до лікаря в Бельгії</h2>
            <h3>Діалог у лікаря (Médecin généraliste) :</h3>
            <div class="example-box">
                <p><strong>« J'ai de la fièvre et mal à la gorge. »</strong> — У мене температура і болить горло.</p>
                <p><strong>« Une ordonnance »</strong> — Рецепт на ліки.</p>
                <p><strong>La Mutuelle</strong> — Страхова каса, яка автоматично повертає кошти за візит.</p>
            </div>

            <h3>В аптеці :</h3>
            <p><strong>La pharmacie de garde</strong> — Чергова аптека у вихідні та вночі.</p>
            """,
            "content_html_en": """
            <h2>Healthcare & Visiting the Doctor in Belgium</h2>
            <ul>
                <li><strong>Médecin généraliste</strong>: General practitioner (book online via Rosa.be / Doctena.be).</li>
                <li><strong>Une ordonnance</strong>: Medical prescription.</li>
                <li><strong>La Mutuelle</strong>: Reimburses the majority of consultation costs.</li>
                <li><strong>Le ticket modérateur</strong>: The small co-pay remaining for the patient.</li>
                <li><strong>Pharmacie de garde</strong>: On-duty emergency pharmacy.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Chez le médecin et à la pharmacie en Belgique</h2>
            <div class="example-box">
                <p><strong>« J'ai mal à la gorge et de la fièvre. »</strong></p>
                <p><strong>L'ordonnance</strong> et le remboursement par la <strong>Mutuelle</strong>.</p>
            </div>
            """,
            "questions": [
                {
                    "text_ru": "Как по-французски сказать врачу 'У меня болит горло и температура'?",
                    "text_uk": "Як французькою сказати лікарю 'У мене болить горло і температура'?",
                    "text_en": "How do you say 'I have a sore throat and a fever' in French?",
                    "text_fr": "Comment dire 'J'ai mal à la gorge et de la fièvre' ?",
                    "choices": [
                        {"text": "J'ai de la fièvre et mal à la gorge", "correct": True},
                        {"text": "J'ai faim et soif", "correct": False},
                        {"text": "Je voudrais un café", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 31,
            "data_lesson_id": "lesson-work-be",
            "topic": topic_be,
            "title_uk": "💼 Робота в Бельгії: Actiris, Forem, контракти та пільги",
            "title_ru": "💼 Работа в Бельгии: Actiris, Forem, контракты и льготы",
            "title_en": "💼 Working in Belgium: Contracts, Benefits & Job Search",
            "title_fr": "💼 Travailler en Belgique : Actiris, Forem et contrats",
            "content_html_ru": """
            <h2>Трудоустройство и работа в Бельгии</h2>
            <p>Бельгийский рынок труда имеет сильную систему социальной защиты и особые бонусы:</p>

            <h3>1. Службы занятости по регионам:</h3>
            <ul>
                <li><strong>Actiris</strong> — Брюссельская служба занятости (помощь в поиске работы, курсы языков <em>Chèques-Langues</em>).</li>
                <li><strong>Le Forem</strong> — Государственная служба занятости Валлонии.</li>
                <li><strong>VDAB</strong> — Служба занятости Фландрии.</li>
            </ul>

            <h3>2. Типы контрактов:</h3>
            <div class="conjugation-grid">
                <div><strong>CDI</strong><br>Бессрочный постоянный трудовой договор (<em>Contrat à Durée Indéterminée</em>) — золотой стандарт.</div>
                <div><strong>CDD</strong><br>Срочный договор на фиксированный период (<em>Contrat à Durée Déterminée</em>).</div>
                <div><strong>Contrat Intérim</strong><br>Временная работа через агентство занятости (Adecco, Randstad, Manpower).</div>
            </div>

            <h3>3. Знаменитые бельгийские бонусы и термины:</h3>
            <ul>
                <li><strong>Les chèques-repas / Titres-repas</strong> — Талоны на питание (электронные карты Edenred, Sodexo/Pluxee, Monizze — около 8 € за рабочий день без налога!).</li>
                <li><strong>Les éco-chèques</strong> — Эко-чеки на покупку экологичных товаров, электросамокатов, велосипедов, органической еды.</li>
                <li><strong>Le salaire brut vs net</strong> — Зарплата до вычета налогов (брутто) и на руки (нетто).</li>
                <li><strong>Le treizième mois (13e mois)</strong> — Тринадцатая зарплата / годовая премия в конце года.</li>
                <li><strong>La fiche de paie</strong> — Ежемесячный расчетный листок по заработной плате.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Працевлаштування та робота в Бельгії</h2>
            <h3>Служби зайнятості :</h3>
            <ul>
                <li><strong>Actiris</strong> — Брюссель.</li>
                <li><strong>Le Forem</strong> — Валлонія.</li>
            </ul>

            <h3>Бонуси в Бельгії :</h3>
            <ul>
                <li><strong>CDI</strong> — Постійний безстроковий контракт.</li>
                <li><strong>Chèques-repas</strong> — Чеки на харчування (електронна картка).</li>
                <li><strong>Éco-chèques</strong> — Еко-чеки на екологічні товари.</li>
                <li><strong>Fiche de paie</strong> — Розрахунковий листок зарплати.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Working in Belgium: Contracts & Benefits</h2>
            <ul>
                <li><strong>Actiris & Forem</strong>: Regional employment agencies.</li>
                <li><strong>CDI</strong>: Permanent open-ended work contract.</li>
                <li><strong>Chèques-repas (Meal vouchers)</strong>: Daily non-taxable meal allowance card (approx. 8€/day).</li>
                <li><strong>Éco-chèques</strong>: Vouchers for eco-friendly goods and transit.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le monde du travail en Belgique</h2>
            <ul>
                <li><strong>Actiris et Forem</strong> pour l'emploi.</li>
                <li><strong>CDI et CDD</strong> : types de contrats.</li>
                <li><strong>Chèques-repas et éco-chèques</strong> : avantages extra-légaux.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Что такое 'CDI' в бельгийском трудовом праве?",
                    "text_uk": "Що таке 'CDI' у бельгійському трудовому праві?",
                    "text_en": "What is a 'CDI' contract in Belgium?",
                    "text_fr": "Que signifie un contrat 'CDI' ?",
                    "choices": [
                        {"text": "Постоянный бессрочный трудовой контракт (Contrat à Durée Indéterminée)", "correct": True},
                        {"text": "Временная однодневная стажировка", "correct": False},
                        {"text": "Волонтерский неоплачиваемый договор", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 32,
            "data_lesson_id": "lesson-recycling-be",
            "topic": topic_be,
            "title_uk": "🏠 Сортування сміття та комунальні правила в Бельгії",
            "title_ru": "🏠 Сортировка мусора и коммунальные правила в Бельгии",
            "title_en": "🏠 Waste Sorting & Municipal Rules in Belgium",
            "title_fr": "🏠 Le tri des déchets et les règles communales en Belgique",
            "content_html_ru": """
            <h2>Сортировка мусора и пакеты в Бельгии</h2>
            <p>В Бельгии сортировка отходов — строгая обязанность каждого жителя. Неправильный пакет или выброс не в тот день может повлечь штраф от коммуны (<em>amende administrative</em>)!</p>

            <h3>1. Цвета официальных пакетов (Bruxelles-Propreté / Wallonie):</h3>
            <div class="conjugation-grid">
                <div><strong>⚪ Sac blanc</strong><br>Остаточный бытовой несортируемый мусор (<em>déchets résiduels</em>).</div>
                <div><strong>🔵 Sac bleu (PMC)</strong><br>Пластиковые бутылки, упаковка, металлические банки, тетрапаки.</div>
                <div><strong>🟠 Sac orange / vert</strong><br>Пищевые и органические отходы (<em>déchets alimentaires / compost</em>).</div>
                <div><strong>🟡 Sac jaune</strong><br>Бумага, газеты, картонные коробки (чистые).</div>
            </div>

            <h3>2. Стекло (Les bulles à verre):</h3>
            <p>Стеклянные бутылки и банки выбрасывают в уличные контейнеры-колокола (<strong>bulles à verre</strong>), разделяя на белое прозрачное стекло (<em>verre blanc</em>) и цветное (<em>verre coloré</em>). Запрещено выбрасывать с 22:00 до 07:00 утра из-за шума!</p>

            <h3>3. Правила и лексика:</h3>
            <ul>
                <li><strong>Le calendrier des collectes</strong> — Календарь вывоза мусора (в каждом районе свой день недели!).</li>
                <li><strong>Sortir les poubelles</strong> — Выставить пакеты на улицу (обычно накануне вечером после 18:00).</li>
                <li><strong>Le parc à conteneurs / Recypark / Déchetterie</strong> — Пункт приема крупногабаритного мусора, мебели, электроники и стройматериалов.</li>
                <li><strong>Les encombrants</strong> — Крупногабаритный мусор.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Сортування сміття в Бельгії</h2>
            <h3>Кольори пакетів :</h3>
            <ul>
                <li><strong>⚪ Sac blanc</strong> — Звичайне побутове несортоване сміття.</li>
                <li><strong>🔵 Sac bleu (PMC)</strong> — Пластик, бляшанки, тетрапак.</li>
                <li><strong>🟠 Sac orange</strong> — Органічні та харчові відходи.</li>
                <li><strong>🟡 Sac jaune</strong> — Папір та картон.</li>
                <li><strong>Bulles à verre</strong> — Контейнери для скла (біле та кольорове).</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Waste Sorting in Belgium</h2>
            <ul>
                <li><strong>⚪ White bag</strong>: Non-recyclable household waste.</li>
                <li><strong>🔵 Blue bag (PMC)</strong>: Plastic bottles, metal cans, drink cartons.</li>
                <li><strong>🟠 Orange bag</strong>: Food and organic waste.</li>
                <li><strong>🟡 Yellow bag</strong>: Paper and clean cardboard.</li>
                <li><strong>Bulles à verre</strong>: Public street containers for glass.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le tri des déchets en Belgique</h2>
            <ul>
                <li><strong>Sac blanc</strong> : déchets résiduels.</li>
                <li><strong>Sac bleu (PMC)</strong> : emballages plastiques et métalliques.</li>
                <li><strong>Sac orange</strong> : déchets organiques.</li>
                <li><strong>Sac jaune</strong> : papiers et cartons.</li>
                <li><strong>Bulles à verre</strong> pour le verre transparent et coloré.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "В какой пакет в Бельгии выбрасывают пластиковые бутылки, металлические банки и упаковку (PMC)?",
                    "text_uk": "У який пакет у Бельгії викидають пластикові пляшки, бляшанки та пакування (PMC)?",
                    "text_en": "Which bag is used in Belgium for plastic bottles, cans, and drink cartons (PMC)?",
                    "text_fr": "Dans quel sac jette-t-on les emballages PMC en Belgique ?",
                    "choices": [
                        {"text": "В синий пакет (Sac bleu)", "correct": True},
                        {"text": "В белый пакет (Sac blanc)", "correct": False},
                        {"text": "В желтый пакет (Sac jaune)", "correct": False}
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
    seed_belgian_mega_pack()
    print("Belgian mega pack successfully added!")
