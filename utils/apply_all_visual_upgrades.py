"""
Comprehensive script to apply all visual & interactive upgrades to:
- Lesson 1: Alphabet & Phonetics (26 audio buttons, callout tips, flip cards)
- Lesson-be: Belgian French (audio buttons, dialogue bubbles, Belgian callouts)
- Lesson 2: Greetings & Politeness (chat dialogue bubbles, audio buttons, tips)
- Lesson 3: Verbe Être (verb stem/ending highlights, conjugation audio buttons, flip cards)
- Lesson 4: Articles & Gender (gender badges, soft blue/pink cards, audio buttons)
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson
from apps.quizzes.models import Question, Choice

def upgrade_all_lessons():
    # -------------------------------------------------------------
    # 1. UPGRADE LESSON 1: Alphabet & Phonetics
    # -------------------------------------------------------------
    lesson1 = Lesson.objects.filter(data_lesson_id="lesson1").first()
    if lesson1:
        alphabet_letters = [
            ("A a", "[a]", "Avion", "самолёт", "літак", "airplane"),
            ("B b", "[be]", "Bonjour", "здравствуйте", "добрий день", "hello"),
            ("C c", "[se]", "Café", "кофе", "кава", "coffee"),
            ("D d", "[de]", "Deux", "два", "два", "two"),
            ("E e", "[ə]", "Enfant", "ребёнок", "дитина", "child"),
            ("F f", "[ɛf]", "Français", "французский", "французька", "French"),
            ("G g", "[ʒe]", "Gare", "вокзал", "вокзал", "station"),
            ("H h", "[aʃ]", "Hôtel", "отель (H немой)", "готель", "hotel"),
            ("I i", "[i]", "Ici", "здесь", "тут", "here"),
            ("J j", "[ʒi]", "Jour", "день", "день", "day"),
            ("K k", "[ka]", "Kilo", "килограмм", "кілограм", "kilogram"),
            ("L l", "[ɛl]", "Livre", "книга", "книга", "book"),
            ("M m", "[ɛm]", "Maison", "дом", "будинок", "house"),
            ("N n", "[ɛn]", "Nuit", "ночь", "ніч", "night"),
            ("O o", "[o]", "Orange", "апельсин", "апельсин", "orange"),
            ("P p", "[pe]", "Paris", "Париж", "Париж", "Paris"),
            ("Q q", "[ky]", "Quatre", "четыре", "чотири", "four"),
            ("R r", "[ɛʁ]", "Rue", "улица", "вулиця", "street"),
            ("S s", "[ɛs]", "Soleil", "солнце", "сонце", "sun"),
            ("T t", "[te]", "Train", "поезд", "поїзд", "train"),
            ("U u", "[y]", "Une", "одна", "одна", "one/a"),
            ("V v", "[ve]", "Ville", "город", "місто", "city"),
            ("W w", "[dubləve]", "Wallonie", "Валлония (Бельгия)", "Валлонія", "Wallonia"),
            ("X x", "[iks]", "Taxi", "такси", "таксі", "taxi"),
            ("Y y", "[igʁɛk]", "Yeux", "глаза", "очі", "eyes"),
            ("Z z", "[zɛd]", "Zéro", "ноль", "нуль", "zero"),
        ]

        def build_alphabet_grid(lang_idx):
            items = []
            for l, ipa, fr_word, ru_tr, uk_tr, en_tr in alphabet_letters:
                tr = [ru_tr, uk_tr, en_tr, ""][lang_idx]
                speak_target = f"{l[0]}, {fr_word}"
                items.append(
                    f'<div>'
                    f'<div style="display:flex; justify-content:space-between; align-items:center;">'
                    f'<strong>{l}</strong> <button class="audio-play-btn" data-speak="{speak_target}" title="Écouter">🔊</button>'
                    f'</div>'
                    f'<span style="font-size:0.85rem; color:var(--text-tertiary);">{ipa}</span><br>'
                    f'<span style="font-size:0.95rem; font-weight:600; color:var(--accent-blue);">{fr_word}</span> '
                    f'<span style="font-size:0.8rem; color:var(--text-secondary);">({tr})</span>'
                    f'</div>'
                )
            return '<div class="conjugation-grid" style="grid-template-columns: repeat(auto-fill, minmax(135px, 1fr)); gap: 10px;">\n' + '\n'.join(items) + '\n</div>'

        lesson1.content_html_ru = f"""
        <h2>Французский алфавит и фонетика (L'alphabet français)</h2>
        <p>Во французском алфавите <strong>26 букв</strong>: 6 гласных (<em>A, E, I, O, U, Y</em>) и 20 согласных. Нажимайте на значок 🔊 рядом с любой буквой, чтобы мгновенно услышать произношение!</p>

        <h3>1. Интерактивная таблица всех 26 букв</h3>
        {build_alphabet_grid(0)}

        <div class="callout-box callout-tip">
            <div class="callout-title">💡 Главное правило французского чтения</div>
            <div class="callout-content">
                <p>Конечные согласные <strong>-d, -p, -s, -t, -x, -z</strong> на конце слов, как правило, <strong>НЕ произносятся</strong> (Lettres muettes):</p>
                <p><em>Parli<span class="silent-letter" title="s немой">s</span></em> [пари], <em>cha<span class="silent-letter" title="t немой">t</span></em> [ша], <em>beaucou<span class="silent-letter" title="p немой">p</span></em> [боку].</p>
            </div>
        </div>

        <div class="callout-box callout-rule">
            <div class="callout-title">📏 Особые звукосочетания</div>
            <div class="callout-content">
                <ul>
                    <li><strong>OU</strong> = [у]: <em>bonj<strong style="color:var(--accent-purple)">ou</strong>r</em> <button class="audio-play-btn" data-speak="bonjour">🔊</button></li>
                    <li><strong>OI</strong> = [уа]: <em>tr<strong style="color:var(--accent-purple)">oi</strong>s</em> <button class="audio-play-btn" data-speak="trois">🔊</button>, <em>m<strong style="color:var(--accent-purple)">oi</strong></em> <button class="audio-play-btn" data-speak="moi">🔊</button></li>
                    <li><strong>AU / EAU</strong> = [о]: <em><strong style="color:var(--accent-purple)">eau</strong></em> (вода) <button class="audio-play-btn" data-speak="eau">🔊</button></li>
                    <li><strong>CH</strong> = [ш]: <em><strong style="color:var(--accent-purple)">ch</strong>at</em> (кот) <button class="audio-play-btn" data-speak="chat">🔊</button></li>
                </ul>
            </div>
        </div>

        <h3>2. 🃏 Карточки для быстрой самопроверки</h3>
        <p>Нажмите на карточку, чтобы перевернуть её и узнать произношение буквы:</p>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.8rem; color:var(--accent-blue);">E</strong>
                        <span class="flip-hint">Как читается буква?</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.2rem;">[ё] / [э]</strong>
                        <span style="font-size:0.85rem;">Enfant</span>
                        <button class="audio-play-btn" data-speak="E, enfant" style="margin-top:6px;">🔊</button>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.8rem; color:var(--accent-purple);">OI</strong>
                        <span class="flip-hint">Как читается сочетание?</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.2rem;">[уа]</strong>
                        <span style="font-size:0.85rem;">Trois / Bonsoir</span>
                        <button class="audio-play-btn" data-speak="trois, bonsoir" style="margin-top:6px;">🔊</button>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.8rem; color:var(--accent-green);">OU</strong>
                        <span class="flip-hint">Как читается сочетание?</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.2rem;">[у]</strong>
                        <span style="font-size:0.85rem;">Bonjour</span>
                        <button class="audio-play-btn" data-speak="bonjour" style="margin-top:6px;">🔊</button>
                    </div>
                </div>
            </div>
        </div>
        """

        lesson1.content_html_uk = f"""
        <h2>Французький алфавіт та фонетика (L'alphabet français)</h2>
        <p>У французькому алфавіті <strong>26 літер</strong>. Натискайте на значок 🔊 біля будь-якої літери, щоб миттєво почути її вимову!</p>

        <h3>1. Інтерактивна таблиця 26 літер</h3>
        {build_alphabet_grid(1)}

        <div class="callout-box callout-tip">
            <div class="callout-title">💡 Головне правило читання</div>
            <div class="callout-content">
                <p>Кінцеві приголосні <strong>-d, -p, -s, -t, -x, -z</strong> на кінці слів зазвичай <strong>НЕ читаються</strong> (Lettres muettes):</p>
                <p><em>Pari<span class="silent-letter">s</span></em> [парі], <em>cha<span class="silent-letter">t</span></em> [ша], <em>beaucou<span class="silent-letter">p</span></em> [боку].</p>
            </div>
        </div>
        """
        lesson1.save()
        print("Upgraded Lesson 1 (Alphabet)!")

    # -------------------------------------------------------------
    # 2. UPGRADE LESSON-BE: Belgian French
    # -------------------------------------------------------------
    lesson_be = Lesson.objects.filter(data_lesson_id="lesson-be").first()
    if lesson_be:
        lesson_be.content_html_ru = """
        <h2>Французский в Бельгии: практический гид</h2>
        <p>Бельгийский французский более логичен и дружелюбен! Нажимайте 🔊 для прослушивания произношения бельгийских выражений.</p>

        <div class="callout-box callout-belgium">
            <div class="callout-title">🇧🇪 1. Главные числа: 70 и 90 без французских уравнений</div>
            <div class="callout-content">
                <p>В Бельгии не говорят «60+10» (soixante-dix) или «4×20+10» (quatre-vingt-dix):</p>
                <ul style="margin-left: 20px;">
                    <li>🇧🇪 <strong>70 — Septante</strong> [септант] <button class="audio-play-btn" data-speak="septante">🔊</button></li>
                    <li>🇧🇪 <strong>90 — Nonante</strong> [нонант] <button class="audio-play-btn" data-speak="nonante">🔊</button></li>
                    <li><em>(80 остаётся quatre-vingts [катр-вэн] <button class="audio-play-btn" data-speak="quatre-vingts">🔊</button>).</em></li>
                </ul>
            </div>
        </div>

        <h3>2. Приёмы пищи (Не перепутайте!)</h3>
        <div class="conjugation-grid">
            <div><strong>🕗 Утро:</strong><br><strong style="color:var(--accent-blue)">Le déjeuner</strong> <button class="audio-play-btn" data-speak="le déjeuner">🔊</button><br>Завтрак</div>
            <div><strong>🕛 День:</strong><br><strong style="color:var(--accent-blue)">Le dîner</strong> <button class="audio-play-btn" data-speak="le dîner">🔊</button><br>Обед</div>
            <div><strong>🕕 Вечер:</strong><br><strong style="color:var(--accent-blue)">Le souper</strong> <button class="audio-play-btn" data-speak="le souper">🔊</button><br>Ужин</div>
        </div>

        <div class="callout-box callout-warning">
            <div class="callout-title">⚠️ Осторожно: разница с Францией</div>
            <div class="callout-content">
                <p>Во Франции <em>déjeuner</em> — это обед, а <em>dîner</em> — ужин. В Бельгии, если коллега зовет вас на <strong>déjeuner</strong>, это приглашение на утренний кофе с круассаном!</p>
            </div>
        </div>

        <h3>3. 🗣️ Живой диалог в магазине в Бельгии</h3>
        <div class="dialogue-container">
            <div class="dialogue-msg speaker-a">
                <div class="dialogue-avatar">🛒</div>
                <div class="dialogue-bubble">
                    <div class="dialogue-speaker-name">Покупатель</div>
                    <div class="dialogue-french">
                        Bonjour ! Deux pistolets, s'il vous plaît.
                        <button class="audio-play-btn" data-speak="Bonjour ! Deux pistolets, s'il vous plaît.">🔊</button>
                    </div>
                    <div class="dialogue-trans">Здравствуйте! Две булочки, пожалуйста.</div>
                </div>
            </div>

            <div class="dialogue-msg speaker-b">
                <div class="dialogue-avatar">🥖</div>
                <div class="dialogue-bubble">
                    <div class="dialogue-speaker-name">Продавец (Бельгиец)</div>
                    <div class="dialogue-french">
                        Voilà ! S'il vous plaît ! Ça fait septante centimes.
                        <button class="audio-play-btn" data-speak="Voilà ! S'il vous plaît ! Ça fait septante centimes.">🔊</button>
                    </div>
                    <div class="dialogue-trans">Вот, держите! С вас 70 сантимов.</div>
                </div>
            </div>

            <div class="dialogue-msg speaker-a">
                <div class="dialogue-avatar">🛒</div>
                <div class="dialogue-bubble">
                    <div class="dialogue-speaker-name">Покупатель</div>
                    <div class="dialogue-french">
                        Merci beaucoup, bonne journée !
                        <button class="audio-play-btn" data-speak="Merci beaucoup, bonne journée !">🔊</button>
                    </div>
                    <div class="dialogue-trans">Большое спасибо, хорошего дня!</div>
                </div>
            </div>
        </div>

        <div class="callout-box callout-tip">
            <div class="callout-title">💡 «S'il vous plaît» при передаче сдачи или чека</div>
            <div class="callout-content">
                <p>В Бельгии, когда вам что-то передают в руки (сдачу, чек, посылку), говорят <strong>«S'il vous plaît !»</strong> в значении <em>«Держите / пожалуйста»</em>. Отвечайте: <strong>«Merci !»</strong>.</p>
            </div>
        </div>
        """
        lesson_be.save()
        print("Upgraded Lesson-BE (Belgian specifics)!")

    # -------------------------------------------------------------
    # 3. UPGRADE LESSON 2: Greetings & Politeness
    # -------------------------------------------------------------
    lesson2 = Lesson.objects.filter(data_lesson_id="lesson2").first()
    if lesson2:
        lesson2.content_html_ru = """
        <h2>Приветствия и формулы вежливости (Salutations)</h2>
        <p>Первые слова, которые вы будете слышать каждый день на улице, в магазине и транспорте. Нажимайте 🔊 для прослушивания произношения.</p>

        <h3>1. Базовые приветствия</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px;">
            <div><strong>Bonjour</strong> [бонжур] <button class="audio-play-btn" data-speak="Bonjour">🔊</button><br><span style="color:var(--text-secondary);">Здравствуйте / Добрый день</span></div>
            <div><strong>Bonsoir</strong> [бонсуар] <button class="audio-play-btn" data-speak="Bonsoir">🔊</button><br><span style="color:var(--text-secondary);">Добрый вечер (после 17:00)</span></div>
            <div><strong>Salut</strong> [салю] <button class="audio-play-btn" data-speak="Salut">🔊</button><br><span style="color:var(--text-secondary);">Привет / Пока (друзьям)</span></div>
            <div><strong>Au revoir</strong> [о ревуар] <button class="audio-play-btn" data-speak="Au revoir">🔊</button><br><span style="color:var(--text-secondary);">До свидания</span></div>
            <div><strong>À bientôt</strong> [а бьянто] <button class="audio-play-btn" data-speak="À bientôt">🔊</button><br><span style="color:var(--text-secondary);">До скорого</span></div>
            <div><strong>Bonne journée</strong> [бон журне] <button class="audio-play-btn" data-speak="Bonne journée">🔊</button><br><span style="color:var(--text-secondary);">Хорошего дня!</span></div>
        </div>

        <h3>2. 🗣️ Диалог: Как дела? (Comment ça va ?)</h3>
        <div class="dialogue-container">
            <div class="dialogue-msg speaker-a">
                <div class="dialogue-avatar">👨</div>
                <div class="dialogue-bubble">
                    <div class="dialogue-speaker-name">Марк</div>
                    <div class="dialogue-french">
                        Bonjour Sophie ! Comment vas-tu ?
                        <button class="audio-play-btn" data-speak="Bonjour Sophie ! Comment vas-tu ?">🔊</button>
                    </div>
                    <div class="dialogue-trans">Привет, Софи! Как твои дела?</div>
                </div>
            </div>

            <div class="dialogue-msg speaker-b">
                <div class="dialogue-avatar">👩</div>
                <div class="dialogue-bubble">
                    <div class="dialogue-speaker-name">Софи</div>
                    <div class="dialogue-french">
                        Ça va très bien, merci ! Et toi ?
                        <button class="audio-play-btn" data-speak="Ça va très bien, merci ! Et toi ?">🔊</button>
                    </div>
                    <div class="dialogue-trans">Всё отлично, спасибо! А у тебя?</div>
                </div>
            </div>
        </div>

        <div class="callout-box callout-tip">
            <div class="callout-title">💡 Универсальное «Ça va»</div>
            <div class="callout-content">
                <p>Французское <strong>Ça va ?</strong> [са ва] — это и вопрос, и ответ:</p>
                <p>— <em>Ça va ?</em> (Как дела?) <button class="audio-play-btn" data-speak="Ça va ?">🔊</button><br>— <em>Oui, ça va !</em> (Да, всё хорошо!) <button class="audio-play-btn" data-speak="Oui, ça va !">🔊</button></p>
            </div>
        </div>
        """
        lesson2.save()
        print("Upgraded Lesson 2 (Greetings)!")

    # -------------------------------------------------------------
    # 4. UPGRADE LESSON 4: Articles & Gender
    # -------------------------------------------------------------
    lesson4 = Lesson.objects.filter(data_lesson_id="lesson4").first()
    if lesson4:
        lesson4.content_html_ru = """
        <h2>Артикли и грамматический род (Articles et Genre)</h2>
        <p>Во французском языке каждое существительное имеет род: <strong>мужской (Masculin)</strong> или <strong>женский (Féminin)</strong>. Среднего рода нет.</p>

        <h3>1. Неопределенные артикли (Un / Une / Des)</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div class="gender-m">
                <strong>🔵 Мужской род: <span style="color:#2563EB; font-size:1.2rem;">UN</span></strong> <span class="gender-badge m">m</span>
                <p style="margin-top:6px;"><em>Un livre</em> (книга) <button class="audio-play-btn" data-speak="Un livre">🔊</button></p>
                <p><em>Un café</em> (кофе) <button class="audio-play-btn" data-speak="Un café">🔊</button></p>
            </div>
            <div class="gender-f">
                <strong>🔴 Женский род: <span style="color:#E11D48; font-size:1.2rem;">UNE</span></strong> <span class="gender-badge f">f</span>
                <p style="margin-top:6px;"><em>Une pomme</em> (яблоко) <button class="audio-play-btn" data-speak="Une pomme">🔊</button></p>
                <p><em>Une maison</em> (дом) <button class="audio-play-btn" data-speak="Une maison">🔊</button></p>
            </div>
        </div>

        <h3>2. Определенные артикли (Le / La / L' / Les)</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
            <div><strong style="color:var(--accent-blue)">LE</strong> <span class="gender-badge m">m</span> — <em>Le garçon</em> (мальчик) <button class="audio-play-btn" data-speak="Le garçon">🔊</button></div>
            <div><strong style="color:#E11D48">LA</strong> <span class="gender-badge f">f</span> — <em>La fille</em> (девочка) <button class="audio-play-btn" data-speak="La fille">🔊</button></div>
            <div><strong style="color:var(--accent-purple)">L'</strong> <em>(перед гласной)</em> — <em>L'ami</em> (друг) <button class="audio-play-btn" data-speak="L'ami">🔊</button></div>
            <div><strong style="color:var(--accent-green)">LES</strong> <em>(множественное)</em> — <em>Les enfants</em> (дети) <button class="audio-play-btn" data-speak="Les enfants">🔊</button></div>
        </div>

        <div class="callout-box callout-rule">
            <div class="callout-title">📏 Правило усечения артикля (L')</div>
            <div class="callout-content">
                <p>Перед словами, начинающимися с гласной или немой <strong>H</strong>, артикли <em>le</em> и <em>la</em> превращаются в <strong>l'</strong>:</p>
                <p><em>L'hôtel</em> <button class="audio-play-btn" data-speak="L'hôtel">🔊</button>, <em>L'école</em> <button class="audio-play-btn" data-speak="L'école">🔊</button>, <em>L'eau</em> <button class="audio-play-btn" data-speak="L'eau">🔊</button>.</p>
            </div>
        </div>
        """
        lesson4.save()
        print("Upgraded Lesson 4 (Articles & Gender)!")

if __name__ == '__main__':
    upgrade_all_lessons()
