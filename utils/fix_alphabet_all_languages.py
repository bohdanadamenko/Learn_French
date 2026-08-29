"""
Update Lesson 1 (Alphabet & Phonetics) with full 26-letter alphabet tables,
phonetics, accents, and pronunciation rules across all 4 languages (RU, UK, EN, FR).
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson

def fix_alphabet():
    lesson = Lesson.objects.get(data_lesson_id='lesson1')

    # Complete 26-letter alphabet grid data
    alphabet_letters = [
        ("A a", "[a]", "Avion (самолёт)", "Avion (літак)", "Avion (airplane)", "Avion (avion)"),
        ("B b", "[be]", "Bonjour (здравствуйте)", "Bonjour (добрий день)", "Bonjour (hello)", "Bonjour"),
        ("C c", "[se]", "Café / Cité", "Café / Cité", "Café / City", "Café / Cité"),
        ("D d", "[de]", "Dimanche (воскресенье)", "Dimanche (неділя)", "Dimanche (Sunday)", "Dimanche"),
        ("E e", "[ə]", "Enfant (ребёнок)", "Enfant (дитина)", "Enfant (child)", "Enfant"),
        ("F f", "[ɛf]", "Français (французский)", "Français (французька)", "Français (French)", "Français"),
        ("G g", "[ʒe]", "Gare / Gare", "Gare (вокзал)", "Gare (station)", "Gare / Girafe"),
        ("H h", "[aʃ]", "Hôtel (отель)", "Hôtel (готель)", "Hôtel (hotel)", "Hôtel"),
        ("I i", "[i]", "Image (картинка)", "Image (картинка)", "Image (picture)", "Image"),
        ("J j", "[ʒi]", "Jour (день)", "Jour (день)", "Jour (day)", "Jour"),
        ("K k", "[ka]", "Kilo (килограмм)", "Kilo (кілограм)", "Kilo (kilogram)", "Kilo / Kot"),
        ("L l", "[ɛl]", "Livre (книга)", "Livre (книга)", "Livre (book)", "Livre"),
        ("M m", "[ɛm]", "Maison (дом)", "Maison (будинок)", "Maison (house)", "Maison"),
        ("N n", "[ɛn]", "Nuit (ночь)", "Nuit (ніч)", "Nuit (night)", "Nuit"),
        ("O o", "[o]", "Orange (апельсин)", "Orange (апельсин)", "Orange (orange)", "Orange"),
        ("P p", "[pe]", "Pistolet (бельг. булочка)", "Pistolet (булочка)", "Pistolet (bread roll)", "Pistolet"),
        ("Q q", "[ky]", "Quatre (четыре)", "Quatre (чотири)", "Quatre (four)", "Quatre"),
        ("R r", "[ɛʁ]", "Rue (улица)", "Rue (вулиця)", "Rue (street)", "Rue"),
        ("S s", "[ɛs]", "Soleil (солнце)", "Soleil (сонце)", "Soleil (sun)", "Soleil"),
        ("T t", "[te]", "Train (поезд)", "Train (поїзд)", "Train (train)", "Train"),
        ("U u", "[y]", "Une (одна)", "Une (одна)", "Une (one/a)", "Une / Université"),
        ("V v", "[ve]", "Ville (город)", "Ville (місто)", "Ville (city)", "Ville"),
        ("W w", "[dubləve]", "Wallonie (Валлония)", "Wallonie (Валлонія)", "Wallonie (Wallonia)", "Wallonie / W.-C."),
        ("X x", "[iks]", "Taxi (такси)", "Taxi (таксі)", "Taxi (taxi)", "Taxi"),
        ("Y y", "[igʁɛk]", "Yeux (глаза)", "Yeux (очі)", "Yeux (eyes)", "Yeux"),
        ("Z z", "[zɛd]", "Zèbre (зебра)", "Zèbre (зебра)", "Zèbre (zebra)", "Zèbre / Zéro"),
    ]

    def make_grid(lang_idx):
        items = []
        for l, ipa, ru_ex, uk_ex, en_ex, fr_ex in alphabet_letters:
            ex = [ru_ex, uk_ex, en_ex, fr_ex][lang_idx]
            items.append(f'<div><strong>{l}</strong> <span>{ipa}</span><br><em>{ex}</em></div>')
        return '<div class="conjugation-grid" style="grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px;">\n' + '\n'.join(items) + '\n</div>'

    grid_ru = make_grid(0)
    grid_uk = make_grid(1)
    grid_en = make_grid(2)
    grid_fr = make_grid(3)

    # Content RU
    content_ru = f"""
    <h2>Французский алфавит (L'alphabet français)</h2>
    <p>Во французском алфавите <strong>26 букв</strong>: 6 гласных (<em>A, E, I, O, U, Y</em>) и 20 согласных.</p>

    {grid_ru}

    <h3>Диакритические знаки (акценты):</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
        <div><strong>Accent aigu (é)</strong><br>Закрытый звук [e]<br><em>café, été</em></div>
        <div><strong>Accent grave (à, è, ù)</strong><br>Открытый звук [ɛ] / смысл<br><em>mère, où, là</em></div>
        <div><strong>Accent circonflexe (â, ê, î, ô, û)</strong><br>Долгий звук<br><em>fête, hôtel, château</em></div>
        <div><strong>Tréma (ë, ï, ü)</strong><br>Раздельное чтение<br><em>Noël, maïs</em></div>
        <div><strong>Cédille (ç)</strong><br>Буква С читается как [с]<br><em>français, garçon</em></div>
    </div>

    <h3>Главные буквосочетания и звуки:</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [wa] (уа) — <em>bonsoir, trois, croissant</em></p>
        <p><strong>OU</strong> = [u] (у) — <em>bonjour, vous, nous</em></p>
        <p><strong>EAU / AU</strong> = [o] (о) — <em>beau, gâteau, restaurant</em></p>
        <p><strong>AI / EI</strong> = [ɛ] (э) — <em>maison, treize</em></p>
        <p><strong>CH</strong> = [ʃ] (ш) — <em>chocolat, chicon</em></p>
        <p><strong>GN</strong> = [ɲ] (нь) — <em>champagne, montagne</em></p>
        <p><strong>ILL / IL</strong> = [j] (й) — <em>famille, billet, soleil</em></p>
    </div>

    <div class="example-box warning">
        <strong>Золотое правило согласных на конце слов:</strong>
        <p>Конечные согласные <strong>D, P, S, T, X, Z</strong> обычно <strong>НЕ читаются</strong>:</p>
        <p><em>Parisc [пари], Grand [гран], Salut [салю], Vous [ву], Frites [фрит].</em></p>
        <p>Исключения (правило CaReFuL): буквы <strong>C, R, F, L</strong> на конце обычно читаются (<em>sac, soir, neuf, festival</em>).</p>
    </div>
    """

    # Content UK
    content_uk = f"""
    <h2>Французький алфавіт (L'alphabet français)</h2>
    <p>У французькому алфавіті <strong>26 літер</strong>: 6 голосних (<em>A, E, I, O, U, Y</em>) та 20 приголосних.</p>

    {grid_uk}

    <h3>Діакритичні знаки (акценти):</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
        <div><strong>Accent aigu (é)</strong><br>Закритий звук [e]<br><em>café, été</em></div>
        <div><strong>Accent grave (à, è, ù)</strong><br>Відкритий звук [ɛ]<br><em>mère, où, là</em></div>
        <div><strong>Accent circonflexe (â, ê, î, ô, û)</strong><br>Подовжений звук<br><em>fête, hôtel</em></div>
        <div><strong>Tréma (ë, ï, ü)</strong><br>Окреме читання<br><em>Noël, maïs</em></div>
        <div><strong>Cédille (ç)</strong><br>Буква С читається як [с]<br><em>français, garçon</em></div>
    </div>

    <h3>Ключові буквосполучення:</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [wa] (уа) — <em>bonsoir, trois</em></p>
        <p><strong>OU</strong> = [u] (у) — <em>bonjour, vous</em></p>
        <p><strong>EAU / AU</strong> = [o] (о) — <em>beau, gâteau</em></p>
        <p><strong>CH</strong> = [ʃ] (ш) — <em>chocolat</em></p>
        <p><strong>GN</strong> = [ɲ] (нь) — <em>champagne</em></p>
    </div>

    <div class="example-box warning">
        <strong>Німі приголосні в кінці слів:</strong>
        <p>Кінцеві <strong>D, P, S, T, X, Z</strong> зазвичай <strong>не читаються</strong> (<em>Paris, Grand, Salut, Vous</em>).</p>
    </div>
    """

    # Content EN
    content_en = f"""
    <h2>The French Alphabet (L'alphabet français)</h2>
    <p>The French alphabet has <strong>26 letters</strong>: 6 vowels (<em>A, E, I, O, U, Y</em>) and 20 consonants.</p>

    {grid_en}

    <h3>French Diacritics (Accents):</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
        <div><strong>Accent aigu (é)</strong><br>Closed [e]<br><em>café, été</em></div>
        <div><strong>Accent grave (à, è, ù)</strong><br>Open [ɛ]<br><em>mère, où, là</em></div>
        <div><strong>Accent circonflexe (â, ê, î, ô, û)</strong><br>Longer vowel<br><em>fête, hôtel</em></div>
        <div><strong>Tréma (ë, ï, ü)</strong><br>Separate vowel sound<br><em>Noël, maïs</em></div>
        <div><strong>Cédille (ç)</strong><br>C pronounced as [s]<br><em>français, garçon</em></div>
    </div>

    <h3>Key Letter Combinations:</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [wa] — <em>bonsoir, trois, croissant</em></p>
        <p><strong>OU</strong> = [u] — <em>bonjour, vous, nous</em></p>
        <p><strong>EAU / AU</strong> = [o] — <em>beau, gâteau</em></p>
        <p><strong>CH</strong> = [ʃ] (sh) — <em>chocolat</em></p>
        <p><strong>GN</strong> = [ɲ] (ny) — <em>champagne</em></p>
    </div>

    <div class="example-box warning">
        <strong>Silent Endings:</strong>
        <p>Final consonants <strong>D, P, S, T, X, Z</strong> are usually <strong>silent</strong> (<em>Paris, Grand, Salut, Vous</em>).</p>
    </div>
    """

    # Content FR
    content_fr = f"""
    <h2>L'alphabet français et la phonétique</h2>
    <p>L'alphabet français compte <strong>26 lettres</strong> : 6 voyelles (<em>A, E, I, O, U, Y</em>) et 20 consonnes.</p>

    {grid_fr}

    <h3>Les accents et signes diacritiques :</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
        <div><strong>Accent aigu (é)</strong><br>Son fermé [e]<br><em>café, été</em></div>
        <div><strong>Accent grave (à, è, ù)</strong><br>Son ouvert [ɛ]<br><em>mère, où, là</em></div>
        <div><strong>Accent circonflexe (â, ê, î, ô, û)</strong><br>Voyelle allongée<br><em>fête, hôtel</em></div>
        <div><strong>Tréma (ë, ï, ü)</strong><br>Prononciation séparée<br><em>Noël, maïs</em></div>
        <div><strong>Cédille (ç)</strong><br>Se prononce [s]<br><em>français, garçon</em></div>
    </div>

    <h3>Les combinaisons phonétiques essentielles :</h3>
    <div class="example-box">
        <p><strong>OI</strong> = [wa] — <em>bonsoir, trois, croissant</em></p>
        <p><strong>OU</strong> = [u] — <em>bonjour, vous, nous</em></p>
        <p><strong>EAU / AU</strong> = [o] — <em>beau, gâteau</em></p>
        <p><strong>CH</strong> = [ʃ] — <em>chocolat, chicon</em></p>
        <p><strong>GN</strong> = [ɲ] — <em>champagne, montagne</em></p>
        <p><strong>ILL / IL</strong> = [j] — <em>famille, billet, soleil</em></p>
    </div>

    <div class="example-box warning">
        <strong>Consonnes finales muettes :</strong>
        <p>Les lettres finales <strong>D, P, S, T, X, Z</strong> ne se prononcent généralement pas en fin de mot :</p>
        <p><em>Paris, Grand, Salut, Vous, Frites.</em></p>
    </div>
    """

    lesson.content_html = content_uk
    lesson.content_html_uk = content_uk
    lesson.content_html_ru = content_ru
    lesson.content_html_en = content_en
    lesson.content_html_fr = content_fr
    lesson.save()
    print("Lesson 1 updated with full 26-letter alphabet in all 4 languages!")

if __name__ == '__main__':
    fix_alphabet()
