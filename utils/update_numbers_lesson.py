"""
Script to update the Numbers lesson with complete numbers from 0 to 100, pronunciation, and Belgian usage.
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
    <p>Счёт во французском языке начинается с базовых чисел от 0 до 10, которые используются везде: от цен в магазине до номеров телефонов.</p>

    <h3>1. Базовые числа от 0 до 10</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>0</strong> — <strong>Zéro</strong> [зеро]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>1</strong> — <strong>Un / Une</strong> [эн / юн]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>2</strong> — <strong>Deux</strong> [дё]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>3</strong> — <strong>Trois</strong> [труа]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>4</strong> — <strong>Quatre</strong> [катр]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>5</strong> — <strong>Cinq</strong> [сэнк]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>6</strong> — <strong>Six</strong> [сис]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>7</strong> — <strong>Sept</strong> [сэт] <em>(p немой)</em></div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>8</strong> — <strong>Huit</strong> [юит]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>9</strong> — <strong>Neuf</strong> [нёф]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>10</strong> — <strong>Dix</strong> [дис]</div>
    </div>

    <h3>2. Числа от 11 до 20</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>11</strong> — <strong>Onze</strong> [онз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>12</strong> — <strong>Douze</strong> [дуз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>13</strong> — <strong>Treize</strong> [трэз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>14</strong> — <strong>Quatorze</strong> [каторз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>15</strong> — <strong>Quinze</strong> [канз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>16</strong> — <strong>Seize</strong> [сэз]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>17</strong> — <strong>Dix-sept</strong> [дис-сэт]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>18</strong> — <strong>Dix-huit</strong> [диз-юит]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>19</strong> — <strong>Dix-neuf</strong> [диз-нёф]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>20</strong> — <strong>Vingt</strong> [вэн]</div>
    </div>

    <h3>3. Десятки (20–60)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div><strong>20</strong> — Vingt [вэн]</div>
        <div><strong>30</strong> — Trente [трант]</div>
        <div><strong>40</strong> — Quarante [карант]</div>
        <div><strong>50</strong> — Cinquante [сэнкант]</div>
        <div><strong>60</strong> — Soixante [суасант]</div>
    </div>
    <div class="example-box">
        <p><strong>Образование составных чисел:</strong></p>
        <p>Когда прибавляем 1: используется союз <em>et</em> (и): <em>21 = Vingt <strong>et</strong> un</em>, <em>31 = Trente <strong>et</strong> un</em>.</p>
        <p>Для остальных цифр — через дефис: <em>22 = Vingt-deux</em>, <em>35 = Trente-cinq</em>, <em>48 = Quarante-huit</em>.</p>
    </div>

    <h3>4. 🇧🇪 В Бельгии (70, 80, 90, 100)</h3>
    <p>В Бельгии числа 70 и 90 произносятся просто и прямо, без сложных подсчетов:</p>
    <div class="example-box">
        <p>🇧🇪 <strong>70 = Septante</strong> [септант] (71 = <em>septante et un</em>, 75 = <em>septante-cinq</em>)</p>
        <p>🇧🇪 <strong>80 = Quatre-vingts</strong> [катр-вэн] (81 = <em>quatre-vingt-un</em>, 85 = <em>quatre-vingt-cinq</em>)</p>
        <p>🇧🇪 <strong>90 = Nonante</strong> [нонант] (91 = <em>nonante et un</em>, 99 = <em>nonante-neuf</em>)</p>
        <p><strong>100 = Cent</strong> [сан] (200 = <em>deux cents</em>)</p>
    </div>

    <div class="example-box warning">
        <strong>Сравнение с Францией:</strong>
        <p>Во Франции говорят: 70 = <em>soixante-dix</em> (60+10), 90 = <em>quatre-vingt-dix</em> (4×20+10). Но в бельгийских супермаркетах, банках и коммунах вы всегда услышите <strong>Septante</strong> и <strong>Nonante</strong>!</p>
    </div>
    """

    lesson.content_html_uk = """
    <h2>Французькі числа: від 0 до 100</h2>
    <p>Рахунок французькою починається з базових чисел від 0 до 10, які знадобляться щодня.</p>

    <h3>1. Базові числа від 0 до 10</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>0</strong> — <strong>Zéro</strong> [зеро]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>1</strong> — <strong>Un / Une</strong> [ен / юн]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>2</strong> — <strong>Deux</strong> [де]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>3</strong> — <strong>Trois</strong> [труа]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>4</strong> — <strong>Quatre</strong> [катр]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>5</strong> — <strong>Cinq</strong> [сенк]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>6</strong> — <strong>Six</strong> [сіс]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>7</strong> — <strong>Sept</strong> [сет]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>8</strong> — <strong>Huit</strong> [юіт]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>9</strong> — <strong>Neuf</strong> [неф]</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>10</strong> — <strong>Dix</strong> [діс]</div>
    </div>

    <h3>2. Числа від 11 до 20</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div><strong>11</strong> — Onze</div>
        <div><strong>12</strong> — Douze</div>
        <div><strong>13</strong> — Treize</div>
        <div><strong>14</strong> — Quatorze</div>
        <div><strong>15</strong> — Quinze</div>
        <div><strong>16</strong> — Seize</div>
        <div><strong>17</strong> — Dix-sept</div>
        <div><strong>18</strong> — Dix-huit</div>
        <div><strong>19</strong> — Dix-neuf</div>
        <div><strong>20</strong> — Vingt</div>
    </div>

    <h3>3. Десятки (20–60)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
        <div><strong>20</strong> — Vingt</div>
        <div><strong>30</strong> — Trente</div>
        <div><strong>40</strong> — Quarante</div>
        <div><strong>50</strong> — Cinquante</div>
        <div><strong>60</strong> — Soixante</div>
    </div>

    <h3>4. 🇧🇪 У Бельгії (70, 80, 90, 100)</h3>
    <div class="example-box">
        <p>🇧🇪 <strong>70 = Septante</strong> [септант]</p>
        <p>🇧🇪 <strong>80 = Quatre-vingts</strong> [катр-вен]</p>
        <p>🇧🇪 <strong>90 = Nonante</strong> [нонант]</p>
        <p><strong>100 = Cent</strong> [сан]</p>
    </div>
    """

    lesson.content_html_en = """
    <h2>French Numbers: 0 to 100</h2>
    <h3>1. Basic Numbers 0 to 10:</h3>
    <p>0 (Zéro), 1 (Un/Une), 2 (Deux), 3 (Trois), 4 (Quatre), 5 (Cinq), 6 (Six), 7 (Sept), 8 (Huit), 9 (Neuf), 10 (Dix).</p>
    <h3>2. Numbers 11 to 20:</h3>
    <p>11 (Onze), 12 (Douze), 13 (Treize), 14 (Quatorze), 15 (Quinze), 16 (Seize), 17 (Dix-sept), 18 (Dix-huit), 19 (Dix-neuf), 20 (Vingt).</p>
    <h3>3. Tens:</h3>
    <p>20 (Vingt), 30 (Trente), 40 (Quarante), 50 (Cinquante), 60 (Soixante).</p>
    <h3>4. 🇧🇪 In Belgium:</h3>
    <p>70 = <strong>Septante</strong>, 80 = <strong>Quatre-vingts</strong>, 90 = <strong>Nonante</strong>, 100 = <strong>Cent</strong>.</p>
    """

    lesson.content_html_fr = """
    <h2>Les nombres de 0 à 100</h2>
    <h3>De 0 à 10 :</h3>
    <p>0 (Zéro), 1 (Un), 2 (Deux), 3 (Trois), 4 (Quatre), 5 (Cinq), 6 (Six), 7 (Sept), 8 (Huit), 9 (Neuf), 10 (Dix).</p>
    <h3>De 11 à 20 :</h3>
    <p>11 (Onze), 12 (Douze), 13 (Treize), 14 (Quatorze), 15 (Quinze), 16 (Seize), 17 (Dix-sept), 18 (Dix-huit), 19 (Dix-neuf), 20 (Vingt).</p>
    <h3>🇧🇪 En Belgique :</h3>
    <p>70 = Septante, 80 = Quatre-vingts, 90 = Nonante, 100 = Cent.</p>
    """

    lesson.save()
    print("Lesson numbers updated successfully with complete 0-100 guide!")

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
