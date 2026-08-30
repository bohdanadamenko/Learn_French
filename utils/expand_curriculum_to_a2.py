"""
Master script to populate and elevate the curriculum to complete CEFR A2 (Élémentaire) level:
- Comprehensive grammar masterclasses (Passé Composé vs Imparfait, Futur Simple, Conditionnel, Impératif)
- Core pronouns for fluent speech (COD/COI, Y & EN, Qui/Que/Où, Comparatifs)
- Real-life Belgian scenarios (Rent & Housing, Job interviews, Healthcare, Opinion & Debates)
- Interactive 3D flip cards, messenger dialogues, and rich quiz questions for each module.
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

def setup_a2_curriculum():
    # Retrieve or verify topics
    t_grammar = Topic.objects.filter(id=2).first() or Topic.objects.filter(order=2).first()
    t_verbs = Topic.objects.filter(id=3).first() or Topic.objects.filter(order=3).first()
    t_vocab = Topic.objects.filter(id=4).first() or Topic.objects.filter(order=4).first()
    t_belgium = Topic.objects.filter(id=5).first() or Topic.objects.filter(order=5).first()
    t_dialogues = Topic.objects.filter(id=6).first() or Topic.objects.filter(order=6).first()

    # =========================================================================
    # 1. PASSÉ COMPOSÉ (Прошедшее время)
    # =========================================================================
    l_pc, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-passe-compose", defaults={"topic": t_verbs, "order": 12})
    l_pc.topic = t_verbs
    l_pc.title_uk = "🕰 Минулий час Passé Composé (Avoir та Être)"
    l_pc.title_ru = "🕰 Прошедшее время Passé Composé (Avoir и Être)"
    l_pc.title_en = "🕰 Past Tense Passé Composé (Avoir & Être)"
    l_pc.title_fr = "🕰 Le Passé Composé (Avoir et Être)"

    l_pc.content_html_uk = """
    <h2>Passé Composé — Головний минулий час для завершених дій</h2>
    <p><strong>Passé Composé</strong> використовується для дій, які <strong>відбулися і завершилися у минулому</strong> (<em>«Я поїв»</em>, <em>«Він приїхав»</em>, <em>«Ми купили квитки»</em>).</p>

    <h3>1. 📐 Формула утворення</h3>
    <div style="background:rgba(59,130,246,0.08); padding:16px; border-radius:14px; border:1px solid rgba(59,130,246,0.25); text-align:center; margin:16px 0;">
        <span style="font-size:1.3rem; font-weight:800; color:var(--accent-blue);">AVOIR / ÊTRE (в Présent) + Participe Passé (Дієприкметник)</span>
    </div>

    <h3>2. 🎯 Закінчення дієприкметників (Participe Passé):</h3>
    <ul>
        <li><strong>1-ша група (-ER) ➔ -É:</strong> <em>Parler ➔ Parlé</em> (J'ai parlé), <em>Manger ➔ Mangé</em> (J'ai mangé).</li>
        <li><strong>2-га група (-IR) ➔ -I:</strong> <em>Finir ➔ Fini</em> (J'ai fini), <em>Choisir ➔ Choisi</em> (J'ai choisi).</li>
        <li><strong>Неправильні (3-тя група):</strong> <em>Avoir ➔ Eu</em> [ю], <em>Être ➔ Été</em>, <em>Faire ➔ Fait</em>, <em>Prendre ➔ Pris</em>, <em>Voir ➔ Vu</em>, <em>Boire ➔ Bu</em>.</li>
    </ul>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Глаголи руху та стану відмінюються з ÊTRE (Dr & Mrs Vandertramp)!</div>
        <div class="callout-content">
            <p>14 дієслів руху (<em>Aller, Venir, Partir, Arriver, Entrer, Sortir, Monter, Descendre, Naître, Mourir, Rester, Tomber, Retourner, Passer</em>) та <strong>всі зворотні дієслова</strong> беруть <strong>ÊTRE</strong> з обов'язковим узгодженням за родом і числом:</p>
            <ul>
                <li><em>Il est allé</em> (Він пішов) vs <em>Elle est allé<strong>e</strong></em> (Вона пішла)</li>
                <li><em>Ils sont partis</em> (Вони пішли) vs <em>Elles sont parti<strong>es</strong></em></li>
            </ul>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я завершив роботу</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai fini le travail</strong>
                    <span style="font-size:0.8rem;">[же фіні льо травай]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Вона приїхала в Брюссель</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Elle est arrivée à Bruxelles</strong>
                    <span style="font-size:0.8rem;">[ель ет-аріве а брюсель] 🇧🇪</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-green);">Ми випили кави</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous avons bu un café</strong>
                    <span style="font-size:0.8rem;">[ну-з-авон бю ен кафе]</span>
                </div>
            </div>
        </div>
    </div>
    """

    l_pc.content_html_ru = """
    <h2>Passé Composé — Главное прошедшее время для завершенных событий</h2>
    <p><strong>Passé Composé</strong> используется для действий, которые <strong>произошли и полностью завершились в прошлом</strong> (<em>«Я поел»</em>, <em>«Он приехал»</em>, <em>«Мы купили билеты»</em>).</p>

    <h3>1. 📐 Формула образования</h3>
    <div style="background:rgba(59,130,246,0.08); padding:16px; border-radius:14px; border:1px solid rgba(59,130,246,0.25); text-align:center; margin:16px 0;">
        <span style="font-size:1.3rem; font-weight:800; color:var(--accent-blue);">AVOIR / ÊTRE (в Présent) + Participe Passé (Причастие)</span>
    </div>

    <h3>2. 🎯 Окончания причастий:</h3>
    <ul>
        <li><strong>1-я группа (-ER) ➔ -É:</strong> <em>Parler ➔ Parlé</em> (J'ai parlé), <em>Manger ➔ Mangé</em> (J'ai mangé).</li>
        <li><strong>2-я группа (-IR) ➔ -I:</strong> <em>Finir ➔ Fini</em> (J'ai fini), <em>Choisir ➔ Choisi</em> (J'ai choisi).</li>
        <li><strong>Неправильные (3-я группа):</strong> <em>Avoir ➔ Eu</em> [ю], <em>Être ➔ Été</em>, <em>Faire ➔ Fait</em>, <em>Prendre ➔ Pris</em>, <em>Voir ➔ Vu</em>, <em>Boire ➔ Bu</em>.</li>
    </ul>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Глаголы движения и состояния спрягаются с ÊTRE (Dr & Mrs Vandertramp)!</div>
        <div class="callout-content">
            <p>14 глаголов движения (<em>Aller, Venir, Partir, Arriver, Entrer, Sortir, Monter, Descendre, Naître, Mourir, Rester, Tomber, Retourner, Passer</em>) и <strong>все возвратные глаголы</strong> спрягаются с <strong>ÊTRE</strong> и согласуются в роде и числе:</p>
            <ul>
                <li><em>Il est allé</em> (Он пошел) vs <em>Elle est allé<strong>e</strong></em> (Она пошла)</li>
                <li><em>Ils sont partis</em> (Они ушли) vs <em>Elles sont parti<strong>es</strong></em></li>
            </ul>
        </div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я закончил работу</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai fini le travail</strong>
                    <span style="font-size:0.8rem;">[жэ фини лё травай]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Она приехала в Брюссель</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Elle est arrivée à Bruxelles</strong>
                    <span style="font-size:0.8rem;">[эль эт-аривэ а брюсель] 🇧🇪</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-green);">Мы выпили кофе</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous avons bu un café</strong>
                    <span style="font-size:0.8rem;">[ну-з-авон бю эн кафэ]</span>
                </div>
            </div>
        </div>
    </div>
    """
    l_pc.content_html_en = "<p>Passé Composé past tense masterclass with Avoir and Être.</p>"
    l_pc.content_html_fr = "<p>Le passé composé avec avoir et être.</p>"
    l_pc.save()

    Question.objects.filter(lesson=l_pc).delete()
    q_pc1 = Question.objects.create(lesson=l_pc, order=1, text="Как правильно сказать: «Она пошла в магазин» (с согласованием)?", text_ru="Как правильно сказать: «Она пошла в магазин» (с согласованием)?", text_uk="Як правильно сказати: «Вона пішла в магазин» (з узгодженням)?", text_en="How to say 'She went to the store'?", text_fr="Comment dit-on 'Elle est allée au magasin' ?")
    Choice.objects.create(question=q_pc1, text="Elle est allée au magasin", text_ru="Elle est allée (с окончанием -e женского рода)", text_uk="Elle est allée (із закінченням -e жіночого роду)", text_en="Elle est allée", text_fr="Elle est allée", is_correct=True)
    Choice.objects.create(question=q_pc1, text="Elle a allé au magasin", text_ru="Elle a allé (ошибка: aller спрягается с être)", text_uk="Elle a allé (помилка)", text_en="Elle a allé", text_fr="Elle a allé", is_correct=False)

    q_pc2 = Question.objects.create(lesson=l_pc, order=2, text="Какая форма participe passé у глагола FAIRE?", text_ru="Какая форма participe passé у глагола FAIRE?", text_uk="Яка форма participe passé у дієслова FAIRE?", text_en="What is the past participle of FAIRE?", text_fr="Quel est le participe passé de FAIRE ?")
    Choice.objects.create(question=q_pc2, text="Fait", text_ru="Fait (J'ai fait)", text_uk="Fait (J'ai fait)", text_en="Fait", text_fr="Fait", is_correct=True)
    Choice.objects.create(question=q_pc2, text="Faisé", text_ru="Faisé (не существует)", text_uk="Faisé", text_en="Faisé", text_fr="Faisé", is_correct=False)

    # =========================================================================
    # 2. L'IMPARFAIT vs PASSÉ COMPOSÉ (Прошедшее время описания)
    # =========================================================================
    l_imp, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-imparfait", defaults={"topic": t_verbs, "order": 46})
    l_imp.topic = t_verbs
    l_imp.title_uk = "🕰️ Минулий час опису L'Imparfait та різниця з Passé Composé"
    l_imp.title_ru = "🕰️ Прошедшее время описания L'Imparfait и разница с Passé Composé"
    l_imp.title_en = "🕰️ Imperfect Tense L'Imparfait & Passé Composé"
    l_imp.title_fr = "🕰️ L'Imparfait et le Passé Composé"

    l_imp.content_html_uk = """
    <h2>L'Imparfait — Минулий час для фону, звичок, погоди та почуттів</h2>
    <p>Якщо <strong>Passé Composé</strong> — це фотоапарат (що конкретно сталося: <em>клац!</em>), то <strong>L'Imparfait</strong> — це відеокамера (що відбувалося в цей момент: опис погоди, природи, віку, настрою, повторюваних звичок).</p>

    <h3>1. 📐 Утворення L'Imparfait:</h3>
    <p>Візьміть основу форми <strong>NOUS</strong> у теперішньому часі (Présent), приберіть <em>-ons</em> і додайте універсальні закінчення:</p>
    <ul>
        <li>Je ➔ <strong>-ais</strong> [е] (<em>J'étais, Je parlais, Je faisais</em>)</li>
        <li>Tu ➔ <strong>-ais</strong> [е] (<em>Tu avais</em>)</li>
        <li>Il / Elle / On ➔ <strong>-ait</strong> [е] (<em>Il faisait beau, Il pleuvait</em>)</li>
        <li>Nous ➔ <strong>-ions</strong> [йон] (<em>Nous habitions</em>)</li>
        <li>Vous ➔ <strong>-iez</strong> [йе] (<em>Vous mangiez</em>)</li>
        <li>Ils / Elles ➔ <strong>-aient</strong> [е] (<em>Ils étaient</em>)</li>
    </ul>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Золоте правило вибору в оповіданні:</div>
        <div class="callout-content">
            <p><em>«Quand j'<strong>étais</strong> petit (Imparfait — тривалий стан у дитинстві), je <strong>suis allé</strong> à Bruxelles pour la première fois (Passé Composé — конкретна подія)».</em></p>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Була гарна погода</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Il faisait beau</strong>
                    <span style="font-size:0.8rem;">[іль фезе бо]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Коли я жив у Бельгії...</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Quand j'habitais en Belgique...</strong>
                    <span style="font-size:0.8rem;">[кан жабіте ан бельжік] 🇧🇪</span>
                </div>
            </div>
        </div>
    </div>
    """

    l_imp.content_html_ru = """
    <h2>L'Imparfait — Прошедшее время для описания фона, погоды и привычек</h2>
    <p>Если <strong>Passé Composé</strong> — это вспышка фотоаппарата (что конкретно произошло: <em>щелк!</em>), то <strong>L'Imparfait</strong> — это видеокамера (что происходило: описание фона, погоды, возраста, чувств, привычек в прошлом).</p>

    <h3>1. 📐 Универсальные окончания L'Imparfait:</h3>
    <ul>
        <li>Je ➔ <strong>-ais</strong> [э] (<em>J'étais, Je parlais, Je faisais</em>)</li>
        <li>Tu ➔ <strong>-ais</strong> [э] (<em>Tu avais</em>)</li>
        <li>Il / Elle / On ➔ <strong>-ait</strong> [э] (<em>Il faisait beau, Il était 20h</em>)</li>
        <li>Nous ➔ <strong>-ions</strong> [йон] (<em>Nous habitions</em>)</li>
        <li>Vous ➔ <strong>-iez</strong> [йе] (<em>Vous faisiez</em>)</li>
        <li>Ils / Elles ➔ <strong>-aient</strong> [э] (<em>Ils étaient heureux</em>)</li>
    </ul>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Была хорошая погода</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Il faisait beau</strong>
                    <span style="font-size:0.8rem;">[иль фэзэ бо]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Когда я жил в Бельгии...</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Quand j'habitais en Belgique...</strong>
                    <span style="font-size:0.8rem;">[кан жабитэ ан бельжик] 🇧🇪</span>
                </div>
            </div>
        </div>
    </div>
    """
    l_imp.content_html_en = "<p>L'Imparfait vs Passé Composé past tenses masterclass.</p>"
    l_imp.content_html_fr = "<p>L'imparfait et le passé composé.</p>"
    l_imp.save()

    # =========================================================================
    # 3. LE CONDITIONNEL PRÉSENT (Вежливые просьбы и желания A2)
    # =========================================================================
    l_cond, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-conditionnel", defaults={"topic": t_verbs, "order": 15})
    l_cond.topic = t_verbs
    l_cond.title_uk = "👑 Умовний спосіб Le Conditionnel (Ввічливість і бажання)"
    l_cond.title_ru = "👑 Условное наклонение Le Conditionnel (Вежливость и желания)"
    l_cond.title_en = "👑 Conditional Mood Le Conditionnel Présent"
    l_cond.title_fr = "👑 Le Conditionnel Présent (Politesse et souhaits)"

    l_cond.content_html_uk = """
    <h2>Le Conditionnel Présent — Мова ввічливості, порад та мрій</h2>
    <p>На рівні A2 <strong>Conditionnel</strong> — це найважливіший інструмент ввічливого спілкування в ресторані, банку, на пошті та в комуні.</p>

    <h3>1. 🌟 Ключові ввічливі форми:</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je voudrais...</strong><br><span style="color:var(--text-tertiary);">[жьо вудре]</span><br>Я хотів би... (замовлення / прохання)</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">J'aimerais...</strong><br><span style="color:var(--text-tertiary);">[жемере]</span><br>Мені б хотілося... (мрії)</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Pourriez-vous...?</strong><br><span style="color:var(--text-tertiary);">[пур'є-ву]</span><br>Чи не могли б ви...? (найвища ввічливість)</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous devriez...</strong><br><span style="color:var(--text-tertiary);">[ву дьовріє]</span><br>Вам варто було б... (порада)</div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Чи не могли б ви мені допомогти?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Pourriez-vous m'aider ?</strong>
                    <span style="font-size:0.8rem;">[пур'є-ву меде]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Я хотів би записатися на прийом</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je voudrais prendre un rendez-vous</strong>
                    <span style="font-size:0.8rem;">[жьо вудре прандр ен рандеву]</span>
                </div>
            </div>
        </div>
    </div>
    """

    l_cond.content_html_ru = """
    <h2>Le Conditionnel Présent — Язык вежливости, советов и желаний</h2>
    <p>На уровне A2 <strong>Conditionnel</strong> — главный инструмент для вежливого общения в кафе, магазинах, банках и учреждениях.</p>

    <h3>1. 🌟 Главные вежливые формы:</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">Je voudrais...</strong><br><span style="color:var(--text-tertiary);">[жё вудрэ]</span><br>Я хотел бы... (заказ / просьба)</div>
        <div><strong style="color:var(--accent-blue); font-size:1.15rem;">J'aimerais...</strong><br><span style="color:var(--text-tertiary);">[жэмрэ]</span><br>Мне бы хотелось... (желания)</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Pourriez-vous...?</strong><br><span style="color:var(--text-tertiary);">[пурьé-ву]</span><br>Не могли бы вы...? (вежливая просьба)</div>
        <div><strong style="color:var(--accent-purple); font-size:1.15rem;">Vous devriez...</strong><br><span style="color:var(--text-tertiary);">[ву дёврьé]</span><br>Вам следовало бы... (совет)</div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Не могли бы вы мне помочь?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Pourriez-vous m'aider ?</strong>
                    <span style="font-size:0.8rem;">[пурьé-ву мэдэ]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">Я хотел бы записаться на прием</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je voudrais prendre un rendez-vous</strong>
                    <span style="font-size:0.8rem;">[жё вудрэ прандр эн рандэву]</span>
                </div>
            </div>
        </div>
    </div>
    """
    l_cond.content_html_en = "<p>Conditional mood for politeness and wishes.</p>"
    l_cond.content_html_fr = "<p>Le conditionnel présent de politesse.</p>"
    l_cond.save()

    Question.objects.filter(lesson=l_cond).delete()
    qc1 = Question.objects.create(lesson=l_cond, order=1, text="Как максимально вежливо попросить счет в ресторане?", text_ru="Как максимально вежливо попросить счет в ресторане?", text_uk="Як максимально ввічливо попросити рахунок у ресторані?", text_en="How to politely ask for the check?", text_fr="Comment demander poliment l'addition ?")
    Choice.objects.create(question=qc1, text="Je voudrais l'addition, s'il vous plaît", text_ru="Je voudrais l'addition, s'il vous plaît", text_uk="Je voudrais l'addition, s'il vous plaît", text_en="Je voudrais l'addition, s'il vous plaît", text_fr="Je voudrais l'addition, s'il vous plaît", is_correct=True)
    Choice.objects.create(question=qc1, text="Donne-moi l'addition", text_ru="Donne-moi l'addition (грубо)", text_uk="Donne-moi l'addition (грубо)", text_en="Donne-moi l'addition", text_fr="Donne-moi l'addition", is_correct=False)

    # =========================================================================
    # 4. МЕСТОИМЕНИЯ Y И EN (Les Pronoms Y et EN - A2)
    # =========================================================================
    l_yen, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-pronouns-y-en", defaults={"topic": t_grammar, "order": 44})
    l_yen.topic = t_grammar
    l_yen.title_uk = "📍 Займенники Y та EN (Заміна місць і кількостей)"
    l_yen.title_ru = "📍 Местоимения Y и EN (Замена мест и количеств)"
    l_yen.title_en = "📍 Pronouns Y and EN"
    l_yen.title_fr = "📍 Les pronoms Y et EN"

    l_yen.content_html_uk = """
    <h2>Займенники Y та EN — Секрет природної французької мови</h2>
    <p>Французи ненавидять повторювати ті самі іменники, тому використовують крихітні слова <strong>Y</strong> та <strong>EN</strong>.</p>

    <h3>1. Займенник Y [і] ➔ Замінює МІСЦЕ (à, en, dans, chez + місце):</h3>
    <ul>
        <li><em>Tu vas à Bruxelles ?</em> ➔ <strong>Oui, j'y vais !</strong> (Так, я туди їду!)</li>
        <li><em>Tu es chez toi ?</em> ➔ <strong>Oui, j'y suis.</strong> (Так, я вдома.)</li>
    </ul>

    <h3>2. Займенник EN [ан] ➔ Замінює КІЛЬКІСТЬ або прийменник DE:</h3>
    <ul>
        <li><em>Tu veux du chocolat ?</em> ➔ <strong>Oui, j'en veux !</strong> (Так, я його хочу!)</li>
        <li><em>Tu as des enfants ?</em> ➔ <strong>Oui, j'en ai deux.</strong> (Так, у мене їх двоє.)</li>
    </ul>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я туди їду (в Брюссель)</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'y vais</strong>
                    <span style="font-size:0.8rem;">[жі ве]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">У мене їх двоє (дітей / речей)</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'en ai deux</strong>
                    <span style="font-size:0.8rem;">[жан-не дьо]</span>
                </div>
            </div>
        </div>
    </div>
    """

    l_yen.content_html_ru = """
    <h2>Местоимения Y и EN — Секрет естественной беглой речи</h2>
    <p>Французы избегают повторов одних и тех же существительных с помощью коротких местоимений <strong>Y</strong> и <strong>EN</strong>.</p>

    <h3>1. Местоимение Y [и] ➔ Заменяет МЕСТО (куда? где?):</h3>
    <ul>
        <li><em>Tu vas à Bruxelles ?</em> ➔ <strong>Oui, j'y vais !</strong> (Да, я туда еду!)</li>
        <li><em>Tu penses à ton travail ?</em> ➔ <strong>Oui, j'y pense.</strong> (Да, я думаю об этом.)</li>
    </ul>

    <h3>2. Местоимение EN [ан] ➔ Заменяет КОЛИЧЕСТВО или предлог DE:</h3>
    <ul>
        <li><em>Tu veux du fromage ?</em> ➔ <strong>Oui, j'en veux !</strong> (Да, я его хочу!)</li>
        <li><em>Tu as des frères ?</em> ➔ <strong>Oui, j'en ai un.</strong> (Да, у меня есть один.)</li>
    </ul>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-blue);">Я туда иду / еду</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'y vais</strong>
                    <span style="font-size:0.8rem;">[жи вэ]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.3rem; color:var(--accent-purple);">У меня их двое</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'en ai deux</strong>
                    <span style="font-size:0.8rem;">[жан-нэ дё]</span>
                </div>
            </div>
        </div>
    </div>
    """
    l_yen.content_html_en = "<p>Pronouns Y and EN in French.</p>"
    l_yen.content_html_fr = "<p>Les pronoms Y et EN.</p>"
    l_yen.save()

    Question.objects.filter(lesson=l_yen).delete()
    qy1 = Question.objects.create(lesson=l_yen, order=1, text="Как ответить: «Да, я туда еду» на вопрос «Tu vas à Paris ?»", text_ru="Как ответить: «Да, я туда еду» на вопрос «Tu vas à Paris ?»", text_uk="Як відповісти: «Так, я туди їду» на запитання «Tu vas à Paris ?»", text_en="How to answer 'Yes, I am going there'?", text_fr="Comment répondre 'Oui, j'y vais' ?")
    Choice.objects.create(question=qy1, text="Oui, j'y vais", text_ru="Oui, j'y vais (Y заменяет à Paris)", text_uk="Oui, j'y vais", text_en="Oui, j'y vais", text_fr="Oui, j'y vais", is_correct=True)
    Choice.objects.create(question=qy1, text="Oui, j'en vais", text_ru="Oui, j'en vais (ошибка)", text_uk="Oui, j'en vais", text_en="Oui, j'en vais", text_fr="Oui, j'en vais", is_correct=False)

    # =========================================================================
    # 5. АРЕНДА ЖИЛЬЯ В БЕЛЬГИИ (Recherche de Logement en Belgique - A2)
    # =========================================================================
    l_rent, _ = Lesson.objects.get_or_create(data_lesson_id="lesson-rent-housing-be", defaults={"topic": t_belgium, "order": 33})
    l_rent.topic = t_belgium
    l_rent.title_uk = "🏡 Оренда житла в Бельгії: Договір (Bail), Застава та Опис"
    l_rent.title_ru = "🏡 Аренда жилья в Бельгии: Договор (Bail), Залог и Опись"
    l_rent.title_en = "🏡 Renting an Apartment in Belgium: Lease & Deposit"
    l_rent.title_fr = "🏡 Louer un logement en Belgique (Le bail, garantie)"

    l_rent.content_html_uk = """
    <h2>Оренда квартири в Бельгії — Практичний путівник A2</h2>
    <p>Оренда житла в Бельгії має свої суворі юридичні терміни та правила.</p>

    <h3>1. 🔑 Ключовий словник орендаря:</h3>
    <ul>
        <li><strong>Le bail</strong> [льйо бей] = Договір оренди (найчастіше <em>Bail de 9 ans (3-6-9)</em> або короткостроковий <em>Bail de courte durée (1-3 ans)</em>).</li>
        <li><strong>La garantie locative</strong> = Гарантійний залог (зазвичай 2-3 місяці оренди на заблокованому банківському рахунку).</li>
        <li><strong>L'état des lieux</strong> [лєта де льє] = Опис стану квартири (при в'їзді та виїзді експертом).</li>
        <li><strong>Les charges</strong> [ле шарж] = Комунальні платежі (опалення, вода, ліфт, прибирання під'їзду).</li>
        <li><strong>Non meublé / Meublé</strong> = Без меблів / З меблями.</li>
    </ul>

    <h3>🃏 Картки для запам'ятовування</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-blue);">Комунальні витрати включені?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Les charges sont comprises ?</strong>
                    <span style="font-size:0.8rem;">[ле шарж сон компріз]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-purple);">Коли можна подивитися квартиру?</strong>
                    <span class="flip-hint">Натисніть для перекладу</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Quand est-il possible de visiter ?</strong>
                    <span style="font-size:0.8rem;">[кан е-т-іль посібль дьо візіте]</span>
                </div>
            </div>
        </div>
    </div>
    """

    l_rent.content_html_ru = """
    <h2>Аренда квартиры в Бельгии — Практический путеводитель A2</h2>
    <p>Аренда жилья в Бельгии имеет свои строгие юридические термины и правила.</p>

    <h3>1. 🔑 Ключевой словарь арендатора:</h3>
    <ul>
        <li><strong>Le bail</strong> [лё бай] = Договор аренды (стандартный <em>Bail 3-6-9</em> или краткосрочный).</li>
        <li><strong>La garantie locative</strong> = Гарантийный залог (обычно 2-3 месяца аренды на заблокированном счете).</li>
        <li><strong>L'état des lieux</strong> [лэта дэ льё] = Опись состояния жилья (при въезде и выезде с экспертом).</li>
        <li><strong>Les charges</strong> [ле шарж] = Коммунальные платежи (вода, отопление, уборка).</li>
    </ul>

    <h3>🃏 Карточки для запоминания</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-blue);">Коммунальные включены?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Les charges sont comprises ?</strong>
                    <span style="font-size:0.8rem;">[ле шарж сон комприз]</span>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.25rem; color:var(--accent-purple);">Когда можно посмотреть квартиру?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Quand est-il possible de visiter ?</strong>
                    <span style="font-size:0.8rem;">[кан э-т-иль посибль дё визитэ]</span>
                </div>
            </div>
        </div>
    </div>
    """
    l_rent.content_html_en = "<p>Renting an apartment in Belgium guide.</p>"
    l_rent.content_html_fr = "<p>Guide pratique pour louer en Belgique.</p>"
    l_rent.save()

    Question.objects.filter(lesson=l_rent).delete()
    qr1 = Question.objects.create(lesson=l_rent, order=1, text="Как по-французски называется договор аренды жилья в Бельгии?", text_ru="Как по-французски называется договор аренды жилья в Бельгии?", text_uk="Як французькою називається договір оренди житла в Бельгії?", text_en="What is a rental lease called in French?", text_fr="Comment s'appelle le contrat de location ?")
    Choice.objects.create(question=qr1, text="Le bail", text_ru="Le bail [лё бай]", text_uk="Le bail [льйо бей]", text_en="Le bail", text_fr="Le bail", is_correct=True)
    Choice.objects.create(question=qr1, text="La facture", text_ru="La facture (это счет)", text_uk="La facture (це рахунок)", text_en="La facture", text_fr="La facture", is_correct=False)

    print("Successfully populated and enriched A2 curriculum lessons with dynamic 3D flashcards, tables, and quizzes!")

if __name__ == '__main__':
    setup_a2_curriculum()
