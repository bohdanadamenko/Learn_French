"""
Script to update the Numbers lesson with complete numbers from 0 to 100, audio TTS, pronunciation, and Belgian usage.
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

def update_numbers_lesson():
    lesson = Lesson.objects.filter(data_lesson_id="lesson-numbers-100").first()
    if not lesson:
        print("Lesson lesson-numbers-100 not found!")
        return

    lesson.title_ru = "🔢 Числа от 0 до 100 (Французские и бельгийские)"
    lesson.title_uk = "🔢 Числа від 0 до 100 (Французькі та бельгійські)"
    lesson.title_en = "🔢 Numbers from 0 to 100 (French & Belgian)"
    lesson.title_fr = "🔢 Les nombres de 0 à 100"

    lesson.content_html_ru = """
    <h2>Французские числа: от 0 до 100</h2>
    <p>Счёт во французском языке начинается с базовых чисел от 0 до 10. Нажимайте на значок 🔊 рядом с любым словом, чтобы услышать правильное французское произношение.</p>

    <h3>1. Базовые числа от 0 до 10</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>0</strong> — <strong>Zéro</strong> [зеро] <button class="audio-play-btn" data-speak="zéro" title="Прослушать">🔊</button></div>
        <div><strong>1</strong> — <strong>Un <span class="gender-badge m">m</span> / Une <span class="gender-badge f">f</span></strong> [эн / юн] <button class="audio-play-btn" data-speak="un, une" title="Прослушать">🔊</button></div>
        <div><strong>2</strong> — <strong>Deux</strong> [дё] <button class="audio-play-btn" data-speak="deux" title="Прослушать">🔊</button></div>
        <div><strong>3</strong> — <strong>Trois</strong> [труа] <button class="audio-play-btn" data-speak="trois" title="Прослушать">🔊</button></div>
        <div><strong>4</strong> — <strong>Quatre</strong> [катр] <button class="audio-play-btn" data-speak="quatre" title="Прослушать">🔊</button></div>
        <div><strong>5</strong> — <strong>Cinq</strong> [сэнк] <button class="audio-play-btn" data-speak="cinq" title="Прослушать">🔊</button></div>
        <div><strong>6</strong> — <strong>Six</strong> [сис] <button class="audio-play-btn" data-speak="six" title="Прослушать">🔊</button></div>
        <div><strong>7</strong> — <strong>Sep<span class="silent-letter" title="p — немой">t</span></strong> [сэт] <button class="audio-play-btn" data-speak="sept" title="Прослушать">🔊</button></div>
        <div><strong>8</strong> — <strong>Huit</strong> [юит] <button class="audio-play-btn" data-speak="huit" title="Прослушать">🔊</button></div>
        <div><strong>9</strong> — <strong>Neuf</strong> [нёф] <button class="audio-play-btn" data-speak="neuf" title="Прослушать">🔊</button></div>
        <div><strong>10</strong> — <strong>Dix</strong> [дис] <button class="audio-play-btn" data-speak="dix" title="Прослушать">🔊</button></div>
    </div>

    <h3>2. Числа от 11 до 20</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>11</strong> — <strong>Onze</strong> [онз] <button class="audio-play-btn" data-speak="onze">🔊</button></div>
        <div><strong>12</strong> — <strong>Douze</strong> [дуз] <button class="audio-play-btn" data-speak="douze">🔊</button></div>
        <div><strong>13</strong> — <strong>Treize</strong> [трэз] <button class="audio-play-btn" data-speak="treize">🔊</button></div>
        <div><strong>14</strong> — <strong>Quatorze</strong> [каторз] <button class="audio-play-btn" data-speak="quatorze">🔊</button></div>
        <div><strong>15</strong> — <strong>Quinze</strong> [канз] <button class="audio-play-btn" data-speak="quinze">🔊</button></div>
        <div><strong>16</strong> — <strong>Seize</strong> [сэз] <button class="audio-play-btn" data-speak="seize">🔊</button></div>
        <div><strong>17</strong> — <strong>Dix-sept</strong> [дис-сэт] <button class="audio-play-btn" data-speak="dix-sept">🔊</button></div>
        <div><strong>18</strong> — <strong>Dix-huit</strong> [диз-юит] <button class="audio-play-btn" data-speak="dix-huit">🔊</button></div>
        <div><strong>19</strong> — <strong>Dix-neuf</strong> [диз-нёф] <button class="audio-play-btn" data-speak="dix-neuf">🔊</button></div>
        <div><strong>20</strong> — <strong>Vin<span class="silent-letter" title="gt — немые">gt</span></strong> [вэн] <button class="audio-play-btn" data-speak="vingt">🔊</button></div>
    </div>

    <h3>3. Десятки (20–60)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>20</strong> — Vingt <button class="audio-play-btn" data-speak="vingt">🔊</button></div>
        <div><strong>30</strong> — Trente <button class="audio-play-btn" data-speak="trente">🔊</button></div>
        <div><strong>40</strong> — Quarante <button class="audio-play-btn" data-speak="quarante">🔊</button></div>
        <div><strong>50</strong> — Cinquante <button class="audio-play-btn" data-speak="cinquante">🔊</button></div>
        <div><strong>60</strong> — Soixante <button class="audio-play-btn" data-speak="soixante">🔊</button></div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Правило сложения чисел</div>
        <div class="callout-content">
            <p>Когда прибавляем 1 — используем союз <strong>et</strong> (и): <em>21 = Vingt <strong style="color:var(--accent-purple)">et</strong> un</em>, <em>31 = Trente <strong style="color:var(--accent-purple)">et</strong> un</em>.</p>
            <p>Для всех остальных цифр пишется обычный дефис: <em>22 = Vingt-deux</em>, <em>35 = Trente-cinq</em>, <em>48 = Quarante-huit</em>.</p>
        </div>
    </div>

    <h3>4. 🇧🇪 В Бельгии (70, 80, 90, 100)</h3>
    <div class="callout-box callout-belgium">
        <div class="callout-title">🇧🇪 Бельгийский стандарт (без сложных подсчётов)</div>
        <div class="callout-content">
            <p>В Бельгии не используют французские формулы вроде «60+10» (soixante-dix) или «4×20+10» (quatre-vingt-dix):</p>
            <ul style="margin: 8px 0 0 20px;">
                <li>🇧🇪 <strong>70 = Septante</strong> [септант] <button class="audio-play-btn" data-speak="septante">🔊</button></li>
                <li>🇧🇪 <strong>80 = Quatre-vingts</strong> [катр-вэн] <button class="audio-play-btn" data-speak="quatre-vingts">🔊</button></li>
                <li>🇧🇪 <strong>90 = Nonante</strong> [нонант] <button class="audio-play-btn" data-speak="nonante">🔊</button></li>
                <li><strong>100 = Cent</strong> [сан] <button class="audio-play-btn" data-speak="cent">🔊</button></li>
            </ul>
        </div>
    </div>

    <h3>5. 🃏 Интерактивные карточки для самопроверки</h3>
    <p>Нажмите на карточку, чтобы перевернуть её и проверить себя:</p>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.6rem">70</strong>
                    <span class="flip-hint">Нажмите для ответа</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem; color:var(--accent-blue);">Septante</strong>
                    <span style="font-size:0.85rem">[септант] 🇧🇪</span>
                    <button class="audio-play-btn" data-speak="septante" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.6rem">90</strong>
                    <span class="flip-hint">Нажмите для ответа</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem; color:var(--accent-blue);">Nonante</strong>
                    <span style="font-size:0.85rem">[нонант] 🇧🇪</span>
                    <button class="audio-play-btn" data-speak="nonante" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.6rem">100</strong>
                    <span class="flip-hint">Нажмите для ответа</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem; color:var(--accent-purple);">Cent</strong>
                    <span style="font-size:0.85rem">[сан]</span>
                    <button class="audio-play-btn" data-speak="cent" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
    </div>
    """

    lesson.content_html_uk = """
    <h2>Французькі числа: від 0 до 100</h2>
    <p>Рахунок французькою мовою починається з базових чисел від 0 до 10. Натискайте на значок 🔊 біля будь-якого слова, щоб почути правильну французьку вимову.</p>

    <h3>1. Базові числа від 0 до 10</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>0</strong> — <strong>Zéro</strong> [зеро] <button class="audio-play-btn" data-speak="zéro">🔊</button></div>
        <div><strong>1</strong> — <strong>Un <span class="gender-badge m">m</span> / Une <span class="gender-badge f">f</span></strong> [ен / юн] <button class="audio-play-btn" data-speak="un, une">🔊</button></div>
        <div><strong>2</strong> — <strong>Deux</strong> [де] <button class="audio-play-btn" data-speak="deux">🔊</button></div>
        <div><strong>3</strong> — <strong>Trois</strong> [труа] <button class="audio-play-btn" data-speak="trois">🔊</button></div>
        <div><strong>4</strong> — <strong>Quatre</strong> [катр] <button class="audio-play-btn" data-speak="quatre">🔊</button></div>
        <div><strong>5</strong> — <strong>Cinq</strong> [сенк] <button class="audio-play-btn" data-speak="cinq">🔊</button></div>
        <div><strong>6</strong> — <strong>Six</strong> [сіс] <button class="audio-play-btn" data-speak="six">🔊</button></div>
        <div><strong>7</strong> — <strong>Sep<span class="silent-letter">t</span></strong> [сет] <button class="audio-play-btn" data-speak="sept">🔊</button></div>
        <div><strong>8</strong> — <strong>Huit</strong> [юіт] <button class="audio-play-btn" data-speak="huit">🔊</button></div>
        <div><strong>9</strong> — <strong>Neuf</strong> [неф] <button class="audio-play-btn" data-speak="neuf">🔊</button></div>
        <div><strong>10</strong> — <strong>Dix</strong> [діс] <button class="audio-play-btn" data-speak="dix">🔊</button></div>
    </div>

    <h3>2. Числа від 11 до 20</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>11</strong> — Onze <button class="audio-play-btn" data-speak="onze">🔊</button></div>
        <div><strong>12</strong> — Douze <button class="audio-play-btn" data-speak="douze">🔊</button></div>
        <div><strong>13</strong> — Treize <button class="audio-play-btn" data-speak="treize">🔊</button></div>
        <div><strong>14</strong> — Quatorze <button class="audio-play-btn" data-speak="quatorze">🔊</button></div>
        <div><strong>15</strong> — Quinze <button class="audio-play-btn" data-speak="quinze">🔊</button></div>
        <div><strong>16</strong> — Seize <button class="audio-play-btn" data-speak="seize">🔊</button></div>
        <div><strong>17</strong> — Dix-sept <button class="audio-play-btn" data-speak="dix-sept">🔊</button></div>
        <div><strong>18</strong> — Dix-huit <button class="audio-play-btn" data-speak="dix-huit">🔊</button></div>
        <div><strong>19</strong> — Dix-neuf <button class="audio-play-btn" data-speak="dix-neuf">🔊</button></div>
        <div><strong>20</strong> — Vingt <button class="audio-play-btn" data-speak="vingt">🔊</button></div>
    </div>

    <h3>3. Десятки (20–60)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>20</strong> — Vingt <button class="audio-play-btn" data-speak="vingt">🔊</button></div>
        <div><strong>30</strong> — Trente <button class="audio-play-btn" data-speak="trente">🔊</button></div>
        <div><strong>40</strong> — Quarante <button class="audio-play-btn" data-speak="quarante">🔊</button></div>
        <div><strong>50</strong> — Cinquante <button class="audio-play-btn" data-speak="cinquante">🔊</button></div>
        <div><strong>60</strong> — Soixante <button class="audio-play-btn" data-speak="soixante">🔊</button></div>
    </div>

    <div class="callout-box callout-belgium">
        <div class="callout-title">🇧🇪 У Бельгії (70, 80, 90, 100)</div>
        <div class="callout-content">
            <p>🇧🇪 <strong>70 = Septante</strong> [септант] <button class="audio-play-btn" data-speak="septante">🔊</button></p>
            <p>🇧🇪 <strong>80 = Quatre-vingts</strong> [катр-вен] <button class="audio-play-btn" data-speak="quatre-vingts">🔊</button></p>
            <p>🇧🇪 <strong>90 = Nonante</strong> [нонант] <button class="audio-play-btn" data-speak="nonante">🔊</button></p>
            <p><strong>100 = Cent</strong> [сан] <button class="audio-play-btn" data-speak="cent">🔊</button></p>
        </div>
    </div>
    """

    lesson.content_html_en = """
    <h2>French Numbers: 0 to 100</h2>
    <p>French counting starts with basic numbers from 0 to 10. Click the 🔊 button to listen to clear French pronunciation.</p>

    <h3>1. Basic Numbers 0 to 10</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>0</strong> — Zéro <button class="audio-play-btn" data-speak="zéro">🔊</button></div>
        <div><strong>1</strong> — Un <span class="gender-badge m">m</span> / Une <span class="gender-badge f">f</span> <button class="audio-play-btn" data-speak="un, une">🔊</button></div>
        <div><strong>2</strong> — Deux <button class="audio-play-btn" data-speak="deux">🔊</button></div>
        <div><strong>3</strong> — Trois <button class="audio-play-btn" data-speak="trois">🔊</button></div>
        <div><strong>4</strong> — Quatre <button class="audio-play-btn" data-speak="quatre">🔊</button></div>
        <div><strong>5</strong> — Cinq <button class="audio-play-btn" data-speak="cinq">🔊</button></div>
        <div><strong>6</strong> — Six <button class="audio-play-btn" data-speak="six">🔊</button></div>
        <div><strong>7</strong> — Sep<span class="silent-letter">t</span> <button class="audio-play-btn" data-speak="sept">🔊</button></div>
        <div><strong>8</strong> — Huit <button class="audio-play-btn" data-speak="huit">🔊</button></div>
        <div><strong>9</strong> — Neuf <button class="audio-play-btn" data-speak="neuf">🔊</button></div>
        <div><strong>10</strong> — Dix <button class="audio-play-btn" data-speak="dix">🔊</button></div>
    </div>

    <div class="callout-box callout-belgium">
        <div class="callout-title">🇧🇪 In Belgium (70, 80, 90, 100)</div>
        <div class="callout-content">
            <p>70 = <strong>Septante</strong> <button class="audio-play-btn" data-speak="septante">🔊</button></p>
            <p>80 = <strong>Quatre-vingts</strong> <button class="audio-play-btn" data-speak="quatre-vingts">🔊</button></p>
            <p>90 = <strong>Nonante</strong> <button class="audio-play-btn" data-speak="nonante">🔊</button></p>
            <p>100 = <strong>Cent</strong> <button class="audio-play-btn" data-speak="cent">🔊</button></p>
        </div>
    </div>
    """

    lesson.content_html_fr = """
    <h2>Les nombres de 0 à 100</h2>
    <p>Apprenez à compter en français de 0 à 100. Cliquez sur le bouton 🔊 pour écouter la prononciation.</p>

    <h3>De 0 à 10 :</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div><strong>0</strong> — Zéro <button class="audio-play-btn" data-speak="zéro">🔊</button></div>
        <div><strong>1</strong> — Un / Une <button class="audio-play-btn" data-speak="un, une">🔊</button></div>
        <div><strong>2</strong> — Deux <button class="audio-play-btn" data-speak="deux">🔊</button></div>
        <div><strong>3</strong> — Trois <button class="audio-play-btn" data-speak="trois">🔊</button></div>
        <div><strong>4</strong> — Quatre <button class="audio-play-btn" data-speak="quatre">🔊</button></div>
        <div><strong>5</strong> — Cinq <button class="audio-play-btn" data-speak="cinq">🔊</button></div>
        <div><strong>6</strong> — Six <button class="audio-play-btn" data-speak="six">🔊</button></div>
        <div><strong>7</strong> — Sept <button class="audio-play-btn" data-speak="sept">🔊</button></div>
        <div><strong>8</strong> — Huit <button class="audio-play-btn" data-speak="huit">🔊</button></div>
        <div><strong>9</strong> — Neuf <button class="audio-play-btn" data-speak="neuf">🔊</button></div>
        <div><strong>10</strong> — Dix <button class="audio-play-btn" data-speak="dix">🔊</button></div>
    </div>

    <div class="callout-box callout-belgium">
        <div class="callout-title">🇧🇪 En Belgique :</div>
        <div class="callout-content">
            <p>70 = Septante, 80 = Quatre-vingts, 90 = Nonante, 100 = Cent.</p>
        </div>
    </div>
    """

    lesson.save()
    print("Lesson numbers updated successfully with complete 0-100 guide and audio TTS!")

    # Update questions
    Question.objects.filter(lesson=lesson).delete()

    q1 = Question.objects.create(
        lesson=lesson,
        order=1,
        text="Как по-французски сказать число '3'?",
        text_ru="Как по-французски сказать число '3'?",
        text_uk="Як французькою сказати число '3'?",
        text_en="How do you say the number '3' in French?",
        text_fr="Comment dit-on le chiffre '3' en français ?"
    )
    Choice.objects.create(question=q1, text="Trois", text_ru="Trois [труа]", text_uk="Trois [труа]", text_en="Trois", text_fr="Trois", is_correct=True)
    Choice.objects.create(question=q1, text="Deux", text_ru="Deux [дё]", text_uk="Deux [де]", text_en="Deux", text_fr="Deux", is_correct=False)
    Choice.objects.create(question=q1, text="Quatre", text_ru="Quatre [катр]", text_uk="Quatre [катр]", text_en="Quatre", text_fr="Quatre", is_correct=False)

    q2 = Question.objects.create(
        lesson=lesson,
        order=2,
        text="Как в Бельгии говорят число '70'?",
        text_ru="Как в Бельгии говорят число '70'?",
        text_uk="Як у Бельгії кажуть число '70'?",
        text_en="How is '70' called in Belgium?",
        text_fr="Comment dit-on '70' en Belgique ?"
    )
    Choice.objects.create(question=q2, text="Septante", text_ru="Septante [септант]", text_uk="Septante [септант]", text_en="Septante", text_fr="Septante", is_correct=True)
    Choice.objects.create(question=q2, text="Soixante-dix", text_ru="Soixante-dix", text_uk="Soixante-dix", text_en="Soixante-dix", text_fr="Soixante-dix", is_correct=False)
    Choice.objects.create(question=q2, text="Huitante", text_ru="Huitante", text_uk="Huitante", text_en="Huitante", text_fr="Huitante", is_correct=False)

    print("Created updated questions for numbers lesson.")

if __name__ == '__main__':
    update_numbers_lesson()
