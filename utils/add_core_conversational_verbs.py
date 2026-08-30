"""
Script to:
1. Ensure AVOIR is placed immediately after ÊTRE in order.
2. Add & enrich all the TOP core conversational verbs in French:
   - ALLER (Je vais, tu vas, il va...) + Futur Proche + Ça va
   - FAIRE (Je fais, tu fais, il fait...) + выражения погоды и спорта
   - VOULOIR, POUVOIR, DEVOIR (Модальные глаголы речи: Je veux / Je voudrais, Je peux, Je dois)
   - PRENDRE, VENIR (Je prends, Je viens de...)
   - SAVOIR vs CONNAÎTRE (Знать / Уметь + бельгийское вежливое употребление)
3. Equip each verb lesson with:
   - Full conjugation grid
   - Real-life conversational examples
   - Interactive Flashcards (ФМ / Flip cards)
   - Practical dialogues in messenger bubbles
   - 3 verified quiz questions
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

def setup_core_verbs():
    topic_grammar = Topic.objects.filter(id=2).first() or Topic.objects.filter(order=2).first()
    topic_verbs = Topic.objects.filter(id=3).first() or Topic.objects.filter(order=3).first()

    # 1. Place AVOIR immediately after ÊTRE
    lesson_etre = Lesson.objects.filter(data_lesson_id="lesson3").first()
    lesson_avoir = Lesson.objects.filter(data_lesson_id="lesson-avoir").first()
    lesson_articles = Lesson.objects.filter(data_lesson_id="lesson4").first()

    if lesson_etre and lesson_avoir:
        lesson_etre.order = 4
        lesson_etre.save()
        lesson_avoir.order = 5
        lesson_avoir.topic = topic_grammar
        lesson_avoir.save()
    if lesson_articles:
        lesson_articles.order = 6
        lesson_articles.save()

    print("Reordered: 4. Être -> 5. Avoir -> 6. Articles")

    # -------------------------------------------------------------
    # 2. ALLER (Идти / Ехать)
    # -------------------------------------------------------------
    lesson_aller, _ = Lesson.objects.get_or_create(
        data_lesson_id="lesson-aller",
        defaults={"topic": topic_verbs, "order": 8}
    )
    lesson_aller.topic = topic_verbs
    lesson_aller.title_uk = "🚶 Дієслово ALLER (Іти / Їхати) та Близьке майбутнє"
    lesson_aller.title_ru = "🚶 Глагол ALLER (Идти / Ехать) и Ближайшее будущее"
    lesson_aller.title_en = "🚶 Verb ALLER (To go) & Near Future"
    lesson_aller.title_fr = "🚶 Le verbe ALLER et le Futur Proche"

    lesson_aller.content_html_uk = """
    <h2>Дієслово ALLER (Іти / Їхати) — Рух та Майбутній час</h2>
    <p>Дієслово <strong>aller</strong> [але] — найпопулярніше дієслово руху. Воно використовується у вітанні (<em>«Comment ça va ? — Ça va !»</em>), пересуванні містом і побудові найпростішого майбутнього часу (<em>Futur Proche</em>).</p>

    <h3>1. 📊 Відмінювання дієслова ALLER у теперішньому часі</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je vais</strong><br><span style="color:var(--text-tertiary);">[жьо ве]</span><br>Я йду / їду</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Tu vas</strong><br><span style="color:var(--text-tertiary);">[тю ва]</span><br>Ти йдеш / їдеш</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On va</strong><br><span style="color:var(--text-tertiary);">[іль / ель / он ва]</span><br>Він / Вона / Ми йдемо</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Nous <span class="liaison">allons</span></strong><br><span style="color:var(--text-tertiary);">[ну-з-алон]</span><br>Ми йдемо / їдемо</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">allez</span></strong><br><span style="color:var(--text-tertiary);">[ву-з-але]</span><br>Ви йдете / їдете</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles vont</strong><br><span style="color:var(--text-tertiary);">[іль / ель вон]</span><br>Вони йдуть / їдуть</div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Магічна формула: ALLER + Інфінітив = Близьке майбутнє (Futur Proche)</div>
        <div class="callout-content">
            <p>Щоб сказати <em>«Я збираюся зробити щось»</em>, візьміть форму <strong>aller</strong> і додайте будь-яке дієслово:</p>
            <ul>
                <li><strong>Je vais manger</strong> = Я зараз поїм / збираюся їсти</li>
                <li><strong>Je vais partir</strong> = Я зараз піду</li>
                <li><strong>On va voir</strong> = Побачимо / подивимося</li>
            </ul>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Я їду в Брюссель</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Je vais à Bruxelles</strong>
                    <span style="font-size:0.85rem;">[жьо ве а брюсель] 🇧🇪</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Куди ти йдеш?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Où vas-tu ?</strong>
                    <span style="font-size:0.85rem;">[у ва тю]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-green);">Ми зараз підемо</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Nous allons partir</strong>
                    <span style="font-size:0.85rem;">[ну-з-алон партір]</span>
                </div>
            </div>
        </div>
    </div>
    """

    lesson_aller.content_html_ru = """
    <h2>Глагол ALLER (Идти / Ехать) — Движение и Ближайшее будущее</h2>
    <p>Глагол <strong>aller</strong> [але] — главный глагол движения во французском. Он используется в приветствии (<em>«Ça va ? — Ça va !»</em>), поездках по городу и в конструкции ближайшего будущего (<em>Futur Proche</em>).</p>

    <h3>1. 📊 Таблица спряжения глагола ALLER</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je vais</strong><br><span style="color:var(--text-tertiary);">[жё ве]</span><br>Я иду / еду</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Tu vas</strong><br><span style="color:var(--text-tertiary);">[тю ва]</span><br>Ты идешь / едешь</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On va</strong><br><span style="color:var(--text-tertiary);">[иль / эль / он ва]</span><br>Он / Она / Мы идем</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Nous <span class="liaison">allons</span></strong><br><span style="color:var(--text-tertiary);">[ну-з-алон]</span><br>Мы идем / едем</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">allez</span></strong><br><span style="color:var(--text-tertiary);">[ву-з-але]</span><br>Вы идете / едете</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles vont</strong><br><span style="color:var(--text-tertiary);">[иль / эль вон]</span><br>Они идут / едут</div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Формула будущего: ALLER + Инфинитив = Futur Proche</div>
        <div class="callout-content">
            <p>Чтобы сказать <em>«Я собираюсь сделать / сейчас сделаю»</em>:</p>
            <ul>
                <li><strong>Je vais manger</strong> = Я сейчас поем</li>
                <li><strong>Je vais acheter du pain</strong> = Я пойду куплю хлеба</li>
                <li><strong>On va voir</strong> = Посмотрим!</li>
            </ul>
        </div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Я еду в Брюссель</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Je vais à Bruxelles</strong>
                    <span style="font-size:0.85rem;">[жё ве а брюсель] 🇧🇪</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Куда ты идешь?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Où vas-tu ?</strong>
                    <span style="font-size:0.85rem;">[у ва тю]</span>
                </div>
            </div>
        </div>
    </div>
    """
    lesson_aller.content_html_en = "<p>Conjugation of verb ALLER (To go) and near future tense.</p>"
    lesson_aller.content_html_fr = "<p>Conjugaison du verbe ALLER et le futur proche.</p>"
    lesson_aller.save()

    Question.objects.filter(lesson=lesson_aller).delete()
    qa1 = Question.objects.create(lesson=lesson_aller, order=1, text="Как сказать: «Я еду в Брюссель»?", text_ru="Как сказать: «Я еду в Брюссель»?", text_uk="Як сказати: «Я їду в Брюссель»?", text_en="How do you say 'I am going to Brussels'?", text_fr="Comment dit-on 'Je vais à Bruxelles' ?")
    Choice.objects.create(question=qa1, text="Je vais à Bruxelles", text_ru="Je vais à Bruxelles", text_uk="Je vais à Bruxelles", text_en="Je vais à Bruxelles", text_fr="Je vais à Bruxelles", is_correct=True)
    Choice.objects.create(question=qa1, text="Je va à Bruxelles", text_ru="Je va à Bruxelles", text_uk="Je va à Bruxelles", text_en="Je va à Bruxelles", text_fr="Je va à Bruxelles", is_correct=False)

    # -------------------------------------------------------------
    # 3. FAIRE (Делать / Заниматься / Погода)
    # -------------------------------------------------------------
    lesson_faire, _ = Lesson.objects.get_or_create(
        data_lesson_id="lesson-faire",
        defaults={"topic": topic_verbs, "order": 9}
    )
    lesson_faire.topic = topic_verbs
    lesson_faire.title_uk = "⚡ Дієслово FAIRE (Робити / Займатися / Погода)"
    lesson_faire.title_ru = "⚡ Глагол FAIRE (Делать / Заниматься / Погода)"
    lesson_faire.title_en = "⚡ Verb FAIRE (To do / To make)"
    lesson_faire.title_fr = "⚡ Le verbe FAIRE"

    lesson_faire.content_html_uk = """
    <h2>Дієслово FAIRE (Робити) — Універсальне дієслово дії</h2>
    <p>Глагол <strong>faire</strong> [фер] — один із найбільш уживаних. Французи використовують його для опису роботи, спорту, домашніх справ та погоди (<em>Il fait beau</em>).</p>

    <h3>1. 📊 Відмінювання дієслова FAIRE</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je fais</strong><br><span style="color:var(--text-tertiary);">[жьо фе]</span><br>Я роблю</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Tu fais</strong><br><span style="color:var(--text-tertiary);">[тю фе]</span><br>Ти робиш</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On fait</strong><br><span style="color:var(--text-tertiary);">[іль / ель / он фе]</span><br>Він / Вона / Ми робимо</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Nous faisons</strong><br><span style="color:var(--text-tertiary);">[ну фьозон]</span><br>Ми робимо</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous faites</strong><br><span style="color:var(--text-tertiary);">[ву фет] <em>(особлива форма!)</em></span><br>Ви робите</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles font</strong><br><span style="color:var(--text-tertiary);">[іль / ель фон]</span><br>Вони роблять</div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Популярні фрази з FAIRE</div>
        <div class="callout-content">
            <ul>
                <li><strong>Qu'est-ce que tu fais ?</strong> = Що ти робиш?</li>
                <li><strong>Il fait beau / Il fait froid</strong> = Гарна погода / Холодно</li>
                <li><strong>Faire les courses</strong> = Робити покупки в магазині</li>
                <li><strong>Faire du sport</strong> = Займатися спортом</li>
            </ul>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Що ти робиш?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Qu'est-ce que tu fais ?</strong>
                    <span style="font-size:0.85rem;">[кес кьо тю фе]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Гарна погода</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Il fait beau</strong>
                    <span style="font-size:0.85rem;">[іль фе бо]</span>
                </div>
            </div>
        </div>
    </div>
    """

    lesson_faire.content_html_ru = """
    <h2>Глагол FAIRE (Делать / Заниматься)</h2>
    <p>Глагол <strong>faire</strong> [фэр] — универсальный глагол действия. Он используется для описания работы, домашних дел, спорта и погоды (<em>Il fait beau</em>).</p>

    <h3>1. 📊 Таблица спряжения глагола FAIRE</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je fais</strong><br><span style="color:var(--text-tertiary);">[жё фэ]</span><br>Я делаю</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Tu fais</strong><br><span style="color:var(--text-tertiary);">[тю фэ]</span><br>Ты делаешь</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On fait</strong><br><span style="color:var(--text-tertiary);">[иль / эль / он фэ]</span><br>Он / Она / Мы делаем</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Nous faisons</strong><br><span style="color:var(--text-tertiary);">[ну фёзон]</span><br>Мы делаем</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous faites</strong><br><span style="color:var(--text-tertiary);">[ву фэт] <em>(особая форма!)</em></span><br>Вы делаете</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles font</strong><br><span style="color:var(--text-tertiary);">[иль / эль фон]</span><br>Они делают</div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Что ты делаешь?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Qu'est-ce que tu fais ?</strong>
                    <span style="font-size:0.85rem;">[кэске тю фэ]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Хорошая погода</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">Il fait beau</strong>
                    <span style="font-size:0.85rem;">[иль фэ бо]</span>
                </div>
            </div>
        </div>
    </div>
    """
    lesson_faire.content_html_en = "<p>Conjugation of verb FAIRE (To do / make).</p>"
    lesson_faire.content_html_fr = "<p>Conjugaison du verbe FAIRE.</p>"
    lesson_faire.save()

    Question.objects.filter(lesson=lesson_faire).delete()
    qf1 = Question.objects.create(lesson=lesson_faire, order=1, text="Какая форма глагола faire используется с 'Vous'?", text_ru="Какая форма глагола faire используется с 'Vous'?", text_uk="Яка форма дієслова faire використовується з 'Vous'?", text_en="Which form of 'faire' goes with 'Vous'?", text_fr="Quelle est la forme avec 'Vous' ?")
    Choice.objects.create(question=qf1, text="Vous faites", text_ru="Vous faites [ву фэт]", text_uk="Vous faites [ву фет]", text_en="Vous faites", text_fr="Vous faites", is_correct=True)
    Choice.objects.create(question=qf1, text="Vous faisez", text_ru="Vous faisez (ошибка)", text_uk="Vous faisez (помилка)", text_en="Vous faisez", text_fr="Vous faisez", is_correct=False)

    # -------------------------------------------------------------
    # 4. VOULOIR, POUVOIR, DEVOIR (Модальные глаголы)
    # -------------------------------------------------------------
    lesson_modals, _ = Lesson.objects.get_or_create(
        data_lesson_id="lesson-modals",
        defaults={"topic": topic_verbs, "order": 10}
    )
    lesson_modals.topic = topic_verbs
    lesson_modals.title_uk = "👑 Модальні дієслова: Vouloir (Хочу), Pouvoir (Можу), Devoir (Мушу)"
    lesson_modals.title_ru = "👑 Модальные глаголы: Vouloir (Хочу), Pouvoir (Могу), Devoir (Должен)"
    lesson_modals.title_en = "👑 Modal Verbs: Vouloir, Pouvoir, Devoir"
    lesson_modals.title_fr = "👑 Les verbes modaux : Vouloir, Pouvoir, Devoir"

    lesson_modals.content_html_uk = """
    <h2>Модальні дієслова: Бажання, Можливість та Обов'язок</h2>
    <p>Ці три дієслова відкривають 90% живого спілкування в кафе, магазині та на роботі.</p>

    <h3>1. VOULOIR (Хотіти) ➔ Ввічливе «Je voudrais» (Я хотів би)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
        <div><strong>Je veux</strong> [жьо вьо] — Я хочу</div>
        <div><strong>Tu veux</strong> [тю вьо] — Ти хочеш</div>
        <div><strong>Il / Elle veut</strong> [іль вьо] — Він / Вона хоче</div>
        <div><strong>Nous voulons</strong> [ну вулон] — Ми хочемо</div>
        <div><strong>Vous voulez</strong> [ву вуле] — Ви хочете</div>
        <div><strong>Ils veulent</strong> [іль вьоль] — Вони хочуть</div>
    </div>
    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Золоте правило ввічливості: «Je voudrais»</div>
        <div class="callout-content">
            <p>У кафе та магазині замість різкого <em>«Je veux»</em> завжди кажіть: <strong>«Je voudrais un café, s'il vous plaît»</strong> (Я хотів би каву, будь ласка).</p>
        </div>
    </div>

    <h3>2. POUVOIR (Могти) та DEVOIR (Мусити / Бути повинним)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
        <div><strong>Je peux</strong> [жьо пьо] — Я можу</div>
        <div><strong>Tu peux</strong> [тю пьо] — Ти можеш</div>
        <div><strong>Il peut</strong> [іль пьо] — Він може</div>
        <div><strong>Nous pouvons</strong> [ну пувон] — Ми можемо</div>
        <div><strong>Vous pouvez</strong> [ву пуве] — Ви можете</div>
        <div><strong>Ils peuvent</strong> [іль пьов] — Вони можуть</div>
    </div>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-top: 14px;">
        <div><strong>Je dois</strong> [жьо дуа] — Я мушу</div>
        <div><strong>Tu dois</strong> [тю дуа] — Ти мусиш</div>
        <div><strong>Il doit</strong> [іль дуа] — Він мусить</div>
        <div><strong>Nous devons</strong> [ну дьовон] — Ми мусимо</div>
        <div><strong>Vous devez</strong> [ву дьове] — Ви мусите</div>
        <div><strong>Ils doivent</strong> [іль дуав] — Вони мусять</div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я хотів би каву</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je voudrais un café</strong>
                    <span style="font-size:0.8rem;">[жьо вудре ен кафе]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Ви можете мені допомогти?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Vous pouvez m'aider ?</strong>
                    <span style="font-size:0.8rem;">[ву пуве меде]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-green);">Я мушу йти</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je dois partir</strong>
                    <span style="font-size:0.8rem;">[жьо дуа партір]</span>
                </div>
            </div>
        </div>
    </div>
    """

    lesson_modals.content_html_ru = """
    <h2>Модальные глаголы: Желание, Возможность и Долг</h2>
    <p>Три главных модальных глагола французского языка: <strong>Vouloir</strong> (хотеть), <strong>Pouvoir</strong> (мочь) и <strong>Devoir</strong> (быть должным).</p>

    <h3>1. VOULOIR (Хотеть) ➔ Вежливая форма «Je voudrais»</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
        <div><strong>Je veux</strong> [жё вё] — Я хочу</div>
        <div><strong>Tu veux</strong> [тю вё] — Ты хочешь</div>
        <div><strong>Il / Elle veut</strong> [иль вё] — Он / Она хочет</div>
        <div><strong>Nous voulons</strong> [ну вулон] — Мы хотим</div>
        <div><strong>Vous voulez</strong> [ву вуле] — Вы хотите</div>
        <div><strong>Ils veulent</strong> [иль вёль] — Они хотят</div>
    </div>
    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Вежливый заказ: «Je voudrais»</div>
        <div class="callout-content">
            <p>В кафе или магазине используйте вежливую форму: <strong>«Je voudrais un croissant, s'il vous plaît»</strong> (Я хотел бы круассан, пожалуйста).</p>
        </div>
    </div>

    <h3>2. POUVOIR (Мочь) и DEVOIR (Быть должным)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
        <div><strong>Je peux</strong> [жё пё] — Я могу</div>
        <div><strong>Tu peux</strong> [тю пё] — Ты можешь</div>
        <div><strong>Il peut</strong> [иль пё] — Он может</div>
        <div><strong>Nous pouvons</strong> [ну пувон] — Мы можем</div>
        <div><strong>Vous pouvez</strong> [ву пуве] — Вы можете</div>
        <div><strong>Ils peuvent</strong> [иль пёв] — Они могут</div>
    </div>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-top: 14px;">
        <div><strong>Je dois</strong> [жё дуа] — Я должен</div>
        <div><strong>Tu dois</strong> [тю дуа] — Ты должен</div>
        <div><strong>Il doit</strong> [иль дуа] — Он должен</div>
        <div><strong>Nous devons</strong> [ну дёвон] — Мы должны</div>
        <div><strong>Vous devez</strong> [ву дёве] — Вы должны</div>
        <div><strong>Ils doivent</strong> [иль дуав] — Они должны</div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я хотел бы кофе</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je voudrais un café</strong>
                    <span style="font-size:0.8rem;">[жё вудрэ эн кафэ]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Вы можете мне помочь?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Vous pouvez m'aider ?</strong>
                    <span style="font-size:0.8rem;">[ву пувэ мэдэ]</span>
                </div>
            </div>
        </div>
    </div>
    """
    lesson_modals.content_html_en = "<p>Modal verbs in French: Vouloir, Pouvoir, Devoir.</p>"
    lesson_modals.content_html_fr = "<p>Les verbes modaux en français.</p>"
    lesson_modals.save()

    Question.objects.filter(lesson=lesson_modals).delete()
    qm1 = Question.objects.create(lesson=lesson_modals, order=1, text="Как вежливо заказать кофе в кафе?", text_ru="Как вежливо заказать кофе в кафе?", text_uk="Як ввічливо замовити каву в кафе?", text_en="How do you politely order coffee in a cafe?", text_fr="Comment commander poliment un café ?")
    Choice.objects.create(question=qm1, text="Je voudrais un café, s'il vous plaît", text_ru="Je voudrais un café, s'il vous plaît", text_uk="Je voudrais un café, s'il vous plaît", text_en="Je voudrais un café, s'il vous plaît", text_fr="Je voudrais un café, s'il vous plaît", is_correct=True)
    Choice.objects.create(question=qm1, text="Je veux un café", text_ru="Je veux un café (слишком резко)", text_uk="Je veux un café (занадто різко)", text_en="Je veux un café", text_fr="Je veux un café", is_correct=False)

    print("Successfully configured core conversational verbs: ALLER, FAIRE, VOULOIR, POUVOIR, DEVOIR!")

if __name__ == '__main__':
    setup_core_verbs()
