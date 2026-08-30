"""
Script to enrich and expand French articles (du, de la, de l', des, un, une, le, la, les, au, aux)
in the basics:
- Upgrade lesson4 (All categories of French articles overview)
- Upgrade lesson-partitive (Masterclass on du, de la, de l', des + negation transformation + quantities + contracted articles)
- Reorder lesson-partitive to be right next to lesson4 in Basics (Topic 2)
- Include interactive 3D flashcards (Карточки для запоминания) and quizzes
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

def enrich_articles():
    t_grammar = Topic.objects.filter(id=2).first() or Topic.objects.filter(order=2).first()

    # 1. Upgrade lesson4: Complete Guide to Articles
    l4 = Lesson.objects.filter(data_lesson_id="lesson4").first()
    if l4:
        l4.title_uk = "🎯 Усі артиклі у французькій: Означені, Неозначені та Рід"
        l4.title_ru = "🎯 Все артикли во французском: Определенные, Неопределенные и Род"
        l4.title_en = "🎯 Complete Guide to French Articles & Gender"
        l4.title_fr = "🎯 Les articles en français et le genre"

        l4.content_html_uk = """
        <h2>Французькі артиклі — Головний паспорт кожного іменника</h2>
        <p>У французькій мові іменники <strong>майже ніколи не вживаються самі по собі</strong>. Перед кожним словом обов'язково стоїть артикль, який вказує на його <strong>рід (чоловічий / жіночий)</strong> та <strong>кількість</strong>.</p>

        <h3>1. 🟢 Неозначені артиклі (Articles indéfinis) — Будь-який / Один з багатьох</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div><strong style="color:var(--accent-blue); font-size:1.15rem;">UN</strong> [ен]<br><span style="color:var(--text-tertiary);">Чоловічий рід (однина)</span><br><em>Un café, un croissant, un ami</em></div>
            <div><strong style="color:var(--accent-purple); font-size:1.15rem;">UNE</strong> [юн]<br><span style="color:var(--text-tertiary);">Жіночий рід (однина)</span><br><em>Une gaufre, une table, une bière</em></div>
            <div><strong style="color:var(--accent-green); font-size:1.15rem;">DES</strong> [де]<br><span style="color:var(--text-tertiary);">Множина (декілька)</span><br><em>Des frites, des amis, des croissants</em></div>
        </div>

        <h3>2. 🔵 Означені артиклі (Articles définis) — Конкретний / Усім відомий</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div><strong style="color:var(--accent-blue); font-size:1.15rem;">LE</strong> [льйо]<br><span style="color:var(--text-tertiary);">Чоловічий рід (однина)</span><br><em>Le chocolat, le train, le musée</em></div>
            <div><strong style="color:var(--accent-purple); font-size:1.15rem;">LA</strong> [ля]<br><span style="color:var(--text-tertiary);">Жіночий рід (однина)</span><br><em>La ville, la gare, la maison</em></div>
            <div><strong style="color:var(--accent-cyan); font-size:1.15rem;">L'</strong> [ель]<br><span style="color:var(--text-tertiary);">Перед голосною чи німою H</span><br><em>L'eau, l'hôtel, l'appartement</em></div>
            <div><strong style="color:var(--accent-green); font-size:1.15rem;">LES</strong> [ле]<br><span style="color:var(--text-tertiary);">Множина (конкретні)</span><br><em>Les enfants, les rues, les gaufres</em></div>
        </div>

        <h3>🃏 Картки для запам'ятовування</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Одна бельгійська вафля</strong>
                        <span class="flip-hint">Натисніть для перекладу</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Une gaufre</strong>
                        <span style="font-size:0.8rem;">[юн гофр] 🇧🇪</span>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-purple);">Вокзал (конкретний)</strong>
                        <span class="flip-hint">Натисніть для перекладу</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">La gare</strong>
                        <span style="font-size:0.8rem;">[ля гар]</span>
                    </div>
                </div>
            </div>
        </div>
        """

        l4.content_html_ru = """
        <h2>Французские артикли — Паспорт каждого существительного</h2>
        <p>Во французском языке существительные <strong>практически никогда не используются без артиклей</strong>. Артикль указывает на <strong>род (мужской / женский)</strong> и <strong>число</strong>.</p>

        <h3>1. 🟢 Неопределенные артикли (Articles indéfinis):</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div><strong style="color:var(--accent-blue); font-size:1.15rem;">UN</strong> [эн]<br><span style="color:var(--text-tertiary);">Мужской род (ед.ч.)</span><br><em>Un café, un croissant</em></div>
            <div><strong style="color:var(--accent-purple); font-size:1.15rem;">UNE</strong> [юн]<br><span style="color:var(--text-tertiary);">Женский род (ед.ч.)</span><br><em>Une gaufre, une table</em></div>
            <div><strong style="color:var(--accent-green); font-size:1.15rem;">DES</strong> [дэ]<br><span style="color:var(--text-tertiary);">Множественное число</span><br><em>Des frites, des croissants</em></div>
        </div>

        <h3>2. 🔵 Определенные артикли (Articles définis):</h3>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div><strong style="color:var(--accent-blue); font-size:1.15rem;">LE</strong> [лё]<br><span style="color:var(--text-tertiary);">Мужской род (ед.ч.)</span><br><em>Le chocolat, le train</em></div>
            <div><strong style="color:var(--accent-purple); font-size:1.15rem;">LA</strong> [ля]<br><span style="color:var(--text-tertiary);">Женский род (ед.ч.)</span><br><em>La ville, la gare</em></div>
            <div><strong style="color:var(--accent-cyan); font-size:1.15rem;">L'</strong> [эль]<br><span style="color:var(--text-tertiary);">Перед гласной или немой H</span><br><em>L'eau, l'appartement</em></div>
            <div><strong style="color:var(--accent-green); font-size:1.15rem;">LES</strong> [ле]<br><span style="color:var(--text-tertiary);">Множественное число</span><br><em>Les enfants, les rues</em></div>
        </div>

        <h3>🃏 Карточки для запоминания</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Одна бельгийская вафля</strong>
                        <span class="flip-hint">Нажмите для перевода</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Une gaufre</strong>
                        <span style="font-size:0.8rem;">[юн гофр] 🇧🇪</span>
                    </div>
                </div>
            </div>
        </div>
        """
        l4.save()
        print("Updated Lesson 4: Complete Articles Guide.")

    # 2. Upgrade lesson-partitive: Masterclass DU, DE LA, DE L', DES
    lp, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-partitive", defaults={"topic": t_grammar, "order": 7})
    lp.topic = t_grammar
    lp.order = 7
    lp.title_uk = "🥖 Часткові артиклі DU, DE LA, DE L', DES та злиття артиклів"
    lp.title_ru = "🥖 Частичные артикли DU, DE LA, DE L', DES и слитные артикли"
    lp.title_en = "🥖 Partitive Articles: DU, DE LA, DE L', DES"
    lp.title_fr = "🥖 Les articles partitifs : DU, DE LA, DE L', DES"

    lp.content_html_uk = """
    <h2>Часткові артиклі (Articles Partitifs) — Незлічувані кількості</h2>
    <p>Коли ви їсте, п'єте або берете <strong>частину від чогось цілого або незлічуваного</strong> (хліб, сир, вода, час, гроші), французи обов'язково вживають <strong>частковий артикль</strong>:</p>

    <h3>1. 📊 Таблиця часткових артиклів:</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue); font-size:1.2rem;">DU</strong> [дю]<br>
            <span style="color:var(--text-tertiary);">Чоловічий рід (незлічуване)</span><br>
            <em>Du pain</em> (хліб), <em>du fromage</em> (сир), <em>du café</em> (кава), <em>du chocolat</em>.
        </div>
        <div>
            <strong style="color:var(--accent-purple); font-size:1.2rem;">DE LA</strong> [дьо ля]<br>
            <span style="color:var(--text-tertiary);">Жіночий рід (незлічуване)</span><br>
            <em>De la bière</em> (пиво), <em>de la viande</em> (м'ясо), <em>de la salade</em>, <em>de la confiture</em>.
        </div>
        <div>
            <strong style="color:var(--accent-cyan); font-size:1.2rem;">DE L'</strong> [дьо лель]<br>
            <span style="color:var(--text-tertiary);">Перед голосною чи німою H</span><br>
            <em>De l'eau</em> (вода), <em>de l'huile</em> (олія), <em>de l'argent</em> (гроші).
        </div>
        <div>
            <strong style="color:var(--accent-green); font-size:1.2rem;">DES</strong> [де]<br>
            <span style="color:var(--text-tertiary);">Множина</span><br>
            <em>Des frites</em> (картопля фрі), <em>des légumes</em> (овочі), <em>des pâtes</em> (макарони).
        </div>
    </div>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Головне правило заперечення: DU / DE LA / DES перетворюються на DE / D'!</div>
        <div class="callout-content">
            <p>У запереченні будь-який частковий артикль змінюється на звичайне <strong>DE</strong> (або <strong>D'</strong> перед голосною):</p>
            <ul>
                <li>✅ <em>Je bois <strong>du</strong> café</em> (Я п'ю каву) ➔ ❌ <em>Je ne bois pas <strong>de</strong> café</em> (Я не п'ю кави).</li>
                <li>✅ <em>J'ai <strong>de l'</strong>argent</em> (У мене є гроші) ➔ ❌ <em>Je n'ai pas <strong>d'</strong>argent</em> (У мене немає грошей).</li>
                <li>✅ <em>Je mange <strong>des</strong> frites</em> ➔ ❌ <em>Je ne mange pas <strong>de</strong> frites</em>.</li>
            </ul>
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Точні кількості завжди вимагають прийменника DE:</div>
        <div class="callout-content">
            <ul>
                <li><em>Un kilo <strong>de</strong> tomates</em> (Кілограм помідорів)</li>
                <li><em>Une bouteille <strong>d'</strong>eau</em> (Пляшка води)</li>
                <li><em>Beaucoup <strong>de</strong> fromage</em> (Багато сиру)</li>
                <li><em>Un peu <strong>de</strong> sucre</em> (Трохи цукру)</li>
            </ul>
        </div>
    </div>

    <h3>2. 🔀 Злиті артиклі (Articles contractés):</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
        <div><strong>À + LE = AU</strong><br><em>Je vais au restaurant</em></div>
        <div><strong>À + LES = AUX</strong><br><em>Je vais aux friteries</em></div>
        <div><strong>DE + LE = DU</strong><br><em>Le goût du chocolat</em></div>
        <div><strong>DE + LES = DES</strong><br><em>Le prix des billets</em></div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я п'ю воду</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je bois de l'eau</strong>
                    <span style="font-size:0.8rem;">[жьо буа дьо льо]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Я хочу сиру</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je veux du fromage</strong>
                    <span style="font-size:0.8rem;">[жьо вьо дю фромаж]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-green);">У мене немає цукру</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je n'ai pas de sucre</strong>
                    <span style="font-size:0.8rem;">[жьо не па дьо сюкр]</span>
                </div>
            </div>
        </div>
    </div>
    """

    lp.content_html_ru = """
    <h2>Частичные артикли (Articles Partitifs) — Неисчисляемые количества</h2>
    <p>Когда вы едите, пьете или берете <strong>часть от чего-то неисчисляемого</strong> (хлеб, сыр, вода, деньги, время), французы обязательно используют <strong>частичный артикль</strong>:</p>

    <h3>1. 📊 Таблица частичных артиклей:</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
        <div>
            <strong style="color:var(--accent-blue); font-size:1.2rem;">DU</strong> [дю]<br>
            <span style="color:var(--text-tertiary);">Мужской род (неисчисляемое)</span><br>
            <em>Du pain</em> (хлеб), <em>du fromage</em> (сыр), <em>du café</em> (кофе), <em>du chocolat</em>.
        </div>
        <div>
            <strong style="color:var(--accent-purple); font-size:1.2rem;">DE LA</strong> [дё ля]<br>
            <span style="color:var(--text-tertiary);">Женский род (неисчисляемое)</span><br>
            <em>De la bière</em> (пиво), <em>de la viande</em> (мясо), <em>de la salade</em>.
        </div>
        <div>
            <strong style="color:var(--accent-cyan); font-size:1.2rem;">DE L'</strong> [дё лель]<br>
            <span style="color:var(--text-tertiary);">Перед гласной или немой H</span><br>
            <em>De l'eau</em> (вода), <em>de l'huile</em> (масло), <em>de l'argent</em> (деньги).
        </div>
        <div>
            <strong style="color:var(--accent-green); font-size:1.2rem;">DES</strong> [дэ]<br>
            <span style="color:var(--text-tertiary);">Множественное число</span><br>
            <em>Des frites</em> (картофель фри), <em>des légumes</em> (овощи).
        </div>
    </div>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Главное правило отрицания: DU / DE LA / DES превращаются в DE / D'!</div>
        <div class="callout-content">
            <p>В отрицании любой частичный артикль заменяется на простое <strong>DE</strong> (или <strong>D'</strong> перед гласной):</p>
            <ul>
                <li>✅ <em>Je bois <strong>du</strong> café</em> ➔ ❌ <em>Je ne bois pas <strong>de</strong> café</em>.</li>
                <li>✅ <em>J'ai <strong>de l'</strong>argent</em> ➔ ❌ <em>Je n'ai pas <strong>d'</strong>argent</em>.</li>
                <li>✅ <em>Je mange <strong>des</strong> frites</em> ➔ ❌ <em>Je ne mange pas <strong>de</strong> frites</em>.</li>
            </ul>
        </div>
    </div>

    <h3>2. 🔀 Слитные артикли (Articles contractés):</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
        <div><strong>À + LE = AU</strong><br><em>Je vais au restaurant</em></div>
        <div><strong>À + LES = AUX</strong><br><em>Je vais aux magasins</em></div>
        <div><strong>DE + LE = DU</strong><br><em>Le goût du chocolat</em></div>
        <div><strong>DE + LES = DES</strong><br><em>Le prix des billets</em></div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я пью воду</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je bois de l'eau</strong>
                    <span style="font-size:0.8rem;">[жё буа дё льо]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Я хочу сыра</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je veux du fromage</strong>
                    <span style="font-size:0.8rem;">[жё вё дю фромаж]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-green);">У меня нет сахара</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je n'ai pas de sucre</strong>
                    <span style="font-size:0.8rem;">[жё нэ па дё сюкр]</span>
                </div>
            </div>
        </div>
    </div>
    """
    lp.content_html_en = "<p>Partitive articles DU, DE LA, DE L', DES in French.</p>"
    lp.content_html_fr = "<p>Les articles partitifs DU, DE LA, DE L', DES.</p>"
    lp.save()

    Question.objects.filter(lesson=lp).delete()
    qp1 = Question.objects.create(lesson=lp, order=1, text="Какой частичный артикль используется со словом 'pain' (хлеб - мужской род)?", text_ru="Какой частичный артикль используется со словом 'pain' (хлеб - мужской род)?", text_uk="Який частковий артикль використовується зі словом 'pain' (хліб - чоловічий рід)?", text_en="Which partitive article is used with 'pain'?", text_fr="Quel article partitif utilise-t-on avec 'pain' ?")
    Choice.objects.create(question=qp1, text="Du pain", text_ru="Du pain [дю пэн]", text_uk="Du pain [дю пен]", text_en="Du pain", text_fr="Du pain", is_correct=True)
    Choice.objects.create(question=qp1, text="De la pain", text_ru="De la pain", text_uk="De la pain", text_en="De la pain", text_fr="De la pain", is_correct=False)

    qp2 = Question.objects.create(lesson=lp, order=2, text="Как правильно сказать в отрицании: «Я не пью кофе»?", text_ru="Как правильно сказать в отрицании: «Я не пью кофе»?", text_uk="Як правильно сказати в запереченні: «Я не п'ю кави»?", text_en="How to say 'I don't drink coffee' in negative?", text_fr="Comment dit-on 'Je ne bois pas de café' ?")
    Choice.objects.create(question=qp2, text="Je ne bois pas de café", text_ru="Je ne bois pas de café (du превращается в de)", text_uk="Je ne bois pas de café (du перетворюється на de)", text_en="Je ne bois pas de café", text_fr="Je ne bois pas de café", is_correct=True)
    Choice.objects.create(question=qp2, text="Je ne bois pas du café", text_ru="Je ne bois pas du café (ошибка: du не используется в отрицании)", text_uk="Je ne bois pas du café (помилка)", text_en="Je ne bois pas du café", text_fr="Je ne bois pas du café", is_correct=False)

    print("Successfully enriched and organized articles and partitives in the basics!")

if __name__ == '__main__':
    enrich_articles()
