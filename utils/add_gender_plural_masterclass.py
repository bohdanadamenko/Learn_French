"""
Masterclass on Gender & Plural Formation in French:
1. Formation of Feminine (Base + e, doubling consonants -ienne/-onne, suffixes -ère/-euse/-trice/-ve)
2. How to guess gender of inanimate nouns by suffixes (-age, -ment, -eau vs -tion, -té, -ure, -ette)
3. Formation of Plural (Base + s, -s/-x/-z invariant, -al -> -aux, -eau/-eu -> -x)
4. Interactive 3D flashcards (Карточки для запоминания)
5. Comprehensive quizzes
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

def setup_gender_plural():
    t_grammar = Topic.objects.filter(id=2).first() or Topic.objects.filter(order=2).first()

    # 1. Update lesson4 to specifically focus on Gender & Plural formation rules
    l4, _ = Lesson.objects.get_or_create(data_lesson_id="lesson4", defaults={"topic": t_grammar, "order": 6})
    l4.topic = t_grammar
    l4.order = 6
    l4.title_uk = "🚻 Чоловічий і Жіночий рід та Множина: Правила утворення"
    l4.title_ru = "🚻 Мужской и Женский род и Множественное число: Правила образования"
    l4.title_en = "🚻 Gender & Plural in French: Complete Formation Rules"
    l4.title_fr = "🚻 Le masculin, le féminin et le pluriel : Règles de formation"

    l4.content_html_uk = """
    <h2>Як утворюється Чоловічий, Жіночий рід та Множина у французькій мові</h2>
    <p>У французькій мові <strong>немає середнього роду</strong> — усі іменники та прикметники є або <strong>чоловічого (Masculin)</strong>, або <strong>жіночого (Féminin)</strong> роду.</p>

    ---

    <h3>1. ♀️ Як утворити Жіночий рід (Formation du Féminin):</h3>

    <div class="callout-box callout-rule">
        <div class="callout-title">📐 Головне базове правило: Додаємо «-e» в кінці слова</div>
        <div class="callout-content">
            <p>При додаванні <strong>-e</strong> кінцева приголосна, яка раніше мовчала, <strong>починає чітко звучати</strong>:</p>
            <ul>
                <li><em>Un étudiant</em> [етюдьян] ➔ <em>Une étudiant<strong>e</strong></em> [етюдьянт] (Студент ➔ Студентка)</li>
                <li><em>Un ami</em> [амі] ➔ <em>Une ami<strong>e</strong></em> [амі] (Друг ➔ Подруга)</li>
                <li><em>Français</em> [франсе] ➔ <em>Français<strong>e</strong></em> [франсез] (Француз ➔ Француженка)</li>
                <li><em>Petit</em> [пьоті] ➔ <em>Petit<strong>e</strong></em> [пьотіт] (Маленький ➔ Маленька)</li>
            </ul>
        </div>
    </div>

    <h4>Особливі правила зміни закінчень:</h4>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue);">-ER ➔ -ÈRE</strong><br>
            <em>Un boulang<strong>er</strong></em> ➔ <em>Une boulang<strong>ère</strong></em> (Пекар)<br>
            <em>Premier</em> ➔ <em>Premi<strong>ère</strong></em> (Перший)
        </div>
        <div>
            <strong style="color:var(--accent-purple);">-IEN ➔ -IENNE</strong><br>
            <em>Un music<strong>ien</strong></em> ➔ <em>Une music<strong>ienne</strong></em><br>
            <em>Italien</em> ➔ <em>Ital<strong>ienne</strong></em>
        </div>
        <div>
            <strong style="color:var(--accent-cyan);">-EUR ➔ -EUSE</strong><br>
            <em>Un serv<strong>eur</strong></em> ➔ <em>Une serv<strong>euse</strong></em> (Офіціант)<br>
            <em>Heureux</em> ➔ <em>Heur<strong>euse</strong></em> (Щасливий)
        </div>
        <div>
            <strong style="color:var(--accent-green);">-TEUR ➔ -TRICE</strong><br>
            <em>Un dir<strong>ecteur</strong></em> ➔ <em>Une dir<strong>ectrice</strong></em><br>
            <em>Un acteur</em> ➔ <em>Une act<strong>rice</strong></em> (Актор)
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Секрет: Як за закінченням дізнатися рід неживого предмета?</div>
        <div class="callout-content">
            <p><strong>Чоловічий рід (♂️ Un / Le):</strong> слова на <em>-ment</em> (un appartement, un document), <em>-age</em> (le fromage, le voyage), <em>-eau</em> (un bureau, un château), <em>-isme</em> (le tourisme).</p>
            <p><strong>Жіночий рід (♀️ Une / La):</strong> слова на <em>-tion / -sion</em> (la station, la question), <em>-té</em> (la nationalité, la liberté), <em>-ure</em> (la voiture, la culture), <em>-ette</em> (la bicyclette).</p>
        </div>
    </div>

    ---

    <h3>2. 👥 Як утворити Множину (Formation du Pluriel):</h3>

    <div class="callout-box callout-rule">
        <div class="callout-title">📐 Головне базове правило: Додаємо «-s» в кінці (але не читаємо його!)</div>
        <div class="callout-content">
            <ul>
                <li><em>Un croissant</em> ➔ <strong>Des croissant<span style="color:var(--accent-blue)">s</span></strong> [де круасан]</li>
                <li><em>Une table</em> ➔ <strong>Des table<span style="color:var(--accent-blue)">s</span></strong> [де табль]</li>
                <li><em>La grande maison</em> ➔ <strong>Les grande<span style="color:var(--accent-blue)">s</span> maison<span style="color:var(--accent-blue)">s</span></strong></li>
            </ul>
        </div>
    </div>

    <h4>Винятки та особливі закінчення множини:</h4>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue);">Закінчення на -S, -X, -Z</strong><br>
            <span style="color:var(--text-tertiary);">Форма НЕ змінюється!</span><br>
            <em>Un pays ➔ Des pays</em> (Країни)<br>
            <em>Un prix ➔ Des prix</em> (Ціни)
        </div>
        <div>
            <strong style="color:var(--accent-purple);">-EAU, -AU, -EU ➔ додаємо -X</strong><br>
            <em>Un gâteau ➔ Des gâteau<strong>x</strong></em> (Торти)<br>
            <em>Un jeu ➔ Des jeu<strong>x</strong></em> (Ігри)
        </div>
        <div>
            <strong style="color:var(--accent-green);">-AL ➔ перетворюється на -AUX</strong><br>
            <em>Un journ<strong>al</strong> ➔ Des journ<strong>aux</strong></em> (Газети)<br>
            <em>Un animal ➔ Des anim<strong>aux</strong></em> (Тварини)
        </div>
    </div>

    ---

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-blue);">Студентка (жіночий рід)</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Une étudiante</strong>
                    <span style="font-size:0.8rem;">[юн етюдьянт]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-purple);">Газети (множина від journal)</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Des journaux</strong>
                    <span style="font-size:0.8rem;">[де журно]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-green);">Країни (множина від pays)</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Des pays</strong>
                    <span style="font-size:0.8rem;">[де пеі] (без змін)</span>
                </div>
            </div>
        </div>
    </div>
    """

    l4.content_html_ru = """
    <h2>Как образуются Мужской, Женский род и Множественное число</h2>
    <p>Во французском языке <strong>нет среднего рода</strong> — все существительные и прилагательные бывают только <strong>мужского (Masculin)</strong> или <strong>женского (Féminin)</strong> рода.</p>

    ---

    <h3>1. ♀️ Как образуется Женский род (Formation du Féminin):</h3>

    <div class="callout-box callout-rule">
        <div class="callout-title">📐 Главное базовое правило: Добавляем «-e» в конце слова</div>
        <div class="callout-content">
            <p>При добавлении <strong>-e</strong> немая согласная в конце слова <strong>начинает звучать</strong>:</p>
            <ul>
                <li><em>Un étudiant</em> [этюдьян] ➔ <em>Une étudiant<strong>e</strong></em> [этюдьянт] (Студент ➔ Студентка)</li>
                <li><em>Un ami</em> [ами] ➔ <em>Une ami<strong>e</strong></em> [ами] (Друг ➔ Подруга)</li>
                <li><em>Français</em> [франсэ] ➔ <em>Français<strong>e</strong></em> [франсэз] (Француз ➔ Француженка)</li>
                <li><em>Petit</em> [пёти] ➔ <em>Petit<strong>e</strong></em> [пётит] (Маленький ➔ Маленькая)</li>
            </ul>
        </div>
    </div>

    <h4>Особые суффиксы женского рода:</h4>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue);">-ER ➔ -ÈRE</strong><br>
            <em>Un boulang<strong>er</strong></em> ➔ <em>Une boulang<strong>ère</strong></em> (Пекарь)<br>
            <em>Premier</em> ➔ <em>Premi<strong>ère</strong></em> (Первый)
        </div>
        <div>
            <strong style="color:var(--accent-purple);">-IEN ➔ -IENNE</strong><br>
            <em>Un music<strong>ien</strong></em> ➔ <em>Une music<strong>ienne</strong></em><br>
            <em>Italien</em> ➔ <em>Ital<strong>ienne</strong></em>
        </div>
        <div>
            <strong style="color:var(--accent-cyan);">-EUR ➔ -EUSE</strong><br>
            <em>Un serv<strong>eur</strong></em> ➔ <em>Une serv<strong>euse</strong></em> (Официант)<br>
            <em>Heureux</em> ➔ <em>Heur<strong>euse</strong></em> (Счастливый)
        </div>
        <div>
            <strong style="color:var(--accent-green);">-TEUR ➔ -TRICE</strong><br>
            <em>Un dir<strong>ecteur</strong></em> ➔ <em>Une dir<strong>ectrice</strong></em><br>
            <em>Un acteur</em> ➔ <em>Une act<strong>rice</strong></em> (Актёр)
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Секрет: Как по суффиксу определить род предмета?</div>
        <div class="callout-content">
            <p><strong>Мужской род (♂️ Un / Le):</strong> слова на <em>-ment</em> (un appartement), <em>-age</em> (le fromage, le voyage), <em>-eau</em> (un bureau), <em>-isme</em> (le tourisme).</p>
            <p><strong>Женский род (♀️ Une / La):</strong> слова на <em>-tion / -sion</em> (la station, la question), <em>-té</em> (la nationalité, la liberté), <em>-ure</em> (la voiture), <em>-ette</em> (la bicyclette).</p>
        </div>
    </div>

    ---

    <h3>2. 👥 Как образуется Множественное число (Formation du Pluriel):</h3>

    <div class="callout-box callout-rule">
        <div class="callout-title">📐 Главное базовое правило: Добавляем «-s» на конце (но не произносим его!)</div>
        <div class="callout-content">
            <ul>
                <li><em>Un croissant</em> ➔ <strong>Des croissant<span style="color:var(--accent-blue)">s</span></strong> [дэ круассан]</li>
                <li><em>Une table</em> ➔ <strong>Des table<span style="color:var(--accent-blue)">s</span></strong> [дэ табль]</li>
            </ul>
        </div>
    </div>

    <h4>Исключения множественного числа:</h4>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue);">Слова на -S, -X, -Z</strong><br>
            <span style="color:var(--text-tertiary);">Форма НЕ меняется!</span><br>
            <em>Un pays ➔ Des pays</em> (Страны)<br>
            <em>Un prix ➔ Des prix</em> (Цены)
        </div>
        <div>
            <strong style="color:var(--accent-purple);">-EAU, -AU, -EU ➔ добавляем -X</strong><br>
            <em>Un gâteau ➔ Des gâteau<strong>x</strong></em> (Торты)<br>
            <em>Un bureau ➔ Des bureau<strong>x</strong></em> (Офисы)
        </div>
        <div>
            <strong style="color:var(--accent-green);">-AL ➔ переходит в -AUX</strong><br>
            <em>Un journ<strong>al</strong> ➔ Des journ<strong>aux</strong></em> (Газеты)<br>
            <em>Un animal ➔ Des anim<strong>aux</strong></em> (Животные)
        </div>
    </div>

    ---

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-blue);">Студентка (женский род)</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Une étudiante</strong>
                    <span style="font-size:0.8rem;">[юн этюдьянт]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-purple);">Газеты (множ. число от journal)</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Des journaux</strong>
                    <span style="font-size:0.8rem;">[дэ журно]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-green);">Страны (множ. число от pays)</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Des pays</strong>
                    <span style="font-size:0.8rem;">[дэ пэи] (без изменений)</span>
                </div>
            </div>
        </div>
    </div>
    """
    l4.content_html_en = "<p>Formation of Masculine, Feminine and Plural in French.</p>"
    l4.content_html_fr = "<p>Formation du masculin, féminin et pluriel en français.</p>"
    l4.save()

    # Create detailed quiz questions
    Question.objects.filter(lesson=l4).delete()

    q1 = Question.objects.create(
        lesson=l4,
        order=1,
        text="Как правильно образовать женский род от 'Un musicien'?",
        text_ru="Как правильно образовать женский род от 'Un musicien'?",
        text_uk="Як правильно утворити жіночий рід від 'Un musicien'?",
        text_en="What is the feminine form of 'Un musicien'?",
        text_fr="Quelle est la forme féminine de 'Un musicien' ?"
    )
    Choice.objects.create(question=q1, text="Une musicienne", text_ru="Une musicienne (-ien переходит в -ienne)", text_uk="Une musicienne (-ien переходить у -ienne)", text_en="Une musicienne", text_fr="Une musicienne", is_correct=True)
    Choice.objects.create(question=q1, text="Une musicieuse", text_ru="Une musicieuse (ошибка)", text_uk="Une musicieuse (помилка)", text_en="Une musicieuse", text_fr="Une musicieuse", is_correct=False)
    Choice.objects.create(question=q1, text="Une musicient", text_ru="Une musicient (ошибка)", text_uk="Une musicient", text_en="Une musicient", text_fr="Une musicient", is_correct=False)

    q2 = Question.objects.create(
        lesson=l4,
        order=2,
        text="Какое окончание во множественном числе принимает слово 'Un journal'?",
        text_ru="Какое окончание во множественном числе принимает слово 'Un journal'?",
        text_uk="Яку форму у множині має слово 'Un journal'?",
        text_en="What is the plural of 'Un journal'?",
        text_fr="Quel est le pluriel de 'Un journal' ?"
    )
    Choice.objects.create(question=q2, text="Des journaux", text_ru="Des journaux (-al переходит в -aux)", text_uk="Des journaux (-al переходить в -aux)", text_en="Des journaux", text_fr="Des journaux", is_correct=True)
    Choice.objects.create(question=q2, text="Des journals", text_ru="Des journals (ошибка)", text_uk="Des journals (помилка)", text_en="Des journals", text_fr="Des journals", is_correct=False)

    q3 = Question.objects.create(
        lesson=l4,
        order=3,
        text="Как меняется во множественном числе слово 'Un pays' (страна)?",
        text_ru="Как меняется во множественном числе слово 'Un pays' (страна)?",
        text_uk="Як змінюється у множині слово 'Un pays' (країна)?",
        text_en="What is the plural of 'Un pays'?",
        text_fr="Quel est le pluriel de 'Un pays' ?"
    )
    Choice.objects.create(question=q3, text="Des pays (не меняется)", text_ru="Des pays (не меняется, т.к. уже оканчивается на -s)", text_uk="Des pays (не змінюється, бо закінчується на -s)", text_en="Des pays", text_fr="Des pays", is_correct=True)
    Choice.objects.create(question=q3, text="Des payses", text_ru="Des payses (ошибка)", text_uk="Des payses (помилка)", text_en="Des payses", text_fr="Des payses", is_correct=False)

    print("Successfully enriched and created comprehensive Gender & Plural rules in Lesson 4!")

if __name__ == '__main__':
    setup_gender_plural()
