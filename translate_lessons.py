from lessons.models import Lesson

translations = {
    "lesson1": {
        "title_en": "📚 Alphabet and Reading",
        "title_ua": "📚 Алфавіт та читання",
        "title_fr": "📚 Alphabet et lecture",
        "content_en": """
            <h2>Phonetics Basics</h2>
            <p>French is beautiful but tricky. What you see on paper is often not read the way it's written.</p>
            <h3>Complex Sounds</h3>
            <p>There are no direct equivalents for these sounds in many languages:</p>
            <ul>
                <li><strong>[y]</strong> (u) — lips in a tube like for "U", but try to say "I". (tu, salut)</li>
                <li><strong>[œ]</strong> (eu) — something between "O" and "E". (peur, fleur)</li>
                <li><strong>Nasals</strong> (an, on, in) — pronounced "through the nose" without closing the lips.</li>
            </ul>
            <div class="example-box">
                <strong>Reading Rule:</strong>
                <p>Stress is ALWAYS on the last pronounced syllable.<br>
                Letters <strong>e, s, t, d, x, z</strong> at the end of words are usually NOT pronounced.</p>
            </div>
        """,
        "content_ua": """
            <h2>Основи фонетики</h2>
            <p>Французька мова красива, але підступна. Те, що ви бачите на папері, часто читається не так, як написано.</p>
            <h3>Складні звуки</h3>
            <p>В українській мові немає повних аналогів цих звуків:</p>
            <ul>
                <li><strong>[y]</strong> (u) — губи трубочкою як для "У", але намагаємося сказати "І". (tu, salut)</li>
                <li><strong>[œ]</strong> (eu) — щось середнє між "О" та "Е". (peur, fleur)</li>
                <li><strong>Носові</strong> (an, on, in) — вимовляються "в ніс", не стуляючи губ.</li>
            </ul>
            <div class="example-box">
                <strong>Правило читання:</strong>
                <p>Наголос ЗАВЖДИ на останній склад, що вимовляється.<br>
                Букви <strong>e, s, t, d, x, z</strong> в кінці слів зазвичай НЕ читаються.</p>
            </div>
        """,
        "content_fr": """
            <h2>Bases de la phonétique</h2>
            <p>Le français est beau mais complexe. Ce que vous voyez sur le papier n'est souvent pas lu comme c'est écrit.</p>
            <h3>Sons complexes</h3>
            <p>Il n'y a pas d'équivalents directs pour ces sons dans de nombreuses langues :</p>
            <ul>
                <li><strong>[y]</strong> (u) — les lèvres en tube comme pour le "OU", mais on essaie de dire "I". (tu, salut)</li>
                <li><strong>[œ]</strong> (eu) — quelque chose entre le "O" et le "E". (peur, fleur)</li>
                <li><strong>Nasales</strong> (an, on, in) — se prononcent "par le nez", sans fermer les lèvres.</li>
            </ul>
            <div class="example-box">
                <strong>Règle de lecture :</strong>
                <p>L'accent est TOUJOURS sur la dernière syllabe prononcée.<br>
                Les lettres <strong>e, s, t, d, x, z</strong> à la fin des mots ne sont généralement PAS prononcées.</p>
            </div>
        """
    },
    "lesson-be": {
        "title_en": "🇧🇪 Belgian Features",
        "title_ua": "🇧🇪 Бельгійські особливості",
        "title_fr": "🇧🇪 Particularités belges",
        "content_en": """
            <h2>Differences from France</h2>
            <p>Belgian French is simpler and more logical! Here are the main differences that will give you away as a local.</p>
            <h3>1. Math (Numbers)</h3>
            <p>The French say "60 + 10" instead of 70. Belgians say it normally:</p>
            <div class="example-box warning">
                <p>70 — <strong>Septante</strong></p>
                <p>90 — <strong>Nonante</strong></p>
            </div>
            <h3>2. Food (Time of Day)</h3>
            <ul>
                <li>🕗 Morning: <strong>Le déjeuner</strong> (Breakfast)</li>
                <li>🕛 Afternoon: <strong>Le dîner</strong> (Lunch) <span style="color:#e74c3c;">← Important!</span></li>
                <li>🕕 Evening: <strong>Le souper</strong> (Dinner)</li>
            </ul>
            <h3>3. Vocabulary</h3>
            <p><strong>S'il vous plaît</strong> is used when you are giving something (like "here you go").</p>
        """,
        "content_ua": """
            <h2>Відмінності від Франції</h2>
            <p>Бельгійська французька простіша та логічніша! Ось головні відмінності, які видадуть у вас місцевого.</p>
            <h3>1. Математика (Числа)</h3>
            <p>Французи кажуть "60 + 10" замість 70. Бельгійці кажуть нормально:</p>
            <div class="example-box warning">
                <p>70 — <strong>Septante</strong> [септант]</p>
                <p>90 — <strong>Nonante</strong> [нонант]</p>
            </div>
            <h3>2. Їжа (Час доби)</h3>
            <ul>
                <li>🕗 Ранок: <strong>Le déjeuner</strong> (Сніданок)</li>
                <li>🕛 День: <strong>Le dîner</strong> (Обід) <span style="color:#e74c3c;">← Важливо!</span></li>
                <li>🕕 Вечір: <strong>Le souper</strong> (Вечеря)</li>
            </ul>
            <h3>3. Словник</h3>
            <p><strong>S'il vous plaît</strong> використовується, коли ви щось віддаєте (як "ось, будь ласка").</p>
        """,
        "content_fr": """
            <h2>Différences avec la France</h2>
            <p>Le français belge est plus simple et plus logique ! Voici les principales différences qui vous feront passer pour un local.</p>
            <h3>1. Mathématiques (Nombres)</h3>
            <p>Les Français disent "60 + 10" au lieu de 70. Les Belges le disent normalement :</p>
            <div class="example-box warning">
                <p>70 — <strong>Septante</strong></p>
                <p>90 — <strong>Nonante</strong></p>
            </div>
            <h3>2. Nourriture (Moments de la journée)</h3>
            <ul>
                <li>🕗 Matin : <strong>Le déjeuner</strong> (Petit-déjeuner)</li>
                <li>🕛 Midi : <strong>Le dîner</strong> (Déjeuner) <span style="color:#e74c3c;">← Important !</span></li>
                <li>🕕 Soir : <strong>Le souper</strong> (Dîner)</li>
            </ul>
            <h3>3. Vocabulaire</h3>
            <p><strong>S'il vous plaît</strong> est utilisé lorsque vous donnez quelque chose (comme "voici").</p>
        """
    },
    "lesson2": {
        "title_en": "👋 Greetings and Politeness",
        "title_ua": "👋 Привітання та ввічливість",
        "title_fr": "👋 Salutations et politesse",
        "content_en": """
            <h2>Communication Etiquette</h2>
            <h3>The Universal Key</h3>
            <div class="example-box">
                <strong>Ça va? [sa va]</strong>
                <p>A joker phrase: "How are you?", "Fine", "Everything's great!".</p>
            </div>
            <h3>Formal and Informal</h3>
            <ul>
                <li><strong>Bonjour</strong> — Hello (until 6:00 PM).</li>
                <li><strong>Bonsoir</strong> — Good evening.</li>
                <li><strong>Salut</strong> — Hi / Bye (to friends).</li>
                <li><strong>Au revoir</strong> — Goodbye.</li>
            </ul>
        """,
        "content_ua": """
            <h2>Етикет спілкування</h2>
            <h3>Універсальний ключ</h3>
            <div class="example-box">
                <strong>Ça va? [са ва]</strong>
                <p>Фраза-джокер: "Як справи?", "Нормально", "Все супер!".</p>
            </div>
            <h3>Формально та неформально</h3>
            <ul>
                <li><strong>Bonjour</strong> — Добрий день (до 18:00).</li>
                <li><strong>Bonsoir</strong> — Добрий вечір.</li>
                <li><strong>Salut</strong> — Привіт / Бувай (друзям).</li>
                <li><strong>Au revoir</strong> — До побачення.</li>
            </ul>
        """,
        "content_fr": """
            <h2>Étiquette de communication</h2>
            <h3>La clé universelle</h3>
            <div class="example-box">
                <strong>Ça va?</strong>
                <p>Une phrase joker : "Comment ça va ?", "Ça va", "Tout va bien !".</p>
            </div>
            <h3>Formel et informel</h3>
            <ul>
                <li><strong>Bonjour</strong> — Bonjour (jusqu'à 18h00).</li>
                <li><strong>Bonsoir</strong> — Bonsoir.</li>
                <li><strong>Salut</strong> — Salut (aux amis).</li>
                <li><strong>Au revoir</strong> — Au revoir.</li>
            </ul>
        """
    },
    "lesson3": {
        "title_en": "📝 Verb être (to be)",
        "title_ua": "📝 Дієслово être (бути)",
        "title_fr": "📝 Verbe être",
        "content_en": """
            <h2>The Foundation of Grammar</h2>
            <p>I am, you are... The French never omit this verb ("Je <strong>suis</strong> étudiant").</p>
            <div class="conjugation-grid">
                <div><strong>Je suis</strong><br>I am</div>
                <div><strong>Tu es</strong><br>You are</div>
                <div><strong>Il est</strong><br>He is</div>
                <div><strong>Nous sommes</strong><br>We are</div>
                <div><strong>Vous êtes</strong><br>You are</div>
                <div><strong>Ils sont</strong><br>They are</div>
            </div>
            <h3 style="margin-top:20px;">Examples:</h3>
            <ul>
                <li>Je suis fatigué — I am tired.</li>
                <li>Vous êtes belge? — Are you Belgian?</li>
            </ul>
        """,
        "content_ua": """
            <h2>Фундамент граматики</h2>
            <p>Я є, ти є... Французи ніколи не опускають це дієслово ("Je <strong>suis</strong> étudiant").</p>
            <div class="conjugation-grid">
                <div><strong>Je suis</strong><br>Я є</div>
                <div><strong>Tu es</strong><br>Ти є</div>
                <div><strong>Il est</strong><br>Він є</div>
                <div><strong>Nous sommes</strong><br>Ми є</div>
                <div><strong>Vous êtes</strong><br>Ви є</div>
                <div><strong>Ils sont</strong><br>Вони є</div>
            </div>
            <h3 style="margin-top:20px;">Приклади:</h3>
            <ul>
                <li>Je suis fatigué — Я втомився.</li>
                <li>Vous êtes belge? — Ви бельгієць?</li>
            </ul>
        """,
        "content_fr": """
            <h2>Le fondement de la grammaire</h2>
            <p>Je suis, tu es... Les Français n'omettent jamais ce verbe ("Je <strong>suis</strong> étudiant").</p>
            <div class="conjugation-grid">
                <div><strong>Je suis</strong></div>
                <div><strong>Tu es</strong></div>
                <div><strong>Il est</strong></div>
                <div><strong>Nous sommes</strong></div>
                <div><strong>Vous êtes</strong></div>
                <div><strong>Ils sont</strong></div>
            </div>
            <h3 style="margin-top:20px;">Exemples :</h3>
            <ul>
                <li>Je suis fatigué.</li>
                <li>Vous êtes belge ?</li>
            </ul>
        """
    },
    "lesson4": {
        "title_en": "🎯 Articles and Gender",
        "title_ua": "🎯 Артиклі та рід",
        "title_fr": "🎯 Articles et genre",
        "content_en": """
            <h2>The Word's Passport</h2>
            <p>The article shows the gender of the noun (masculine or feminine).</p>
            <h3>Definite (specific item)</h3>
            <ul>
                <li><strong>Le</strong> (m): Le train (the train)</li>
                <li><strong>La</strong> (f): La gare (the station)</li>
                <li><strong>L'</strong> (before a vowel): L'aéroport</li>
                <li><strong>Les</strong> (plural): Les frites</li>
            </ul>
            <h3>Indefinite (one of many)</h3>
            <ul>
                <li><strong>Un</strong> (m): Un croissant</li>
                <li><strong>Une</strong> (f): Une gaufre</li>
                <li><strong>Des</strong> (plural): Des chocolats</li>
            </ul>
        """,
        "content_ua": """
            <h2>Паспорт слова</h2>
            <p>Артикль показує рід іменника (чоловічий або жіночий).</p>
            <h3>Визначені (конкретний предмет)</h3>
            <ul>
                <li><strong>Le</strong> (ч.р.): Le train (потяг)</li>
                <li><strong>La</strong> (ж.р.): La gare (вокзал)</li>
                <li><strong>L'</strong> (перед голосною): L'aéroport</li>
                <li><strong>Les</strong> (мн.): Les frites</li>
            </ul>
            <h3>Невизначені (один із)</h3>
            <ul>
                <li><strong>Un</strong> (ч.р.): Un croissant</li>
                <li><strong>Une</strong> (ж.р.): Une gaufre</li>
                <li><strong>Des</strong> (мн.): Des chocolats</li>
            </ul>
        """,
        "content_fr": """
            <h2>Le passeport du mot</h2>
            <p>L'article indique le genre du nom (masculin ou féminin).</p>
            <h3>Définis (objet spécifique)</h3>
            <ul>
                <li><strong>Le</strong> (m.) : Le train</li>
                <li><strong>La</strong> (f.) : La gare</li>
                <li><strong>L'</strong> (devant une voyelle) : L'aéroport</li>
                <li><strong>Les</strong> (pl.) : Les frites</li>
            </ul>
            <h3>Indéfinis (un parmi d'autres)</h3>
            <ul>
                <li><strong>Un</strong> (m.) : Un croissant</li>
                <li><strong>Une</strong> (f.) : Une gaufre</li>
                <li><strong>Des</strong> (pl.) : Des chocolats</li>
            </ul>
        """
    },
    "lesson-avoir": {
        "title_en": "💼 Verb avoir (to have)",
        "title_ua": "💼 Дієслово avoir (мати)",
        "title_fr": "💼 Verbe avoir",
        "content_en": """
            <h2>The Second Pillar of Grammar</h2>
            <p>Used not only for possession ("I have") but also for age and feelings.</p>
            <div class="conjugation-grid">
                <div><strong>J'ai</strong><br>I have</div>
                <div><strong>Tu as</strong><br>You have</div>
                <div><strong>Il a</strong><br>He has</div>
                <div><strong>Nous avons</strong><br>We have</div>
                <div><strong>Vous avez</strong><br>You have</div>
                <div><strong>Ils ont</strong><br>They have</div>
            </div>
            <h3 style="margin-top:20px;">Common Expressions:</h3>
            <ul>
                <li><strong>J'ai 25 ans</strong> — I am 25 years old (literally: "I have 25 years").</li>
                <li><strong>J'ai faim</strong> — I am hungry ("I have hunger").</li>
                <li><strong>J'ai soif</strong> — I am thirsty ("I have thirst").</li>
            </ul>
        """,
        "content_ua": """
            <h2>Другий кит грамматики</h2>
            <p>Використовується не тільки для володіння ("У мене є"), але й для віку та відчуттів.</p>
            <div class="conjugation-grid">
                <div><strong>J'ai</strong> [же]<br>Я маю</div>
                <div><strong>Tu as</strong> [тю а]<br>Ти маєш</div>
                <div><strong>Il a</strong> [іль а]<br>Він має</div>
                <div><strong>Nous avons</strong> [ну за-вон]<br>Ми маємо</div>
                <div><strong>Vous avez</strong> [ву за-ве]<br>Ви маєте</div>
                <div><strong>Ils ont</strong> [іль зон]<br>Вони мають</div>
            </div>
            <h3 style="margin-top:20px;">Стійкі вирази:</h3>
            <ul>
                <li><strong>J'ai 25 ans</strong> — Мені 25 років (дослівно: "Я маю 25 років").</li>
                <li><strong>J'ai faim</strong> — Я голодний ("Маю голод").</li>
                <li><strong>J'ai soif</strong> — Я хочу пити ("Маю спрагу").</li>
            </ul>
        """,
        "content_fr": """
            <h2>Le deuxième pilier de la grammaire</h2>
            <p>Utilisé non seulement pour la possession ("J'ai") mais aussi pour l'âge et les sensations.</p>
            <div class="conjugation-grid">
                <div><strong>J'ai</strong></div>
                <div><strong>Tu as</strong></div>
                <div><strong>Il a</strong></div>
                <div><strong>Nous avons</strong></div>
                <div><strong>Vous avez</strong></div>
                <div><strong>Ils ont</strong></div>
            </div>
            <h3 style="margin-top:20px;">Expressions courantes :</h3>
            <ul>
                <li><strong>J'ai 25 ans.</strong></li>
                <li><strong>J'ai faim.</strong></li>
                <li><strong>J'ai soif.</strong></li>
            </ul>
        """
    },
    "lesson-negation": {
        "title_en": "🚫 Negation (Ne ... pas)",
        "title_ua": "🚫 Заперечення (Ne ... pas)",
        "title_fr": "🚫 La négation",
        "content_en": """
            <h2>How to say "NO"</h2>
            <p>French negation consists of two parts that "hug" the verb.</p>
            <div class="example-box">
                <strong>Ne + Verb + Pas</strong>
            </div>
            <h3>Examples:</h3>
            <ul>
                <li>Je <strong>ne</strong> suis <strong>pas</strong> français. (I am not French)</li>
                <li>Tu <strong>n'</strong>as <strong>pas</strong> faim? (Are you not hungry?) <br><em>*Ne becomes N' before a vowel.</em></li>
            </ul>
            <div class="example-box warning">
                <strong>In casual speech:</strong>
                <p>The French often "swallow" the <strong>ne</strong> particle.<br>
                "Je sais pas" instead of "Je ne sais pas".</p>
            </div>
        """,
        "content_ua": """
            <h2>Як сказати "НІ"</h2>
            <p>Французьке заперечення складається з двох частин, які "обіймають" дієслово.</p>
            <div class="example-box">
                <strong>Ne + Дієслово + Pas</strong>
            </div>
            <h3>Приклади:</h3>
            <ul>
                <li>Je <strong>ne</strong> suis <strong>pas</strong> français. (Я не француз)</li>
                <li>Tu <strong>n'</strong>as <strong>pas</strong> faim? (Ти не голодний?) <br><em>*Ne перетворюється на N' перед голосною.</em></li>
            </ul>
            <div class="example-box warning">
                <strong>У розмовній мові:</strong>
                <p>Французи часто "ковтають" частку <strong>ne</strong>.<br>
                "Je sais pas" замість "Je ne sais pas".</p>
            </div>
        """,
        "content_fr": """
            <h2>Comment dire "NON"</h2>
            <p>La négation française se compose de deux parties qui "encadrent" le verbe.</p>
            <div class="example-box">
                <strong>Ne + Verbe + Pas</strong>
            </div>
            <h3>Exemples :</h3>
            <ul>
                <li>Je <strong>ne</strong> suis <strong>pas</strong> français.</li>
                <li>Tu <strong>n'</strong>as <strong>pas</strong> faim ? <br><em>*Ne devient N' devant une voyelle.</em></li>
            </ul>
            <div class="example-box warning">
                <strong>À l'oral :</strong>
                <p>Les Français omettent souvent le <strong>ne</strong>.<br>
                "Je sais pas" au lieu de "Je ne sais pas".</p>
            </div>
        """
    },
    "lesson-er-verbs": {
        "title_en": "🏃 Group 1 Verbs (-ER)",
        "title_ua": "🏃 Дієслова 1-ї групи (-ER)",
        "title_fr": "🏃 Verbes du 1er groupe",
        "content_en": """
            <h2>Thousands of Verbs, One Rule</h2>
            <p>Verbs ending in <strong>-ER</strong> (parler, habiter, aimer) are conjugated the same way.</p>
            <h3>Scheme (using Parler as an example):</h3>
            <p>Remove -er, add endings:</p>
            <div class="conjugation-grid">
                <div>Je parl<strong>e</strong> (silent)</div>
                <div>Tu parl<strong>es</strong> (silent)</div>
                <div>Il parl<strong>e</strong> (silent)</div>
                <div>Nous parl<strong>ons</strong> [on]</div>
                <div>Vous parl<strong>ez</strong> [ay]</div>
                <div>Ils parl<strong>ent</strong> (silent!)</div>
            </div>
            <p><strong>Important:</strong> In 4 out of 6 forms, the ending is not pronounced! "Parle, parles, parle, parlent" sound identical.</p>
        """,
        "content_ua": """
            <h2>Тисячі дієслів за одним правилом</h2>
            <p>Дієслова, що закінчуються на <strong>-ER</strong> (parler, habiter, aimer), відмінюються однаково.</p>
            <h3>Схема (на прикладі Parler):</h3>
            <p>Прибираємо -er, додаємо закінчення:</p>
            <div class="conjugation-grid">
                <div>Je parl<strong>e</strong> (не читається)</div>
                <div>Tu parl<strong>es</strong> (не читається)</div>
                <div>Il parl<strong>e</strong> (не читається)</div>
                <div>Nous parl<strong>ons</strong> [он]</div>
                <div>Vous parl<strong>ez</strong> [е]</div>
                <div>Ils parl<strong>ent</strong> (не читається!)</div>
            </div>
            <p><strong>Важливо:</strong> У 4 з 6 форм закінчення не вимовляється! "Parle, parles, parle, parlent" звучать однаково.</p>
        """,
        "content_fr": """
            <h2>Des milliers de verbes, une seule règle</h2>
            <p>Les verbes se terminant par <strong>-ER</strong> (parler, habiter, aimer) se conjuguent de la même manière.</p>
            <h3>Schéma (exemple : Parler) :</h3>
            <p>On enlève -er, on ajoute les terminaisons :</p>
            <div class="conjugation-grid">
                <div>Je parl<strong>e</strong></div>
                <div>Tu parl<strong>es</strong></div>
                <div>Il parl<strong>e</strong></div>
                <div>Nous parl<strong>ons</strong></div>
                <div>Vous parl<strong>ez</strong></div>
                <div>Ils parl<strong>ent</strong></div>
            </div>
            <p><strong>Important :</strong> Pour 4 des 6 formes, la terminaison ne se prononce pas ! "Parle, parles, parle, parlent" se prononcent de la même façon.</p>
        """
    },
    "lesson-adjectives": {
        "title_en": "🎨 Adjectives",
        "title_ua": "🎨 Прикметники",
        "title_fr": "🎨 Les adjectifs",
        "content_en": """
            <h2>Making Speech Colorful</h2>
            <p>Adjectives in French must agree with the noun in gender and number.</p>
            <h3>Feminine Gender (+e)</h3>
            <ul>
                <li>Il est petit (He is small) → Elle est petit<strong>e</strong> (She is small).</li>
                <li>Il est grand → Elle est grand<strong>e</strong>.</li>
            </ul>
            <h3>Plural Number (+s)</h3>
            <ul>
                <li>Ils sont petits. (They are small)</li>
            </ul>
            <div class="example-box">
                <strong>Adjective Placement:</strong>
                <p>Usually AFTER the noun: <em>Une voiture rouge</em>.<br>
                But short and common ones (good, bad, big, small) are placed BEFORE: <em>Une petite maison</em>.</p>
            </div>
        """,
        "content_ua": """
            <h2>Робимо мову яскравою</h2>
            <p>Прикметники у французькій мові мають узгоджуватися з іменником у роді та числі.</p>
            <h3>Жіночий рід (+e)</h3>
            <ul>
                <li>Il est petit (Він маленький) → Elle est petit<strong>e</strong> (Вона маленька).</li>
                <li>Il est grand → Elle est grand<strong>e</strong>.</li>
            </ul>
            <h3>Множина (+s)</h3>
            <ul>
                <li>Ils sont petits. (Вони маленькі)</li>
            </ul>
            <div class="example-box">
                <strong>Місце прикметника:</strong>
                <p>Зазвичай ПІСЛЯ іменника: <em>Une voiture rouge</em>.<br>
                Але короткі та часті (хороший, поганий, великий, маленький) ставляться ДО: <em>Une petite maison</em>.</p>
            </div>
        """,
        "content_fr": """
            <h2>Colorer le discours</h2>
            <p>En français, les adjectifs doivent s'accorder en genre et en nombre avec le nom.</p>
            <h3>Féminin (+e)</h3>
            <ul>
                <li>Il est petit → Elle est petit<strong>e</strong>.</li>
                <li>Il est grand → Elle est grand<strong>e</strong>.</li>
            </ul>
            <h3>Pluriel (+s)</h3>
            <ul>
                <li>Ils sont petits.</li>
            </ul>
            <div class="example-box">
                <strong>Place de l'adjectif :</strong>
                <p>Généralement APRÈS le nom : <em>Une voiture rouge</em>.<br>
                Mais les adjectifs courts et fréquents (bon, mauvais, grand, petit) se placent AVANT : <em>Une petite maison</em>.</p>
            </div>
        """
    },
    "lesson-questions": {
        "title_en": "❓ Asking Questions",
        "title_ua": "❓ Ставимо запитання",
        "title_fr": "❓ Poser des questions",
        "content_en": """
            <h2>Three Ways to Ask</h2>
            <p>From simple to complex.</p>
            <h3>1. Intonation (Casual)</h3>
            <p>Just raise your voice at the end.<br>
            — Tu habites à Bruxelles? (Do you live in Brussels?)</p>
            <h3>2. Est-ce que (Neutral)</h3>
            <p>The magic phrase "Es-kuh" at the beginning.<br>
            — <strong>Est-ce que</strong> tu habites à Bruxelles?</p>
            <h3>3. Inversion (Formal)</h3>
            <p>Swap the verb and the pronoun.<br>
            — Habites-tu à Bruxelles?</p>
            <hr>
            <p><strong>Question Words:</strong> Qui (who), Quoi (what), Où (where), Quand (when), Pourquoi (why).</p>
        """,
        "content_ua": """
            <h2>Три способи запитати</h2>
            <p>Від простого до складного.</p>
            <h3>1. Інтонація (Розмовний)</h3>
            <p>Просто підвищуємо голос наприкінці.<br>
            — Tu habites à Bruxelles? (Ти живеш у Брюсселі?)</p>
            <h3>2. Est-ce que (Нейтральний)</h3>
            <p>Магічна фраза "Ес-кьо" на початку.<br>
            — <strong>Est-ce que</strong> tu habites à Bruxelles?</p>
            <h3>3. Інверсія (Офіційний)</h3>
            <p>Міняємо дієслово та займенник місцями.<br>
            — Habites-tu à Bruxelles?</p>
            <hr>
            <p><strong>Питальні слова:</strong> Qui (хто), Quoi (що), Où (де), Quand (коли), Pourquoi (чому).</p>
        """,
        "content_fr": """
            <h2>Trois façons de poser une question</h2>
            <p>Du plus simple au plus complexe.</p>
            <h3>1. L'intonation (familier)</h3>
            <p>On monte simplement la voix à la fin.<br>
            — Tu habites à Bruxelles ?</p>
            <h3>2. Est-ce que (neutre)</h3>
            <p>La phrase magique au début.<br>
            — <strong>Est-ce que</strong> tu habites à Bruxelles ?</p>
            <h3>3. L'inversion (soutenu)</h3>
            <p>On inverse le verbe et le pronom.<br>
            — Habites-tu à Bruxelles ?</p>
            <hr>
            <p><strong>Mots interrogatifs :</strong> Qui, Quoi, Où, Quand, Pourquoi.</p>
        """
    },
    "lesson-futur-proche": {
        "title_en": "🔮 Near Future",
        "title_ua": "🔮 Найближче майбутнє",
        "title_fr": "🔮 Le futur proche",
        "content_en": """
            <h2>Futur Proche</h2>
            <p>The easiest way to talk about plans ("I am going to do...").</p>
            <div class="example-box">
                <strong>Verb Aller (to go) + Infinitive</strong>
            </div>
            <h3>Examples:</h3>
            <ul>
                <li>Je <strong>vais</strong> manger. (I am going to eat).</li>
                <li>Tu <strong>vas</strong> dormir? (Are you going to sleep?)</li>
                <li>Nous <strong>allons</strong> partir. (We are leaving).</li>
            </ul>
            <p>You only need to learn the conjugation of the verb <em>Aller</em>!</p>
        """,
        "content_ua": """
            <h2>Futur Proche</h2>
            <p>Найпростіший спосіб сказати про плани ("Я збираюся зробити...").</p>
            <div class="example-box">
                <strong>Дієслово Aller (йти) + Інфінітив</strong>
            </div>
            <h3>Приклади:</h3>
            <ul>
                <li>Je <strong>vais</strong> manger. (Я збираюся поїсти / Я поїм).</li>
                <li>Tu <strong>vas</strong> dormir? (Ти будеш спати?)</li>
                <li>Nous <strong>allons</strong> partir. (Ми їдемо).</li>
            </ul>
            <p>Потрібно лише вивчити відмінювання дієслова <em>Aller</em>!</p>
        """,
        "content_fr": """
            <h2>Le futur proche</h2>
            <p>La façon la plus simple de parler de ses projets ("Je vais faire...").</p>
            <div class="example-box">
                <strong>Verbe Aller + Infinitif</strong>
            </div>
            <h3>Exemples :</h3>
            <ul>
                <li>Je <strong>vais</strong> manger.</li>
                <li>Tu <strong>vas</strong> dormir ?</li>
                <li>Nous <strong>allons</strong> partir.</li>
            </ul>
            <p>Il suffit d'apprendre la conjugaison du verbe <em>Aller</em> !</p>
        """
    },
    "lesson-passe-compose": {
        "title_en": "🕰 Past Tense",
        "title_ua": "🕰 Минулий час",
        "title_fr": "🕰 Le passé composé",
        "content_en": """
            <h2>Passé Composé</h2>
            <p>The main past tense for completed actions.</p>
            <div class="example-box">
                <strong>Auxiliary Verb (Avoir) + Participle</strong>
            </div>
            <h3>How to form the participle?</h3>
            <ul>
                <li>Verbs ending in -ER (parler) → <strong>é</strong> (parlé)</li>
                <li>Manger → Mangé (eaten)</li>
                <li>Regarder → Regardé (watched)</li>
            </ul>
            <h3>Examples:</h3>
            <ul>
                <li>J'<strong>ai</strong> mangé une pizza. (I ate a pizza).</li>
                <li>Tu <strong>as</strong> regardé le film. (You watched the movie).</li>
            </ul>
        """,
        "content_ua": """
            <h2>Passé Composé</h2>
            <p>Основний минулий час для закінчених дій.</p>
            <div class="example-box">
                <strong>Допоміжне дієслово (Avoir) + Дієприкметник</strong>
            </div>
            <h3>Як утворити дієприкметник?</h3>
            <ul>
                <li>Дієслова на -ER (parler) → <strong>é</strong> (parlé)</li>
                <li>Manger → Mangé (поїв)</li>
                <li>Regarder → Regardé (подивився)</li>
            </ul>
            <h3>Приклади:</h3>
            <ul>
                <li>J'<strong>ai</strong> mangé une pizza. (Я з'їв піцу).</li>
                <li>Tu <strong>as</strong> regardé le film. (Ти подивився фільм).</li>
            </ul>
        """,
        "content_fr": """
            <h2>Le passé composé</h2>
            <p>Le principal temps du passé pour les actions terminées.</p>
            <div class="example-box">
                <strong>Auxiliaire (Avoir) + Participe passé</strong>
            </div>
            <h3>Comment former le participe passé ?</h3>
            <ul>
                <li>Verbes en -ER (parler) → <strong>é</strong> (parlé)</li>
                <li>Manger → Mangé</li>
                <li>Regarder → Regardé</li>
            </ul>
            <h3>Exemples :</h3>
            <ul>
                <li>J'<strong>ai</strong> mangé une pizza.</li>
                <li>Tu <strong>as</strong> regardé le film.</li>
            </ul>
        """
    },
    "lesson-prepositions": {
        "title_en": "📍 Prepositions of Place",
        "title_ua": "📍 Прийменники місця",
        "title_fr": "📍 Les prépositions de lieu",
        "content_en": """
            <h2>Where are you?</h2>
            <h3>Cities (À)</h3>
            <p>With cities, we always use <strong>à</strong>.<br>
            — J'habite <strong>à</strong> Paris, <strong>à</strong> Moscow.</p>
            <h3>Countries (En / Au)</h3>
            <ul>
                <li>Feminine (ending in -e): <strong>En</strong> France, <strong>En</strong> Belgique.</li>
                <li>Masculine: <strong>Au</strong> Japon, <strong>Au</strong> Canada.</li>
            </ul>
            <h3>At someone's place (Chez)</h3>
            <p>If you are going to a person or are at their place.<br>
            — Je suis <strong>chez</strong> moi. (I am at home).<br>
            — Je vais <strong>chez</strong> le docteur. (I am going to the doctor).</p>
        """,
        "content_ua": """
            <h2>Де ви знаходитесь?</h2>
            <h3>Міста (À)</h3>
            <p>З містами завжди використовуємо <strong>à</strong>.<br>
            — J'habite <strong>à</strong> Paris, <strong>à</strong> Moscou.</p>
            <h3>Країни (En / Au)</h3>
            <ul>
                <li>Жіночий рід (закінчуються на -e): <strong>En</strong> France, <strong>En</strong> Belgique.</li>
                <li>Чоловічий рід: <strong>Au</strong> Japon, <strong>Au</strong> Canada.</li>
            </ul>
            <h3>У когось (Chez)</h3>
            <p>Якщо ви йдете до людини або перебуваєте у неї.<br>
            — Je suis <strong>chez</strong> moi. (Я у себе вдома).<br>
            — Je vais <strong>chez</strong> le docteur. (Я йду до лікаря).</p>
        """,
        "content_fr": """
            <h2>Où êtes-vous ?</h2>
            <h3>Les villes (À)</h3>
            <p>Avec les villes, on utilise toujours <strong>à</strong>.<br>
            — J'habite <strong>à</strong> Paris, <strong>à</strong> Moscou.</p>
            <h3>Les pays (En / Au)</h3>
            <ul>
                <li>Féminin (se terminant par -e) : <strong>En</strong> France, <strong>En</strong> Belgique.</li>
                <li>Masculin : <strong>Au</strong> Japon, <strong>Au</strong> Canada.</li>
            </ul>
            <h3>Chez quelqu'un (Chez)</h3>
            <p>Si vous allez chez une personne ou si vous y êtes.<br>
            — Je suis <strong>chez</strong> moi.<br>
            — Je vais <strong>chez</strong> le médecin.</p>
        """
    },
    "lesson-reflexive": {
        "title_en": "🔄 Reflexive Verbs",
        "title_ua": "🔄 Зворотні дієслова",
        "title_fr": "🔄 Les verbes pronominaux",
        "content_en": """
            <h2>Actions on Oneself</h2>
            <p>Verbs with the "self" particle (to wash oneself, to dress oneself).</p>
            <h3>Se laver (To wash oneself)</h3>
            <div class="conjugation-grid">
                <div>Je <strong>me</strong> lave</div>
                <div>Tu <strong>te</strong> laves</div>
                <div>Il <strong>se</strong> lave</div>
                <div>Nous <strong>nous</strong> lavons</div>
                <div>Vous <strong>vous</strong> lavez</div>
                <div>Ils <strong>se</strong> lavent</div>
            </div>
            <p><strong>Important:</strong> In the past tense, these verbs are conjugated with <em>Être</em>!</p>
        """,
        "content_ua": """
            <h2>Дії над собою</h2>
            <p>Дієслова з часткою "ся" (вмиватися, одягатися).</p>
            <h3>Se laver (Вмиватися)</h3>
            <div class="conjugation-grid">
                <div>Je <strong>me</strong> lave</div>
                <div>Tu <strong>te</strong> laves</div>
                <div>Il <strong>se</strong> lave</div>
                <div>Nous <strong>nous</strong> lavons</div>
                <div>Vous <strong>vous</strong> lavez</div>
                <div>Ils <strong>se</strong> lavent</div>
            </div>
            <p><strong>Важливо:</strong> У минулому часі такі дієслова відмінюються з <em>Être</em>!</p>
        """,
        "content_fr": """
            <h2>Actions sur soi-même</h2>
            <p>Verbes avec la particule "se" (se laver, s'habiller).</p>
            <h3>Se laver</h3>
            <div class="conjugation-grid">
                <div>Je <strong>me</strong> lave</div>
                <div>Tu <strong>te</strong> laves</div>
                <div>Il <strong>se</strong> lave</div>
                <div>Nous <strong>nous</strong> lavons</div>
                <div>Vous <strong>vous</strong> lavez</div>
                <div>Ils <strong>se</strong> lavent</div>
            </div>
            <p><strong>Important :</strong> Au passé composé, ces verbes se conjuguent avec l'auxiliaire <em>Être</em> !</p>
        """
    },
    "lesson-video": {
        "title_en": "🎬 Video Materials",
        "title_ua": "🎬 Відеоматеріали",
        "title_fr": "🎬 Supports vidéo",
        "content_en": """
            <h2>Immersion</h2>
            <p>The best way to get used to the melody of the language.</p>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/KkH5N1vV8MI" allowfullscreen></iframe>
            </div>
            <div class="example-box">
                <strong>Tip:</strong>
                <p>In the video settings, turn on French subtitles (CC) to see how the words are spelled.</p>
            </div>
        """,
        "content_ua": """
            <h2>Занурення в середовище</h2>
            <p>Найкращий спосіб звикнути до мелодики мови.</p>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/KkH5N1vV8MI" allowfullscreen></iframe>
            </div>
            <div class="example-box">
                <strong>Порада:</strong>
                <p>У налаштуваннях відео увімкніть французькі субтитри (CC), щоб бачити написання слів.</p>
            </div>
        """,
        "content_fr": """
            <h2>Immersion</h2>
            <p>La meilleure façon de s'habituer à la mélodie de la langue.</p>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/KkH5N1vV8MI" allowfullscreen></iframe>
            </div>
            <div class="example-box">
                <strong>Conseil :</strong>
                <p>Dans les paramètres de la vidéo, activez les sous-titres français (CC) pour voir l'orthographe des mots.</p>
            </div>
        """
    }
}

count = 0
for lesson_id, data in translations.items():
    try:
        lesson = Lesson.objects.get(data_lesson_id=lesson_id)
        lesson.title_en = data["title_en"]
        lesson.title_ua = data["title_ua"]
        lesson.title_fr = data["title_fr"]
        lesson.content_html_en = data["content_en"]
        lesson.content_html_ua = data["content_ua"]
        lesson.content_html_fr = data["content_fr"]
        lesson.save()
        count += 1
    except Lesson.DoesNotExist:
        print(f"Lesson {lesson_id} not found")

print(f"Successfully updated {count} lessons with translations.")
