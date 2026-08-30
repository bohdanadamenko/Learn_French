"""
Script to update Lesson 3: Verbe Être (быть / бути) with rich interactive components:
- Full conjugation table with TTS audio buttons and liaison cues
- Interactive Flashcards (флеш-карточки / flip cards) for rapid self-testing
- Callout tips (💡 мнемоника и связывание, ⚠️ обязательность связки, 🇧🇪 бельгийский контекст)
- Dialogue in messenger bubbles
- 3 comprehensive quiz questions
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

def update_etre_lesson():
    lesson = Lesson.objects.filter(data_lesson_id="lesson3").first()
    if not lesson:
        print("Lesson 3 not found!")
        return

    lesson.title_ru = "📝 Глагол être (быть / являться)"
    lesson.title_uk = "📝 Дієслово être (бути / являтися)"
    lesson.title_en = "📝 Verb être (to be)"
    lesson.title_fr = "📝 Le verbe être (au présent)"

    # --- UKRAINIAN CONTENT ---
    lesson.content_html_uk = """
    <h2>Дієслово ÊTRE (Бути) — Головний фундамент французької мови</h2>
    <p>Дієслово <strong>être</strong> [етр] — найважливіше дієслово у французькій мові. Воно використовується, щоб назвати професію, національність, описати стан чи місцеперебування.</p>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Головне правило: дієслово ніколи не опускається!</div>
        <div class="callout-content">
            <p>В українській мові ми можемо сказати: <em>«Я студент»</em> або <em>«Він у Брюсселі»</em>. У французькій мові дієслово-зв'язка <strong>обов'язкове</strong>:</p>
            <p>❌ <em>Je étudiant</em> &nbsp; ➔ &nbsp; ✅ <strong>Je <span style="color:var(--accent-blue)">suis</span> étudiant</strong>.</p>
        </div>
    </div>

    <h3>1. 📊 Повна таблиця відмінювання (Présent de l'indicatif)</h3>
    <p>Натискайте 🔊 біля кожної форми, щоб почути точну французьку вимову:</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px;">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Je suis</strong>
                <button class="audio-play-btn" data-speak="Je suis" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[жьо сюі]</span><br>
            <span>Я є / Я знаходжуся</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Tu es</strong>
                <button class="audio-play-btn" data-speak="Tu es" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[тю е]</span><br>
            <span>Ти є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On est</strong>
                <button class="audio-play-btn" data-speak="Il est, elle est, on est" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[іль / ель / он е]</span><br>
            <span>Він / Вона / Ми є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Nous sommes</strong>
                <button class="audio-play-btn" data-speak="Nous sommes" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ну сом]</span><br>
            <span>Ми є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">êtes</span></strong>
                <button class="audio-play-btn" data-speak="Vous êtes" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ву-з-ет] <em>(зв'язування [z])</em></span><br>
            <span>Ви є (ввічливо або множина)</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles sont</strong>
                <button class="audio-play-btn" data-speak="Ils sont, elles sont" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[іль / ель сон]</span><br>
            <span>Вони є</span>
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Секрет вимови: Обов'язкове зв'язування (Liaison)</div>
        <div class="callout-content">
            <p>У формі <strong>Vous êtes</strong> кінцева немовляча <em>s</em> перед голосною <em>ê</em> перетворюється на дзвінкий звук <strong>[z]</strong>: <em>«Вуз-ет»</em> <button class="audio-play-btn" data-speak="Vous êtes">🔊</button>.</p>
            <p>У формі <strong>Ils sont</strong> кінцева <em>s</em> залишається глухим звуком <strong>[s]</strong>: <em>«Іль сон»</em> <button class="audio-play-btn" data-speak="Ils sont">🔊</button>.</p>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <p>Натискайте на картку, щоб перевернути її та перевірити свої знання:</p>

    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Я в Брюсселі</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je suis à Bruxelles</strong>
                    <span style="font-size:0.8rem;">[жьо сюі а брюсель] 🇧🇪</span>
                    <button class="audio-play-btn" data-speak="Je suis à Bruxelles" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Ви готові?</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Vous êtes prêts ?</strong>
                    <span style="font-size:0.8rem;">[вуз-ет пре]</span>
                    <button class="audio-play-btn" data-speak="Vous êtes prêts ?" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-green);">Ми щасливі</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous sommes heureux</strong>
                    <span style="font-size:0.8rem;">[ну сом з-ере]</span>
                    <button class="audio-play-btn" data-speak="Nous sommes heureux" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:#EA580C;">Це чудово!</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">C'est super ! / C'est bon</strong>
                    <span style="font-size:0.8rem;">(C'est = Ce + est)</span>
                    <button class="audio-play-btn" data-speak="C'est super ! C'est bon !" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
    </div>

    <h3>3. 🗣️ Живий діалог: Де ти знаходишся?</h3>
    <div class="dialogue-container">
        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">👨‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Лука</div>
                <div class="dialogue-french">
                    Allô Claire ! Où es-tu ?
                    <button class="audio-play-btn" data-speak="Allô Claire ! Où es-tu ?">🔊</button>
                </div>
                <div class="dialogue-trans">Алло, Клер! Де ти є?</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-b">
            <div class="dialogue-avatar">👩‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Клер</div>
                <div class="dialogue-french">
                    Je suis à la Grand-Place avec Marc ! Nous sommes au café.
                    <button class="audio-play-btn" data-speak="Je suis à la Grand-Place avec Marc ! Nous sommes au café.">🔊</button>
                </div>
                <div class="dialogue-trans">Я на Гран-Плас із Марком! Ми в кафе.</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">👨‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Лука</div>
                <div class="dialogue-french">
                    Super ! J'arrive, je suis tout près !
                    <button class="audio-play-btn" data-speak="Super ! J'arrive, je suis tout près !">🔊</button>
                </div>
                <div class="dialogue-trans">Супер! Я вже йду, я зовсім поруч!</div>
            </div>
        </div>
    </div>
    """

    # --- RUSSIAN CONTENT ---
    lesson.content_html_ru = """
    <h2>Глагол ÊTRE (Быть / Являться / Находиться)</h2>
    <p>Глагол <strong>être</strong> [этр] — абсолютная основа французского языка. С его помощью называют имя, профессию, национальность, чувства и местоположение.</p>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Французы никогда не опускают глагол быть!</div>
        <div class="callout-content">
            <p>В русском языке мы говорим: <em>«Я студент»</em> или <em>«Они дома»</em>. Во французском связка <strong>обязательна</strong>:</p>
            <p>❌ <em>Je étudiant</em> &nbsp; ➔ &nbsp; ✅ <strong>Je <span style="color:var(--accent-blue)">suis</span> étudiant</strong>.</p>
        </div>
    </div>

    <h3>1. 📊 Таблица спряжения в настоящем времени (Présent)</h3>
    <p>Нажимайте 🔊 рядом с любой строкой для идеального французского произношения:</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px;">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Je suis</strong>
                <button class="audio-play-btn" data-speak="Je suis" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[жё сюи]</span><br>
            <span>Я есть / Я нахожусь</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Tu es</strong>
                <button class="audio-play-btn" data-speak="Tu es" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[тю э]</span><br>
            <span>Ты есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On est</strong>
                <button class="audio-play-btn" data-speak="Il est, elle est, on est" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[иль / эль / он э]</span><br>
            <span>Он / Она есть / Мы есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Nous sommes</strong>
                <button class="audio-play-btn" data-speak="Nous sommes" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ну сом]</span><br>
            <span>Мы есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">êtes</span></strong>
                <button class="audio-play-btn" data-speak="Vous êtes" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ву-з-эт] <em>(связывание [z])</em></span><br>
            <span>Вы есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles sont</strong>
                <button class="audio-play-btn" data-speak="Ils sont, elles sont" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[иль / эль сон]</span><br>
            <span>Они есть</span>
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Секрет связывания (Liaison)</div>
        <div class="callout-content">
            <p>В форме <strong>Vous êtes</strong> буква <em>s</em> соединяется со следующим словом со звуком <strong>[z]</strong>: <em>«Вуз-эт»</em> <button class="audio-play-btn" data-speak="Vous êtes">🔊</button>.</p>
        </div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <p>Нажмите на карточку, чтобы перевернуть её и узнать перевод и звучание:</p>

    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Я в Брюсселе</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Je suis à Bruxelles</strong>
                    <span style="font-size:0.8rem;">[жё сюи а брюсель] 🇧🇪</span>
                    <button class="audio-play-btn" data-speak="Je suis à Bruxelles" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Вы готовы?</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Vous êtes prêts ?</strong>
                    <span style="font-size:0.8rem;">[вуз-эт прэ]</span>
                    <button class="audio-play-btn" data-speak="Vous êtes prêts ?" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-green);">Мы счастливы</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous sommes heureux</strong>
                    <span style="font-size:0.8rem;">[ну сом з-ёрё]</span>
                    <button class="audio-play-btn" data-speak="Nous sommes heureux" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:#EA580C;">Это отлично!</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.1rem;">C'est super ! / C'est bon</strong>
                    <span style="font-size:0.8rem;">(C'est = Ce + est)</span>
                    <button class="audio-play-btn" data-speak="C'est super ! C'est bon !" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
    </div>

    <h3>3. 🗣️ Живой диалог: Где ты?</h3>
    <div class="dialogue-container">
        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">👨‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Люка</div>
                <div class="dialogue-french">
                    Allô Claire ! Où es-tu ?
                    <button class="audio-play-btn" data-speak="Allô Claire ! Où es-tu ?">🔊</button>
                </div>
                <div class="dialogue-trans">Алло, Клер! Где ты находишься?</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-b">
            <div class="dialogue-avatar">👩‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Клер</div>
                <div class="dialogue-french">
                    Je suis à la Grand-Place avec Marc ! Nous sommes au café.
                    <button class="audio-play-btn" data-speak="Je suis à la Grand-Place avec Marc ! Nous sommes au café.">🔊</button>
                </div>
                <div class="dialogue-trans">Я на Гран-Плас с Марком! Мы в кафе.</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">👨‍💼</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Люка</div>
                <div class="dialogue-french">
                    Super ! J'arrive, je suis tout près !
                    <button class="audio-play-btn" data-speak="Super ! J'arrive, je suis tout près !">🔊</button>
                </div>
                <div class="dialogue-trans">Супер! Уже иду, я совсем рядом!</div>
            </div>
        </div>
    </div>
    """

    # --- ENGLISH CONTENT ---
    lesson.content_html_en = """
    <h2>Verb ÊTRE (To be) — The Core of French</h2>
    <p>The verb <strong>être</strong> is essential in French to describe names, professions, feelings, and locations.</p>

    <h3>1. Full Conjugation Table (Present)</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
        <div><strong>Je suis</strong> <button class="audio-play-btn" data-speak="Je suis">🔊</button><br>I am</div>
        <div><strong>Tu es</strong> <button class="audio-play-btn" data-speak="Tu es">🔊</button><br>You are</div>
        <div><strong>Il / Elle / On est</strong> <button class="audio-play-btn" data-speak="Il est, elle est, on est">🔊</button><br>He / She / One is</div>
        <div><strong>Nous sommes</strong> <button class="audio-play-btn" data-speak="Nous sommes">🔊</button><br>We are</div>
        <div><strong>Vous êtes</strong> <button class="audio-play-btn" data-speak="Vous êtes">🔊</button><br>You are (formal/plural)</div>
        <div><strong>Ils / Elles sont</strong> <button class="audio-play-btn" data-speak="Ils sont, elles sont">🔊</button><br>They are</div>
    </div>

    <h3>2. 🃏 Interactive Flashcards</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong>I am in Brussels</strong>
                    <span class="flip-hint">Click to flip</span>
                </div>
                <div class="flip-card-back">
                    <strong>Je suis à Bruxelles</strong>
                    <button class="audio-play-btn" data-speak="Je suis à Bruxelles">🔊</button>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong>You are ready</strong>
                    <span class="flip-hint">Click to flip</span>
                </div>
                <div class="flip-card-back">
                    <strong>Vous êtes prêts</strong>
                    <button class="audio-play-btn" data-speak="Vous êtes prêts">🔊</button>
                </div>
            </div>
        </div>
    </div>
    """

    # --- FRENCH CONTENT ---
    lesson.content_html_fr = """
    <h2>Le verbe ÊTRE au présent</h2>
    <p>Le verbe <strong>être</strong> est l'un des verbes les plus importants de la langue française.</p>

    <h3>Conjugaison :</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
        <div><strong>Je suis</strong> <button class="audio-play-btn" data-speak="Je suis">🔊</button></div>
        <div><strong>Tu es</strong> <button class="audio-play-btn" data-speak="Tu es">🔊</button></div>
        <div><strong>Il / Elle / On est</strong> <button class="audio-play-btn" data-speak="Il est">🔊</button></div>
        <div><strong>Nous sommes</strong> <button class="audio-play-btn" data-speak="Nous sommes">🔊</button></div>
        <div><strong>Vous êtes</strong> <button class="audio-play-btn" data-speak="Vous êtes">🔊</button></div>
        <div><strong>Ils / Elles sont</strong> <button class="audio-play-btn" data-speak="Ils sont">🔊</button></div>
    </div>
    """

    lesson.save()
    print("Lesson 3 (être) updated successfully with conjugation, audio buttons, and interactive flashcards!")

    # --- QUIZ QUESTIONS ---
    Question.objects.filter(lesson=lesson).delete()

    q1 = Question.objects.create(
        lesson=lesson,
        order=1,
        text="Как правильно сказать: «Я в Брюсселе»?",
        text_ru="Как правильно сказать: «Я в Брюсселе»?",
        text_uk="Як правильно сказати: «Я в Брюсселі»?",
        text_en="How do you say: 'I am in Brussels' in French?",
        text_fr="Comment dit-on 'Je suis à Bruxelles' ?"
    )
    Choice.objects.create(question=q1, text="Je suis à Bruxelles", text_ru="Je suis à Bruxelles", text_uk="Je suis à Bruxelles", text_en="Je suis à Bruxelles", text_fr="Je suis à Bruxelles", is_correct=True)
    Choice.objects.create(question=q1, text="Je à Bruxelles", text_ru="Je à Bruxelles (без глагола)", text_uk="Je à Bruxelles (без дієслова)", text_en="Je à Bruxelles", text_fr="Je à Bruxelles", is_correct=False)
    Choice.objects.create(question=q1, text="J'ai à Bruxelles", text_ru="J'ai à Bruxelles", text_uk="J'ai à Bruxelles", text_en="J'ai à Bruxelles", text_fr="J'ai à Bruxelles", is_correct=False)

    q2 = Question.objects.create(
        lesson=lesson,
        order=2,
        text="Какая форма глагола être используется с местоимением 'Vous'?",
        text_ru="Какая форма глагола être используется с местоимением 'Vous'?",
        text_uk="Яка форма дієслова être використовується із займенником 'Vous'?",
        text_en="Which form of 'être' goes with 'Vous'?",
        text_fr="Quelle est la forme du verbe être avec 'Vous' ?"
    )
    Choice.objects.create(question=q2, text="Vous êtes", text_ru="Vous êtes [вуз-эт]", text_uk="Vous êtes [вуз-ет]", text_en="Vous êtes", text_fr="Vous êtes", is_correct=True)
    Choice.objects.create(question=q2, text="Vous avez", text_ru="Vous avez [вуз-аве] (это глагол avoir)", text_uk="Vous avez (це дієслово avoir)", text_en="Vous avez", text_fr="Vous avez", is_correct=False)
    Choice.objects.create(question=q2, text="Vous sont", text_ru="Vous sont", text_uk="Vous sont", text_en="Vous sont", text_fr="Vous sont", is_correct=False)

    q3 = Question.objects.create(
        lesson=lesson,
        order=3,
        text="Как сказать: «Мы в кафе»?",
        text_ru="Как сказать: «Мы в кафе»?",
        text_uk="Як сказати: «Ми в кафе»?",
        text_en="How do you say: 'We are at the cafe'?",
        text_fr="Comment dit-on 'Nous sommes au café' ?"
    )
    Choice.objects.create(question=q3, text="Nous sommes au café", text_ru="Nous sommes au café", text_uk="Nous sommes au café", text_en="Nous sommes au café", text_fr="Nous sommes au café", is_correct=True)
    Choice.objects.create(question=q3, text="Nous est au café", text_ru="Nous est au café", text_uk="Nous est au café", text_en="Nous est au café", text_fr="Nous est au café", is_correct=False)
    Choice.objects.create(question=q3, text="Nous ont au café", text_ru="Nous ont au café", text_uk="Nous ont au café", text_en="Nous ont au café", text_fr="Nous ont au café", is_correct=False)

    print("Created 3 comprehensive quiz questions for Lesson 3 (être).")

if __name__ == '__main__':
    update_etre_lesson()
