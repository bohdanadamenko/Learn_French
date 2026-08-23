"""
Script to expand Lesson 1 with a full French Alphabet table, pronunciation, accents, and reading rules.
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

def update_alphabet_lesson():
    lesson = Lesson.objects.filter(data_lesson_id="lesson1").first()
    if not lesson:
        print("Lesson 1 not found!")
        return

    lesson.title_ru = "📚 Французский алфавит и правила чтения"
    lesson.title_uk = "📚 Французький алфавіт та правила читання"
    lesson.title_en = "📚 French Alphabet & Reading Rules"
    lesson.title_fr = "📚 L'alphabet français et la phonétique"

    lesson.content_html_ru = """
    <h2>Французский алфавит (L'alphabet français)</h2>
    <p>Во французском алфавите <strong>26 букв</strong> латинского алфавита: 6 гласных (<em>A, E, I, O, U, Y</em>) и 20 согласных.</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>A a</strong> [а]<br><em>Avion</em> (самолёт)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>B b</strong> [бэ]<br><em>Bonjour</em> (здравствуйте)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>C c</strong> [сэ]<br><em>Café</em> (кофе)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>D d</strong> [дэ]<br><em>Deux</em> (два)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>E e</strong> [ё / э]<br><em>Eau</em> (вода)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>F f</strong> [эф]<br><em>Frite</em> (картофель фри)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>G g</strong> [жэ]<br><em>Gare</em> (вокзал)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>H h</strong> [аш] <em>(немой)</em><br><em>Hôtel</em> (отель)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>I i</strong> [и]<br><em>Ici</em> (здесь)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>J j</strong> [жи]<br><em>Jour</em> (день)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>K k</strong> [ка]<br><em>Kilo</em> (килограмм)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>L l</strong> [эль]<br><em>Lune</em> (луна)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>M m</strong> [эм]<br><em>Merci</em> (спасибо)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>N n</strong> [эн]<br><em>Non</em> (нет)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>O o</strong> [о]<br><em>Oui</em> (да)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>P p</strong> [пэ]<br><em>Paris</em> (Париж)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Q q</strong> [кю]<br><em>Quatre</em> (четыре)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>R r</strong> [эр] <em>(картавый)</em><br><em>Rue</em> (улица)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>S s</strong> [эс]<br><em>Salut</em> (привет)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>T t</strong> [тэ]<br><em>Train</em> (поезд)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>U u</strong> [ю / узкий губной]<br><em>Une</em> (одна)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>V v</strong> [вэ]<br><em>Vélo</em> (велосипед)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>W w</strong> [дубль-вэ]<br><em>Wagon</em> (вагон)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>X x</strong> [икс]<br><em>Taxi</em> (такси)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Y y</strong> [игрек]<br><em>Yeux</em> (глаза)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Z z</strong> [зэд]<br><em>Zéro</em> (ноль)</div>
    </div>

    <h3>Французские значки над буквами (Акценты)</h3>
    <ul>
        <li><strong>É é (Accent aigu)</strong> — закрытый чистый звук [э]: <em>café, téléphone</em>.</li>
        <li><strong>È è, À à, Ù ù (Accent grave)</strong> — открытый широкий [э] (<em>mère, père</em>) или различие слов (<em>à</em> = в/к, <em>où</em> = где).</li>
        <li><strong>Ê ê, Ô ô, Â â, Î î, Û û (Accent circonflexe)</strong> — крышечка над звуком: <em>fête, hôtel, château</em>.</li>
        <li><strong>Ç ç (Cédille)</strong> — хвостик под буквой С. Заставляет букву С читаться как [С] перед A, O, U: <em>français [франсэ], garçon [гарсон], ça va [са ва]</em>.</li>
    </ul>

    <h3>Главные буквосочетания: как читать без ошибок</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [уа] — <em>moi [муа], toi [туа], bonsoir [бонсуар]</em></p>
        <p><strong>OU</strong> = [у] — <em>bonjour [бонжур], vous [ву], nous [ну]</em></p>
        <p><strong>AU / EAU</strong> = [о] — <em>beau [бо], restaurant [ресторан], eau [о]</em></p>
        <p><strong>AI / EI</strong> = [э] — <em>mais [мэ], faire [фэр], treize [трэз]</em></p>
        <p><strong>CH</strong> = [ш] — <em>chocolat [шокола], chat [ша]</em></p>
        <p><strong>GN</strong> = [нь] — <em>champagne [шампань], montagne [монтань]</em></p>
    </div>

    <div class="example-box warning">
        <strong>Золотое правило согласных на конце слов:</strong>
        <p>Буквы <strong>D, P, S, T, X, Z</strong> на конце слов обычно <strong>НЕ ЧИТАЮТСЯ</strong>!</p>
        <p><em>salut [салю], chat [ша], deux [дё], vous [ву], paris [пари]</em>.</p>
    </div>
    """

    lesson.content_html_uk = """
    <h2>Французький алфавіт (L'alphabet français)</h2>
    <p>У французькому алфавіті <strong>26 літер</strong>: 6 голосних (<em>A, E, I, O, U, Y</em>) та 20 приголосних.</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px;">
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>A a</strong> [а]<br><em>Avion</em> (літак)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>B b</strong> [бе]<br><em>Bonjour</em> (добрий день)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>C c</strong> [се]<br><em>Café</em> (кава)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>D d</strong> [де]<br><em>Deux</em> (два)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>E e</strong> [е / о-подібний]<br><em>Eau</em> (вода)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>F f</strong> [еф]<br><em>Frite</em> (картопля фрі)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>G g</strong> [же]<br><em>Gare</em> (вокзал)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>H h</strong> [аш] <em>(німий)</em><br><em>Hôtel</em> (готель)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>I i</strong> [і]<br><em>Ici</em> (тут)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>J j</strong> [жі]<br><em>Jour</em> (день)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>K k</strong> [ка]<br><em>Kilo</em> (кілограм)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>L l</strong> [ель]<br><em>Lune</em> (місяць)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>M m</strong> [ем]<br><em>Merci</em> (дякую)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>N n</strong> [ен]<br><em>Non</em> (ні)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>O o</strong> [о]<br><em>Oui</em> (так)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>P p</strong> [пе]<br><em>Paris</em> (Париж)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Q q</strong> [кю]<br><em>Quatre</em> (чотири)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>R r</strong> [ер] <em>(грасуючий)</em><br><em>Rue</em> (вулиця)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>S s</strong> [ес]<br><em>Salut</em> (привіт)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>T t</strong> [те]<br><em>Train</em> (поїзд)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>U u</strong> [ю / губний]<br><em>Une</em> (одна)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>V v</strong> [ве]<br><em>Vélo</em> (велосипед)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>W w</strong> [дубль-ве]<br><em>Wagon</em> (вагон)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>X x</strong> [ікс]<br><em>Taxi</em> (таксі)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Y y</strong> [ігрек]<br><em>Yeux</em> (очі)</div>
        <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;"><strong>Z z</strong> [зед]<br><em>Zéro</em> (нуль)</div>
    </div>

    <h3>Акценти та особливі знаки</h3>
    <ul>
        <li><strong>É é (Accent aigu)</strong> — закритий звук [е]: <em>café, thé</em>.</li>
        <li><strong>È è, À à, Ù ù (Accent grave)</strong> — відкритий звук [е] (<em>mère</em>) або для розрізнення слів (<em>où</em> = де, <em>ou</em> = або).</li>
        <li><strong>Ç ç (Cédille)</strong> — седіль під літерою С. Читається як [С] перед A, O, U: <em>français, garçon, ça va</em>.</li>
    </ul>

    <h3>Головні буквосполучення</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [уа] — <em>moi, toi, bonsoir</em></p>
        <p><strong>OU</strong> = [у] — <em>bonjour, vous, nous</em></p>
        <p><strong>AU / EAU</strong> = [о] — <em>beau, restaurant, eau</em></p>
        <p><strong>CH</strong> = [ш] — <em>chocolat, chat</em></p>
        <p><strong>GN</strong> = [нь] — <em>champagne, montagne</em></p>
    </div>

    <div class="example-box warning">
        <strong>Кінцеві приголосні:</strong> Букви <strong>D, P, S, T, X, Z</strong> на кінці слів зазвичай <strong>не читаються</strong>!
    </div>
    """

    lesson.content_html_en = """
    <h2>The French Alphabet (L'alphabet français)</h2>
    <p>The French alphabet consists of <strong>26 letters</strong>: 6 vowels and 20 consonants.</p>
    <div class="example-box">
        <p>Key letter combinations: <strong>OI</strong> = [wa] (<em>bonsoir</em>), <strong>OU</strong> = [u] (<em>bonjour</em>), <strong>EAU/AU</strong> = [o] (<em>beau</em>), <strong>CH</strong> = [sh] (<em>chocolat</em>), <strong>GN</strong> = [ny] (<em>champagne</em>).</p>
    </div>
    <div class="example-box warning">
        <strong>Silent Endings:</strong> Letters <strong>D, P, S, T, X, Z</strong> are usually silent at the end of French words (e.g. <em>salut, chat, vous, deux</em>).
    </div>
    """

    lesson.content_html_fr = """
    <h2>L'alphabet français et les sons</h2>
    <p>L'alphabet français compte <strong>26 lettres</strong> et des accents particuliers (é, è, ê, ç, ë).</p>
    <ul>
        <li><strong>OI</strong> = [wa] (<em>bonsoir</em>)</li>
        <li><strong>OU</strong> = [u] (<em>bonjour</em>)</li>
        <li><strong>EAU / AU</strong> = [o] (<em>beau</em>)</li>
        <li><strong>CH</strong> = [ʃ] (<em>chat</em>)</li>
        <li><strong>GN</strong> = [ɲ] (<em>montagne</em>)</li>
    </ul>
    """

    lesson.save()
    print("Lesson 1 successfully updated with full 26-letter Alphabet table, Accents, and Reading rules!")

    # Update question
    q = Question.objects.filter(lesson=lesson).first()
    if q:
        q.text_ru = "Как читается буквосочетание 'OI' во французском языке (например в 'bonsoir')?"
        q.text_uk = "Як читається буквосполучення 'OI' у французькій мові (наприклад у 'bonsoir')?"
        q.text_en = "How is the combination 'OI' pronounced in French (e.g. in 'bonsoir')?"
        q.text_fr = "Comment se prononce la combinaison 'OI' en français ?"
        q.save()
        Choice.objects.filter(question=q).delete()
        Choice.objects.create(question=q, text="[уа] / [wa]", text_ru="[уа]", text_uk="[уа]", text_en="[wa]", text_fr="[wa]", is_correct=True)
        Choice.objects.create(question=q, text="[ой] / [oy]", text_ru="[ой]", text_uk="[ой]", text_en="[oy]", text_fr="[oy]", is_correct=False)
        Choice.objects.create(question=q, text="[и] / [i]", text_ru="[и]", text_uk="[і]", text_en="[i]", text_fr="[i]", is_correct=False)
        print("Updated Question 1 for Lesson 1")

if __name__ == '__main__':
    update_alphabet_lesson()
