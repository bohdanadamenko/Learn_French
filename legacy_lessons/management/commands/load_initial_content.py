from django.core.management.base import BaseCommand
from lessons.models import Lesson


class Command(BaseCommand):
    help = 'Загружает расширенный контент уроков (A0-A2) в базу данных'

    def handle(self, *args, **options):
        # Удаляем существующие уроки
        Lesson.objects.all().delete()
        
        lessons_data = [
            # --- A0: The Foundation ---
            {
                'title': '📚 Алфавит и чтение',
                'data_lesson_id': 'lesson1',
                'order': 1,
                'content_html': '''
                    <h2>Основы фонетики</h2>
                    <p>Французский язык красив, но коварен. То, что вы видите на бумаге, часто не читается так, как написано.</p>
                    <h3>Сложные звуки</h3>
                    <p>В русском языке нет полных аналогов этих звуков:</p>
                    <ul>
                        <li><strong>[y]</strong> (u) — губы трубочкой как для "У", но пытаемся сказать "И". (tu, salut)</li>
                        <li><strong>[œ]</strong> (eu) — что-то среднее между "О" и "Э". (peur, fleur)</li>
                        <li><strong>Носовые</strong> (an, on, in) — произносятся "в нос", не смыкая губ.</li>
                    </ul>
                    <div class="example-box">
                        <strong>Правило чтения:</strong>
                        <p>Ударение ВСЕГДА на последний произносимый слог.<br>
                        Буквы <strong>e, s, t, d, x, z</strong> в конце слов обычно НЕ читаются.</p>
                    </div>
                '''
            },
            {
                'title': '🇧🇪 Бельгийские особенности',
                'data_lesson_id': 'lesson-be',
                'order': 2,
                'content_html': '''
                    <h2>Отличия от Франции</h2>
                    <p>Бельгийский французский проще и логичнее! Вот главные отличия, которые выдадут в вас местного.</p>
                    <h3>1. Математика (Числа)</h3>
                    <p>Французы говорят "60 + 10" вместо 70. Бельгийцы говорят нормально:</p>
                    <div class="example-box warning">
                        <p>70 — <strong>Septante</strong> [септант]</p>
                        <p>90 — <strong>Nonante</strong> [нонант]</p>
                    </div>
                    <h3>2. Еда (Время суток)</h3>
                    <ul>
                        <li>🕗 Утро: <strong>Le déjeuner</strong> (Завтрак)</li>
                        <li>🕛 День: <strong>Le dîner</strong> (Обед) <span style="color:#e74c3c;">← Важно!</span></li>
                        <li>🕕 Вечер: <strong>Le souper</strong> (Ужин)</li>
                    </ul>
                    <h3>3. Словарь</h3>
                    <p><strong>S'il vous plaît</strong> используется, когда вы что-то отдаете (как "вот, пожалуйста").</p>
                '''
            },
            {
                'title': '👋 Приветствия и вежливость',
                'data_lesson_id': 'lesson2',
                'order': 3,
                'content_html': '''
                    <h2>Этикет общения</h2>
                    <h3>Универсальный ключ</h3>
                    <div class="example-box">
                        <strong>Ça va? [са ва]</strong>
                        <p>Фраза-джокер: "Как дела?", "Нормально", "Всё супер!".</p>
                    </div>
                    <h3>Формально и неформально</h3>
                    <ul>
                        <li><strong>Bonjour</strong> — Здравствуйте (до 18:00).</li>
                        <li><strong>Bonsoir</strong> — Добрый вечер.</li>
                        <li><strong>Salut</strong> — Привет / Пока (друзьям).</li>
                        <li><strong>Au revoir</strong> — До свидания.</li>
                    </ul>
                '''
            },
            {
                'title': '📝 Глагол être (быть)',
                'data_lesson_id': 'lesson3',
                'order': 4,
                'content_html': '''
                    <h2>Фундамент грамматики</h2>
                    <p>Я есть, ты есть... Французы никогда не опускают этот глагол ("Je <strong>suis</strong> étudiant").</p>
                    <div class="conjugation-grid">
                        <div><strong>Je suis</strong><br>Я есть</div>
                        <div><strong>Tu es</strong><br>Ты есть</div>
                        <div><strong>Il est</strong><br>Он есть</div>
                        <div><strong>Nous sommes</strong><br>Мы есть</div>
                        <div><strong>Vous êtes</strong><br>Вы есть</div>
                        <div><strong>Ils sont</strong><br>Они есть</div>
                    </div>
                    <h3 style="margin-top:20px;">Примеры:</h3>
                    <ul>
                        <li>Je suis fatigué — Я устал.</li>
                        <li>Vous êtes belge? — Вы бельгиец?</li>
                    </ul>
                '''
            },
            {
                'title': '🎯 Артикли и род',
                'data_lesson_id': 'lesson4',
                'order': 5,
                'content_html': '''
                    <h2>Паспорт слова</h2>
                    <p>Артикль показывает род существительного (мужской или женский).</p>
                    <h3>Определенные (конкретный предмет)</h3>
                    <ul>
                        <li><strong>Le</strong> (м.р.): Le train (поезд)</li>
                        <li><strong>La</strong> (ж.р.): La gare (вокзал)</li>
                        <li><strong>L'</strong> (перед гласной): L'aéroport</li>
                        <li><strong>Les</strong> (мн.ч.): Les frites</li>
                    </ul>
                    <h3>Неопределенные (один из)</h3>
                    <ul>
                        <li><strong>Un</strong> (м.р.): Un croissant</li>
                        <li><strong>Une</strong> (ж.р.): Une gaufre</li>
                        <li><strong>Des</strong> (мн.ч.): Des chocolats</li>
                    </ul>
                '''
            },

            # --- A1: Building Sentences ---
            {
                'title': '💼 Глагол avoir (иметь)',
                'data_lesson_id': 'lesson-avoir',
                'order': 6,
                'content_html': '''
                    <h2>Второй кит грамматики</h2>
                    <p>Используется не только для владения ("У меня есть"), но и для возраста и ощущений.</p>
                    <div class="conjugation-grid">
                        <div><strong>J'ai</strong> [же]<br>Я имею</div>
                        <div><strong>Tu as</strong> [тю а]<br>Ты имеешь</div>
                        <div><strong>Il a</strong> [иль а]<br>Он имеет</div>
                        <div><strong>Nous avons</strong> [ну за-вон]<br>Мы имеем</div>
                        <div><strong>Vous avez</strong> [ву за-ве]<br>Вы имеете</div>
                        <div><strong>Ils ont</strong> [иль зон]<br>Они имеют</div>
                    </div>
                    <h3 style="margin-top:20px;">Устойчивые выражения:</h3>
                    <ul>
                        <li><strong>J'ai 25 ans</strong> — Мне 25 лет (дословно: "Я имею 25 лет").</li>
                        <li><strong>J'ai faim</strong> — Я голоден ("Имею голод").</li>
                        <li><strong>J'ai soif</strong> — Я хочу пить ("Имею жажду").</li>
                    </ul>
                '''
            },
            {
                'title': '🚫 Отрицание (Ne ... pas)',
                'data_lesson_id': 'lesson-negation',
                'order': 7,
                'content_html': '''
                    <h2>Как сказать "НЕТ"</h2>
                    <p>Французское отрицание состоит из двух частей, которые "обнимают" глагол.</p>
                    <div class="example-box">
                        <strong>Ne + Глагол + Pas</strong>
                    </div>
                    <h3>Примеры:</h3>
                    <ul>
                        <li>Je <strong>ne</strong> suis <strong>pas</strong> français. (Я не француз)</li>
                        <li>Tu <strong>n'</strong>as <strong>pas</strong> faim? (Ты не голоден?) <br><em>*Ne превращается в N' перед гласной.</em></li>
                    </ul>
                    <div class="example-box warning">
                        <strong>В разговорной речи:</strong>
                        <p>Французы часто "глотают" частицу <strong>ne</strong>.<br>
                        "Je sais pas" вместо "Je ne sais pas".</p>
                    </div>
                '''
            },
            {
                'title': '🏃 Глаголы 1-й группы (-ER)',
                'data_lesson_id': 'lesson-er-verbs',
                'order': 8,
                'content_html': '''
                    <h2>Тысячи глаголов по одному правилу</h2>
                    <p>Глаголы, оканчивающиеся на <strong>-ER</strong> (parler, habiter, aimer), спрягаются одинаково.</p>
                    <h3>Схема (на примере Parler):</h3>
                    <p>Убираем -er, добавляем окончания:</p>
                    <div class="conjugation-grid">
                        <div>Je parl<strong>e</strong> (не читается)</div>
                        <div>Tu parl<strong>es</strong> (не читается)</div>
                        <div>Il parl<strong>e</strong> (не читается)</div>
                        <div>Nous parl<strong>ons</strong> [он]</div>
                        <div>Vous parl<strong>ez</strong> [э]</div>
                        <div>Ils parl<strong>ent</strong> (не читается!)</div>
                    </div>
                    <p><strong>Важно:</strong> В 4 из 6 форм окончание не произносится! "Parle, parles, parle, parlent" звучат одинаково.</p>
                '''
            },
            {
                'title': '🎨 Прилагательные',
                'data_lesson_id': 'lesson-adjectives',
                'order': 9,
                'content_html': '''
                    <h2>Делаем речь красочной</h2>
                    <p>Прилагательные во французском должны согласовываться с существительным в роде и числе.</p>
                    <h3>Женский род (+e)</h3>
                    <ul>
                        <li>Il est petit (Он маленький) → Elle est petit<strong>e</strong> (Она маленькая).</li>
                        <li>Il est grand → Elle est grand<strong>e</strong>.</li>
                    </ul>
                    <h3>Множественное число (+s)</h3>
                    <ul>
                        <li>Ils sont petits. (Они маленькие)</li>
                    </ul>
                    <div class="example-box">
                        <strong>Место прилагательного:</strong>
                        <p>Обычно ПОСЛЕ существительного: <em>Une voiture rouge</em>.<br>
                        Но короткие и частые (хороший, плохой, большой, маленький) ставятся ДО: <em>Une petite maison</em>.</p>
                    </div>
                '''
            },
            {
                'title': '❓ Задаем вопросы',
                'data_lesson_id': 'lesson-questions',
                'order': 10,
                'content_html': '''
                    <h2>Три способа спросить</h2>
                    <p>От простого к сложному.</p>
                    <h3>1. Интонация (Разговорный)</h3>
                    <p>Просто повышаем голос в конце.<br>
                    — Tu habites à Bruxelles? (Ты живешь в Брюсселе?)</p>
                    <h3>2. Est-ce que (Нейтральный)</h3>
                    <p>Магическая фраза "Эс-кё" в начале.<br>
                    — <strong>Est-ce que</strong> tu habites à Bruxelles?</p>
                    <h3>3. Инверсия (Формальный)</h3>
                    <p>Меняем глагол и местоимение местами.<br>
                    — Habites-tu à Bruxelles?</p>
                    <hr>
                    <p><strong>Вопросительные слова:</strong> Qui (кто), Quoi (что), Où (где), Quand (когда), Pourquoi (почему).</p>
                '''
            },

            # --- A2: Moving Forward ---
            {
                'title': '🔮 Ближайшее будущее',
                'data_lesson_id': 'lesson-futur-proche',
                'order': 11,
                'content_html': '''
                    <h2>Futur Proche</h2>
                    <p>Самый простой способ сказать о планах ("Я собираюсь сделать...").</p>
                    <div class="example-box">
                        <strong>Глагол Aller (идти) + Инфинитив</strong>
                    </div>
                    <h3>Примеры:</h3>
                    <ul>
                        <li>Je <strong>vais</strong> manger. (Я собираюсь поесть / Я поем).</li>
                        <li>Tu <strong>vas</strong> dormir? (Ты будешь спать?)</li>
                        <li>Nous <strong>allons</strong> partir. (Мы уезжаем).</li>
                    </ul>
                    <p>Нужно только выучить спряжение глагола <em>Aller</em>!</p>
                '''
            },
            {
                'title': '🕰 Прошедшее время',
                'data_lesson_id': 'lesson-passe-compose',
                'order': 12,
                'content_html': '''
                    <h2>Passé Composé</h2>
                    <p>Основное прошедшее время для законченных действий.</p>
                    <div class="example-box">
                        <strong>Вспомогательный глагол (Avoir) + Причастие</strong>
                    </div>
                    <h3>Как образовать причастие?</h3>
                    <ul>
                        <li>Глаголы на -ER (parler) → <strong>é</strong> (parlé)</li>
                        <li>Manger → Mangé (поел)</li>
                        <li>Regarder → Regardé (посмотрел)</li>
                    </ul>
                    <h3>Примеры:</h3>
                    <ul>
                        <li>J'<strong>ai</strong> mangé une pizza. (Я съел пиццу).</li>
                        <li>Tu <strong>as</strong> regardé le film. (Ты посмотрел фильм).</li>
                    </ul>
                '''
            },
            {
                'title': '📍 Предлоги места',
                'data_lesson_id': 'lesson-prepositions',
                'order': 13,
                'content_html': '''
                    <h2>Где вы находитесь?</h2>
                    <h3>Города (À)</h3>
                    <p>С городами всегда используем <strong>à</strong>.<br>
                    — J'habite <strong>à</strong> Paris, <strong>à</strong> Moscou.</p>
                    <h3>Страны (En / Au)</h3>
                    <ul>
                        <li>Женский род (оканчиваются на -e): <strong>En</strong> France, <strong>En</strong> Belgique.</li>
                        <li>Мужской род: <strong>Au</strong> Japon, <strong>Au</strong> Canada.</li>
                    </ul>
                    <h3>У кого-то (Chez)</h3>
                    <p>Если вы идете к человеку или находитесь у него.<br>
                    — Je suis <strong>chez</strong> moi. (Я у себя дома).<br>
                    — Je vais <strong>chez</strong> le docteur. (Я иду к врачу).</p>
                '''
            },
            {
                'title': '🔄 Возвратные глаголы',
                'data_lesson_id': 'lesson-reflexive',
                'order': 14,
                'content_html': '''
                    <h2>Действия над собой</h2>
                    <p>Глаголы с частицей "ся" (умываться, одеваться).</p>
                    <h3>Se laver (Умываться)</h3>
                    <div class="conjugation-grid">
                        <div>Je <strong>me</strong> lave</div>
                        <div>Tu <strong>te</strong> laves</div>
                        <div>Il <strong>se</strong> lave</div>
                        <div>Nous <strong>nous</strong> lavons</div>
                        <div>Vous <strong>vous</strong> lavez</div>
                        <div>Ils <strong>se</strong> lavent</div>
                    </div>
                    <p><strong>Важно:</strong> В прошедшем времени такие глаголы спрягаются с <em>Être</em>!</p>
                '''
            },
            {
                'title': '🎬 Видеоматериалы',
                'data_lesson_id': 'lesson-video',
                'order': 15,
                'content_html': '''
                    <h2>Погружение в среду</h2>
                    <p>Лучший способ привыкнуть к мелодике языка.</p>
                    <div class="video-container">
                        <iframe src="https://www.youtube.com/embed/KkH5N1vV8MI" allowfullscreen></iframe>
                    </div>
                    <div class="example-box">
                        <strong>Совет:</strong>
                        <p>В настройках видео включите французские субтитры (CC), чтобы видеть написание слов.</p>
                    </div>
                '''
            },
        ]
        
        for lesson_data in lessons_data:
            lesson = Lesson.objects.create(**lesson_data)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Создан урок: {lesson.title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Успешно загружено {len(lessons_data)} уроков!')
        )
