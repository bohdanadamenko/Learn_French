"""
Script to expand the core French curriculum with 10 foundational grammar, verb, and vocabulary lessons.
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

def seed_curriculum_expansion():
    topic2 = Topic.objects.get(order=2) # 🧱 Базовая грамматика
    topic3 = Topic.objects.get(order=3) # ⚡ Глаголы, времена и вопросы
    topic4 = Topic.objects.get(order=4) # 🌍 Лексика и темы

    lessons_data = [
        # --- Topic 2: Grammar additions ---
        {
            "order": 41,
            "data_lesson_id": "lesson-possessives",
            "topic": topic2,
            "title_uk": "🔤 Присвійні прикметники (Мій, твій, його)",
            "title_ru": "🔤 Притяжательные местоимения (Мой, твой, его/её)",
            "title_en": "🔤 Possessive Adjectives (My, your, his/her...)",
            "title_fr": "🔤 Les adjectifs possessifs",
            "content_html_ru": """
            <h2>Притяжательные местоимения: чей предмет?</h2>
            <p>Во французском языке форма притяжательного местоимения зависит от <strong>рода и числа предмета</strong>, а не владельца:</p>

            <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
                <div><strong>Я (Мой):</strong><br><strong>Mon</strong> (м.р.) — <em>mon livre</em><br><strong>Ma</strong> (ж.р.) — <em>ma maison</em><br><strong>Mes</strong> (мн.ч.) — <em>mes amis</em></div>
                <div><strong>Ты (Твой):</strong><br><strong>Ton</strong> (м.р.) — <em>ton passeport</em><br><strong>Ta</strong> (ж.р.) — <em>ta voiture</em><br><strong>Tes</strong> (мн.ч.) — <em>tes clés</em></div>
                <div><strong>Он / Она (Его/Её):</strong><br><strong>Son</strong> (м.р.) — <em>son GSM</em><br><strong>Sa</strong> (ж.р.) — <em>sa famille</em><br><strong>Ses</strong> (мн.ч.) — <em>ses enfants</em></div>
            </div>

            <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
                <div><strong>Мы (Наш):</strong><br><strong>Notre</strong> (ед.ч.) — <em>notre ville</em><br><strong>Nos</strong> (мн.ч.) — <em>nos amis</em></div>
                <div><strong>Вы (Ваш):</strong><br><strong>Votre</strong> (ед.ч.) — <em>votre adresse</em><br><strong>Vos</strong> (мн.ч.) — <em>vos bagages</em></div>
                <div><strong>Они (Их):</strong><br><strong>Leur</strong> (ед.ч.) — <em>leur appartement</em><br><strong>Leurs</strong> (мн.ч.) — <em>leurs enfants</em></div>
            </div>

            <div class="example-box warning">
                <strong>Важное исключение:</strong>
                <p>Перед существительными женского рода, начинающимися на гласную или немую <em>h</em>, вместо <em>ma, ta, sa</em> используется <strong>mon, ton, son</strong> (для благозвучия):</p>
                <p><em>Mon amie</em> (моя подруга, а не ma amie!), <em>Son histoire</em> (его/её история).</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Присвійні прикметники у французькій мові</h2>
            <p>Форма залежить від роду та числа предмета :</p>
            <div class="conjugation-grid">
                <div><strong>Мій:</strong> Mon (ч.р.), Ma (ж.р.), Mes (мн.)</div>
                <div><strong>Твій:</strong> Ton (ч.р.), Ta (ж.р.), Tes (мн.)</div>
                <div><strong>Його/Її:</strong> Son (ч.р.), Sa (ж.р.), Ses (мн.)</div>
                <div><strong>Наш:</strong> Notre (одн.), Nos (мн.)</div>
                <div><strong>Ваш:</strong> Votre (одн.), Vos (мн.)</div>
                <div><strong>Їхній:</strong> Leur (одн.), Leurs (мн.)</div>
            </div>
            <div class="example-box warning">
                <strong>Виняток:</strong> <em>Mon amie</em> (моя подруга — перед голосною замість ma).
            </div>
            """,
            "content_html_en": """
            <h2>Possessive Adjectives in French</h2>
            <ul>
                <li><strong>My:</strong> Mon (masc.), Ma (fem.), Mes (plural).</li>
                <li><strong>Your:</strong> Ton, Ta, Tes / Votre, Vos.</li>
                <li><strong>His/Her:</strong> Son, Sa, Ses.</li>
                <li><strong>Exception:</strong> Use <em>mon, ton, son</em> before feminine words starting with a vowel (e.g. <em>mon amie</em>).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les adjectifs possessifs</h2>
            <ul>
                <li><strong>Mon / Ma / Mes</strong></li>
                <li><strong>Ton / Ta / Tes</strong></li>
                <li><strong>Son / Sa / Ses</strong></li>
                <li><strong>Notre / Nos, Votre / Vos, Leur / Leurs</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какое притяжательное местоимение нужно поставить перед словом 'amie' (подруга, женский род)?",
                    "text_uk": "Який присвійний займенник ставимо перед 'amie' (подруга, жін. рід)?",
                    "text_en": "Which possessive is used before 'amie' (feminine starting with vowel)?",
                    "text_fr": "Quel possessif utilise-t-on devant 'amie' ?",
                    "choices": [
                        {"text": "Mon amie (перед гласной ma меняется на mon)", "correct": True},
                        {"text": "Ma amie", "correct": False},
                        {"text": "Mes amie", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 42,
            "data_lesson_id": "lesson-demonstratives",
            "topic": topic2,
            "title_uk": "👉 Вказівні прикметники (Цей, ця, ці)",
            "title_ru": "👉 Указательные местоимения (Этот, эта, эти)",
            "title_en": "👉 Demonstrative Adjectives (This, that, these)",
            "title_fr": "👉 Les adjectifs démonstratifs",
            "content_html_ru": """
            <h2>Указательные формы: Ce, Cet, Cette, Ces</h2>
            <p>Когда вы указываете на конкретный предмет или человека (*«этот билет, эта улица, эти люди»*):</p>

            <div class="conjugation-grid">
                <div><strong>CE</strong> [сё]<br>Мужской род (перед согласной)<br><em>Ce train, ce croissant</em></div>
                <div><strong>CET</strong> [сэт]<br>Мужской род (перед гласной или немой h)<br><em>Cet appartement, cet homme</em></div>
                <div><strong>CETTE</strong> [сэт]<br>Женский род (перед любыми буквами)<br><em>Cette gare, cette gaufre</em></div>
                <div><strong>CES</strong> [се]<br>Множественное число (все роды)<br><em>Ces frites, ces enfants</em></div>
            </div>

            <div class="example-box">
                <p><strong>« Ce pistolet est délicieux ! »</strong> — Эта булочка очень вкусная!</p>
                <p><strong>« Cet hôtel est près de la Grand-Place. »</strong> — Этот отель рядом с Гран-Плас.</p>
                <p><strong>« Cette commune est très calme. »</strong> — Эта коммуна очень спокойная.</p>
                <p><strong>« Ces bières trappistes sont réputées. »</strong> — Эти траппистские сорта пива знамениты.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Вказівні прикметники : Ce, Cet, Cette, Ces</h2>
            <div class="conjugation-grid">
                <div><strong>CE:</strong> Чол. рід (<em>ce tram</em>)</div>
                <div><strong>CET:</strong> Чол. рід перед голосною (<em>cet ami</em>)</div>
                <div><strong>CETTE:</strong> Жін. рід (<em>cette ville</em>)</div>
                <div><strong>CES:</strong> Множина (<em>ces billets</em>)</div>
            </div>
            """,
            "content_html_en": """
            <h2>Demonstratives: Ce, Cet, Cette, Ces</h2>
            <ul>
                <li><strong>Ce:</strong> masculine consonant (<em>ce café</em>).</li>
                <li><strong>Cet:</strong> masculine vowel/mute h (<em>cet hôtel</em>).</li>
                <li><strong>Cette:</strong> feminine (<em>cette rue</em>).</li>
                <li><strong>Ces:</strong> plural (<em>ces amis</em>).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les démonstratifs</h2>
            <ul>
                <li><strong>Ce / Cet</strong> (masculin)</li>
                <li><strong>Cette</strong> (féminin)</li>
                <li><strong>Ces</strong> (pluriel)</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какую форму указательного местоимения выбрать перед 'homme' (мужчина, м.р. с немой h)?",
                    "text_uk": "Яку форму вказівного займенника обрати перед 'homme' (чоловік)?",
                    "text_en": "Which demonstrative is used before 'homme'?",
                    "text_fr": "Quel démonstratif devant 'homme' ?",
                    "choices": [
                        {"text": "Cet homme", "correct": True},
                        {"text": "Ce homme", "correct": False},
                        {"text": "Cette homme", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 43,
            "data_lesson_id": "lesson-pronouns-cod-coi",
            "topic": topic2,
            "title_uk": "👥 Займенники прямого та непрямого додатку (COD / COI)",
            "title_ru": "👥 Местоимения прямого и косвенного дополнения (COD / COI)",
            "title_en": "👥 Direct & Indirect Object Pronouns (COD / COI)",
            "title_fr": "👥 Les pronoms compléments COD et COI",
            "content_html_ru": """
            <h2>Местоимения COD и COI: как не повторять слова</h2>
            <p>Чтобы не повторять одно и то же существительное (*«Я вижу Максима → Я его вижу»*), французы ставят местоимения <strong>перед глаголом</strong>:</p>

            <h3>1. Прямое дополнение (COD: кого? что?):</h3>
            <div class="conjugation-grid">
                <div><strong>Le (l')</strong><br>Его / это (м.р.)<br><em>Je <strong>le</strong> vois</em></div>
                <div><strong>La (l')</strong><br>Её (ж.р.)<br><em>Je <strong>la</strong> connais</em></div>
                <div><strong>Les</strong><br>Их (мн.ч.)<br><em>Je <strong>les</strong> achète</em></div>
            </div>

            <h3>2. Косвенное дополнение (COI: кому? с предлогом à):</h3>
            <div class="conjugation-grid">
                <div><strong>Lui</strong><br>Ему / Ей<br><em>Je <strong>lui</strong> téléphone</em></div>
                <div><strong>Leur</strong><br>Им<br><em>Je <strong>leur</strong> écris</em></div>
            </div>

            <div class="example-box">
                <p><strong>« Tu connais Bruxelles ? — Oui, je la connais très bien ! »</strong></p>
                <p><strong>« Tu as appelé le médecin ? — Oui, je lui ai téléphoné ce matin. »</strong></p>
            </div>
            """,
            "content_html_uk": """
            <h2>Займенники COD (його/її) та COI (йому/їй)</h2>
            <p>Займенники ставляться <strong>перед дієсловом</strong> :</p>
            <ul>
                <li><strong>Le / La / Les</strong> (кого? що?): <em>Je le prends</em> (Я це беру).</li>
                <li><strong>Lui / Leur</strong> (кому?): <em>Je lui parle</em> (Я говорю з ним/нею).</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Object Pronouns (COD & COI)</h2>
            <p>Pronouns are placed <strong>before the verb</strong>:</p>
            <ul>
                <li><strong>COD:</strong> Le (him/it), La (her/it), Les (them). E.g. <em>Je la vois</em> (I see her).</li>
                <li><strong>COI:</strong> Lui (to him/her), Leur (to them). E.g. <em>Je lui parle</em> (I speak to him/her).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les pronoms COD et COI</h2>
            <ul>
                <li><strong>COD</strong> : le, la, les (<em>Je le regarde</em>)</li>
                <li><strong>COI</strong> : lui, leur (<em>Je lui réponds</em>)</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Куда во французском предложении ставится местоимение-дополнение (например 'le')?",
                    "text_uk": "Куди у французькому реченні ставиться займенник-додаток?",
                    "text_en": "Where is the object pronoun placed in a standard French sentence?",
                    "text_fr": "Où place-t-on le pronom complément ?",
                    "choices": [
                        {"text": "Перед спрягаемым глаголом (Je le vois)", "correct": True},
                        {"text": "В самом конце предложения", "correct": False},
                        {"text": "После существительного", "correct": False}
                    ]
                }
            ]
        },

        # --- Topic 3: Verbs additions ---
        {
            "order": 44,
            "data_lesson_id": "lesson-ir-verbs",
            "topic": topic3,
            "title_uk": "🏃 Дієслова 2-ї групи на -IR (Finir, Choisir)",
            "title_ru": "🏃 Глаголы 2-й группы на -IR (Finir, Choisir)",
            "title_en": "🏃 2nd Group Verbs ending in -IR (Finir, Choisir)",
            "title_fr": "🏃 Les verbes du 2e groupe (-IR)",
            "content_html_ru": """
            <h2>Глаголы 2-й группы: суффикс -ISS-</h2>
            <p>Глаголы 2-й группы оканчиваются на <strong>-IR</strong> и во множественном числе получают узнаваемый суффикс <strong>-iss-</strong>:</p>

            <h3>Спряжение глагола FINIR (заканчивать):</h3>
            <div class="conjugation-grid">
                <div><strong>Je finis</strong> [же фини]<br>Я заканчиваю</div>
                <div><strong>Tu finis</strong> [тю фини]<br>Ты заканчиваешь</div>
                <div><strong>Il / Elle finit</strong> [іль фини]<br>Он / Она заканчивает</div>
                <div><strong>Nous finissons</strong> [ну финисон]<br>Мы заканчиваем</div>
                <div><strong>Vous finissez</strong> [ву финисе]<br>Вы заканчиваете</div>
                <div><strong>Ils finissent</strong> [іль финис]<br>Они заканчивают</div>
            </div>

            <h3>Популярные глаголы 2-й группы:</h3>
            <ul>
                <li><strong>Choisir</strong> — Выбирать (<em>«Je choisis la gaufre de Liège»</em>).</li>
                <li><strong>Réussir</strong> — Добиваться успеха, сдать экзамен (<em>«Il réussit son test»</em>).</li>
                <li><strong>Réfléchir</strong> — Думать, размышлять (<em>«Nous réfléchissons»</em>).</li>
                <li><strong>Remplir</strong> — Заполнять документ/формуляр (<em>«Remplir un formulaire à la commune»</em>).</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Дієслова 2-ї групи на -IR (Finir, Choisir)</h2>
            <p>Особливість — суфікс <strong>-iss-</strong> у множині :</p>
            <div class="conjugation-grid">
                <div>Je finis</div>
                <div>Tu finis</div>
                <div>Il finit</div>
                <div>Nous finissons</div>
                <div>Vous finissez</div>
                <div>Ils finissent</div>
            </div>
            """,
            "content_html_en": """
            <h2>2nd Group Verbs ending in -IR</h2>
            <p>Key pattern with <strong>-iss-</strong> suffix in plural forms:</p>
            <ul>
                <li><strong>Finir</strong> (to finish), <strong>Choisir</strong> (to choose), <strong>Réussir</strong> (to succeed).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les verbes du 2e groupe en -IR</h2>
            <div class="conjugation-grid">
                <div>Je finis</div>
                <div>Tu finis</div>
                <div>Il finit</div>
                <div>Nous finissons</div>
                <div>Vous finissez</div>
                <div>Ils finissent</div>
            </div>
            """,
            "questions": [
                {
                    "text_ru": "Какая правильная форма: 'Nous ___ (choisir) ce restaurant'?",
                    "text_uk": "Яка правильна форма: 'Nous ___ (choisir) ce restaurant'?",
                    "text_en": "What is the correct form: 'Nous ___ (choisir)'?",
                    "text_fr": "Quelle est la forme correcte : 'Nous ___ (choisir)' ?",
                    "choices": [
                        {"text": "choisissons", "correct": True},
                        {"text": "choisons", "correct": False},
                        {"text": "choisissez", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 45,
            "data_lesson_id": "lesson-key-irregular-verbs",
            "topic": topic3,
            "title_uk": "⚡ Головні неправильні дієслова: Faire, Prendre, Venir, Pouvoir",
            "title_ru": "⚡ Главные неправильные глаголы: Faire, Prendre, Venir, Pouvoir",
            "title_en": "⚡ Key Irregular Verbs: Faire, Prendre, Venir, Pouvoir, Vouloir",
            "title_fr": "⚡ Les verbes irréguliers indispensables",
            "content_html_ru": """
            <h2>Топ-5 самых важных неправильных глаголов</h2>

            <h3>1. FAIRE (делать / заниматься):</h3>
            <div class="conjugation-grid">
                <div><strong>Je fais</strong> [же фэ]</div>
                <div><strong>Tu fais</strong> [тю фэ]</div>
                <div><strong>Il fait</strong> [іль фэ]</div>
                <div><strong>Nous faisons</strong> [ну фёзон]</div>
                <div><strong>Vous faites</strong> [ву фэт]</div>
                <div><strong>Ils font</strong> [іль фон]</div>
            </div>

            <h3>2. PRENDRE (брать / принимать / садиться на транспорт):</h3>
            <div class="conjugation-grid">
                <div><strong>Je prends</strong></div>
                <div><strong>Tu prends</strong></div>
                <div><strong>Il prend</strong></div>
                <div><strong>Nous prenons</strong></div>
                <div><strong>Vous prenez</strong></div>
                <div><strong>Ils prennent</strong></div>
            </div>

            <h3>3. VENIR (приходить / приезжать):</h3>
            <div class="conjugation-grid">
                <div><strong>Je viens</strong></div>
                <div><strong>Tu viens</strong></div>
                <div><strong>Il vient</strong></div>
                <div><strong>Nous venons</strong></div>
                <div><strong>Vous venez</strong></div>
                <div><strong>Ils viennent</strong></div>
            </div>

            <h3>4. POUVOIR (мочь) & VOULOIR (хотеть):</h3>
            <div class="example-box">
                <p><strong>Pouvoir:</strong> <em>Je peux, tu peux, il peut, nous pouvons, vous pouvez, ils peuvent.</em></p>
                <p><strong>Vouloir:</strong> <em>Je veux, tu veux, il veut, nous voulons, vous voulez, ils veulent.</em></p>
            </div>
            """,
            "content_html_uk": """
            <h2>Головні неправильні дієслова</h2>
            <ul>
                <li><strong>Faire:</strong> <em>Je fais, tu fais, il fait, nous faisons, vous faites, ils font.</em></li>
                <li><strong>Prendre:</strong> <em>Je prends, tu prends, il prend, nous prenons, vous prenez, ils prennent.</em></li>
                <li><strong>Venir:</strong> <em>Je viens, tu viens, il vient, nous venons, vous venez, ils viennent.</em></li>
            </ul>
            """,
            "content_html_en": """
            <h2>Key Irregular Verbs in Daily French</h2>
            <ul>
                <li><strong>Faire</strong> (to do/make), <strong>Prendre</strong> (to take), <strong>Venir</strong> (to come), <strong>Pouvoir</strong> (can), <strong>Vouloir</strong> (to want).</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les verbes irréguliers clés</h2>
            <ul>
                <li><strong>Faire</strong> : je fais, nous faisons, vous faites, ils font.</li>
                <li><strong>Prendre</strong> : je prends, nous prenons, ils prennent.</li>
                <li><strong>Venir</strong> : je viens, nous venons, ils viennent.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какая правильная форма глагола Faire для 'Vous'?",
                    "text_uk": "Яка правильна форма дієслова Faire для 'Vous'?",
                    "text_en": "What is the correct form of Faire for 'Vous'?",
                    "text_fr": "Quelle est la forme de Faire avec 'Vous' ?",
                    "choices": [
                        {"text": "Vous faites", "correct": True},
                        {"text": "Vous faisez", "correct": False},
                        {"text": "Vous font", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 46,
            "data_lesson_id": "lesson-imparfait",
            "topic": topic3,
            "title_uk": "🕰️ Минулий тривалий час (L'Imparfait)",
            "title_ru": "🕰️ Прошедшее время описания (L'Imparfait)",
            "title_en": "🕰️ The Imperfect Tense (L'Imparfait)",
            "title_fr": "🕰️ L'Imparfait de l'indicatif",
            "content_html_ru": """
            <h2>L'Imparfait: описание и привычки в прошлом</h2>
            <p>Если <em>Passé Composé</em> описывает разовое завершенное действие (*«Я купил билет»*), то <strong>Imparfait</strong> передает фон, погоду, чувства и регулярные привычки (*«Когда я жил в Брюсселе, светило солнце...»*).</p>

            <h3>Окончания Imparfait (одинаковы для всех глаголов!):</h3>
            <div class="conjugation-grid">
                <div>Je ... <strong>-ais</strong> [э]</div>
                <div>Tu ... <strong>-ais</strong> [э]</div>
                <div>Il / Elle ... <strong>-ait</strong> [э]</div>
                <div>Nous ... <strong>-ions</strong> [йон]</div>
                <div>Vous ... <strong>-iez</strong> [йе]</div>
                <div>Ils / Elles ... <strong>-aient</strong> [э]</div>
            </div>

            <div class="example-box">
                <p><strong>« Quand j'étais jeune, je prenais le tram tous les jours. »</strong><br>— Когда я был молод, я ездил на трамвае каждый день.</p>
                <p><strong>« Il faisait beau et il y avait du monde sur la Grand-Place. »</strong><br>— Была хорошая погода, и на Гран-Плас было много людей.</p>
            </div>
            """,
            "content_html_uk": """
            <h2>L'Imparfait: минулий опис та звички</h2>
            <p>Закінчення однакові для всіх дієслів: <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>.</p>
            <div class="example-box">
                <p><strong>« Quand j'étais petit... »</strong> — Коли я був маленьким...</p>
            </div>
            """,
            "content_html_en": """
            <h2>The Imperfect Tense (L'Imparfait)</h2>
            <p>Used for descriptions, background, and habits in the past:</p>
            <ul>
                <li>Endings: <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>L'Imparfait</h2>
            <p>Pour la description et les habitudes passées.</p>
            <ul>
                <li>Terminaisons : <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какое окончание имеет глагол в Imparfait для местоимения 'Nous'?",
                    "text_uk": "Яке закінчення має дієслово в Imparfait для 'Nous'?",
                    "text_en": "What is the ending of Imparfait for 'Nous'?",
                    "text_fr": "Quelle est la terminaison de l'imparfait pour 'Nous' ?",
                    "choices": [
                        {"text": "-ions (nous parlions)", "correct": True},
                        {"text": "-ons", "correct": False},
                        {"text": "-ez", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 47,
            "data_lesson_id": "lesson-futur-simple",
            "topic": topic3,
            "title_uk": "🔮 Простий майбутній час (Le Futur Simple)",
            "title_ru": "🔮 Простое будущее время (Le Futur Simple)",
            "title_en": "🔮 The Simple Future Tense (Le Futur Simple)",
            "title_fr": "🔮 Le Futur simple",
            "content_html_ru": """
            <h2>Le Futur Simple: планы и будущее</h2>
            <p>Простое будущее время образуется добавлением окончаний к <strong>инфинитиву глагола</strong>:</p>

            <div class="conjugation-grid">
                <div>Je ... <strong>-ai</strong> [е]</div>
                <div>Tu ... <strong>-as</strong> [а]</div>
                <div>Il / Elle ... <strong>-a</strong> [а]</div>
                <div>Nous ... <strong>-ons</strong> [он]</div>
                <div>Vous ... <strong>-ez</strong> [е]</div>
                <div>Ils / Elles ... <strong>-ont</strong> [он]</div>
            </div>

            <h3>Примеры:</h3>
            <div class="example-box">
                <p><strong>Parler → Je parlerai</strong> [же парлёре] (Я буду говорить)</p>
                <p><strong>Partir → Nous partirons</strong> [ну партирон] (Мы уедем)</p>
                <p><strong>Être → Je serai</strong> [же сёре] (Я буду)</p>
                <p><strong>Avoir → J'aurai</strong> [жоре] (У меня будет)</p>
            </div>
            """,
            "content_html_uk": """
            <h2>Простий майбутній час (Futur Simple)</h2>
            <p>Інфінітив + закінчення: <strong>-ai, -as, -a, -ons, -ez, -ont</strong>.</p>
            <div class="example-box">
                <p><strong>« Demain, je visiterai Gand. »</strong> — Завтра я відвідаю Гент.</p>
            </div>
            """,
            "content_html_en": """
            <h2>The Simple Future Tense (Futur Simple)</h2>
            <p>Infinitive stem + endings: <strong>-ai, -as, -a, -ons, -ez, -ont</strong>.</p>
            <ul>
                <li><em>Je parlerai, tu parleras, nous parlerons...</em></li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Le Futur simple</h2>
            <ul>
                <li>Terminaisons : <strong>-ai, -as, -a, -ons, -ez, -ont</strong>.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Как сказать 'Завтра я буду в Брюсселе' в Futur Simple?",
                    "text_uk": "Як сказати 'Завтра я буду в Брюсселі' у Futur Simple?",
                    "text_en": "How do you say 'Tomorrow I will be in Brussels' in Futur Simple?",
                    "text_fr": "Comment dire 'Demain je serai à Bruxelles' ?",
                    "choices": [
                        {"text": "Demain, je serai à Bruxelles", "correct": True},
                        {"text": "Demain, je suis à Bruxelles", "correct": False},
                        {"text": "Demain, j'étais à Bruxelles", "correct": False}
                    ]
                }
            ]
        },

        # --- Topic 4: Vocabulary additions ---
        {
            "order": 48,
            "data_lesson_id": "lesson-weather",
            "topic": topic4,
            "title_uk": "🌤️ Погода, клімат та пори року",
            "title_ru": "🌤️ Погода, климат и времена года",
            "title_en": "🌤️ Weather, Climate & Seasons",
            "title_fr": "🌤️ La météo et les saisons",
            "content_html_ru": """
            <h2>Как говорить о погоде по-французски</h2>
            <p>Разговоры о погоде — любимая тема для смолл-тока в Бельгии!</p>

            <div class="example-box">
                <p><strong>« Quel temps fait-il aujourd'hui ? »</strong> — Какая сегодня погода?</p>
                <p><strong>« Il fait beau / Il fait chaud »</strong> — Хорошая погода / Тепло (жарко).</p>
                <p><strong>« Il fait froid / Il fait gris »</strong> — Холодно / Пасмурно.</p>
                <p><strong>« Il pleut / Il drache ! »</strong> — Идёт дождь / Льёт как из ведра!</p>
                <p><strong>« Il y a du vent / du soleil / du brouillard »</strong> — Ветрено / Солнечно / Туманно.</p>
            </div>

            <h3>Времена года (Les saisons):</h3>
            <div class="conjugation-grid">
                <div><strong>🌸 Le printemps</strong><br>Весна (<em>au printemps</em>)</div>
                <div><strong>☀️ L'été</strong><br>Лето (<em>en été</em>)</div>
                <div><strong>🍂 L'automne</strong><br>Осень (<em>en automne</em>)</div>
                <div><strong>❄️ L'hiver</strong><br>Зима (<em>en hiver</em>)</div>
            </div>
            """,
            "content_html_uk": """
            <h2>Погода та пори року</h2>
            <ul>
                <li><strong>« Il fait beau »</strong> — Гарна погода.</li>
                <li><strong>« Il pleut / Il drache »</strong> — Дощить / Злива.</li>
                <li><strong>Пори року:</strong> <em>Le printemps, l'été, l'automne, l'hiver</em>.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Talking about Weather & Seasons</h2>
            <ul>
                <li><strong>« Quel temps fait-il ? »</strong> — What is the weather like?</li>
                <li><strong>« Il fait beau / Il fait froid / Il pleut »</strong></li>
                <li><strong>Seasons:</strong> <em>Le printemps, l'été, l'automne, l'hiver</em>.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>La météo et les quatre saisons</h2>
            <ul>
                <li><strong>Il fait beau / Il pleut.</strong></li>
                <li><strong>Le printemps, l'été, l'automne, l'hiver.</strong></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Какая конструкция используется во фразе 'На улице хорошая погода'?",
                    "text_uk": "Яка конструкція використовується у фразі 'Гарна погода'?",
                    "text_en": "Which phrase means 'The weather is nice'?",
                    "text_fr": "Comment dit-on 'Il fait beau' ?",
                    "choices": [
                        {"text": "Il fait beau", "correct": True},
                        {"text": "Il a beau", "correct": False},
                        {"text": "Il est beau temps", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 49,
            "data_lesson_id": "lesson-house-rooms",
            "topic": topic4,
            "title_uk": "🏠 Дім, кімнати та меблі",
            "title_ru": "🏠 Дом, комнаты и мебель",
            "title_en": "🏠 House, Rooms & Furniture",
            "title_fr": "🏠 La maison, les pièces et les meubles",
            "content_html_ru": """
            <h2>Дом и интерьер: полезная лексика</h2>

            <h3>Комнаты в квартире (Les pièces de la maison):</h3>
            <div class="conjugation-grid">
                <div><strong>Le salon</strong><br>Гостиная</div>
                <div><strong>La chambre</strong><br>Спальня</div>
                <div><strong>La cuisine</strong><br>Кухня</div>
                <div><strong>La salle de bain</strong><br>Ванная комната</div>
                <div><strong>Les toilettes / W.-C.</strong><br>Туалет</div>
                <div><strong>Le balcon</strong><br>Балкон</div>
            </div>

            <h3>Мебель и предметы (Les meubles):</h3>
            <ul>
                <li><strong>Le lit</strong> — Кровать.</li>
                <li><strong>Le canapé</strong> — Диван.</li>
                <li><strong>La table et les chaises</strong> — Стол и стулья.</li>
                <li><strong>L'armoire / Le placard</strong> — Шкаф / Встроенный шкаф.</li>
                <li><strong>Le frigo (réfrigérateur)</strong> — Холодильник.</li>
            </ul>
            """,
            "content_html_uk": """
            <h2>Дім та меблі</h2>
            <ul>
                <li><strong>Кімнати:</strong> <em>Le salon, la chambre, la cuisine, la salle de bain</em>.</li>
                <li><strong>Меблі:</strong> <em>Le lit, le canapé, la table, les chaises, le frigo</em>.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Rooms & Furniture in French</h2>
            <ul>
                <li><strong>Rooms:</strong> <em>Le salon, la chambre, la cuisine, la salle de bain</em>.</li>
                <li><strong>Furniture:</strong> <em>Le lit, le canapé, la table, l'armoire, le frigo</em>.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>La maison et le mobilier</h2>
            <ul>
                <li><strong>Les pièces :</strong> salon, chambre, cuisine, salle de bain.</li>
                <li><strong>Les meubles :</strong> lit, canapé, table, armoire, réfrigérateur.</li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Как по-французски называется 'Спальня'?",
                    "text_uk": "Як французькою називається 'Спальня'?",
                    "text_en": "How do you say 'Bedroom' in French?",
                    "text_fr": "Comment dit-on 'Bedroom' en français ?",
                    "choices": [
                        {"text": "La chambre", "correct": True},
                        {"text": "La cuisine", "correct": False},
                        {"text": "Le salon", "correct": False}
                    ]
                }
            ]
        },
        {
            "order": 50,
            "data_lesson_id": "lesson-clothes",
            "topic": topic4,
            "title_uk": "👗 Одяг, взуття та аксесуари",
            "title_ru": "👗 Одежда, обувь и аксессуары",
            "title_en": "👗 Clothes, Shoes & Accessories",
            "title_fr": "👗 Les vêtements et la mode",
            "content_html_ru": """
            <h2>Одежда и гардероб (Les vêtements)</h2>

            <div class="conjugation-grid">
                <div><strong>Le manteau</strong><br>Пальто / Тёплая куртка</div>
                <div><strong>La veste / Le blouson</strong><br>Куртка / Пиджак</div>
                <div><strong>Le pantalon / Le jean</strong><br>Брюки / Джинсы</div>
                <div><strong>La chemise</strong><br>Рубашка (мужская)</div>
                <div><strong>Le t-shirt</strong><br>Футболка</div>
                <div><strong>La robe</strong><br>Платье</div>
                <div><strong>La jupe</strong><br>Юбка</div>
                <div><strong>Le pull</strong><br>Свитер / Джемпер</div>
                <div><strong>Les chaussures</strong><br>Обувь / Туфли</div>
                <div><strong>Les baskets</strong><br>Кроссовки</div>
                <div><strong>Le bonnet & l'écharpe</strong><br>Шапка и шарф</div>
                <div><strong>Le parapluie</strong><br>Зонт (незаменим в Бельгии!)</div>
            </div>
            """,
            "content_html_uk": """
            <h2>Одяг та аксесуари</h2>
            <ul>
                <li><em>Le manteau, le pantalon, la chemise, la robe, les chaussures, les baskets, le parapluie</em>.</li>
            </ul>
            """,
            "content_html_en": """
            <h2>Clothing & Footwear</h2>
            <ul>
                <li><em>Le manteau (coat), la chemise (shirt), la robe (dress), les chaussures (shoes), les baskets (sneakers), le parapluie (umbrella)</em>.</li>
            </ul>
            """,
            "content_html_fr": """
            <h2>Les vêtements et accessoires</h2>
            <ul>
                <li><em>Manteau, pantalon, chemise, robe, chaussures, baskets, parapluie.</em></li>
            </ul>
            """,
            "questions": [
                {
                    "text_ru": "Как по-французски сказать 'Кроссовки'?",
                    "text_uk": "Як французькою сказати 'Кросівки'?",
                    "text_en": "How do you say 'Sneakers' in French?",
                    "text_fr": "Comment dit-on 'Sneakers' en français ?",
                    "choices": [
                        {"text": "Les baskets", "correct": True},
                        {"text": "Les chapeaux", "correct": False},
                        {"text": "Les manteaux", "correct": False}
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
    seed_curriculum_expansion()
    print("Curriculum database expansion complete!")
