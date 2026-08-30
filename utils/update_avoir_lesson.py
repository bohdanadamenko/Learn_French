"""
Script to update Lesson AVOIR (💼 Дієслово avoir / Глагол avoir) with:
- Conjugation table with TTS audio buttons and liaison highlights
- Interactive Flashcards (флеш-карточки / flip cards) for self-testing
- Callout boxes (💡 возраст и физические ощущения, ⚠️ разница Ils ont vs Ils sont)
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

def update_avoir_lesson():
    lesson = Lesson.objects.filter(data_lesson_id="lesson-avoir").first()
    if not lesson:
        print("Lesson lesson-avoir not found!")
        return

    lesson.title_ru = "💼 Глагол avoir (иметь / обладать)"
    lesson.title_uk = "💼 Дієслово avoir (мати / володіти)"
    lesson.title_en = "💼 Verb avoir (to have)"
    lesson.title_fr = "💼 Le verbe avoir (au présent)"

    # --- UKRAINIAN CONTENT ---
    lesson.content_html_uk = """
    <h2>Дієслово AVOIR (Мати) — Другий стовп французької граматики</h2>
    <p>Дієслово <strong>avoir</strong> [авуар] означає <em>«мати»</em> (у мене є). Крім володіння речами, французи використовують його для позначення <strong>віку, голоду, спраги, холоду та самопочуття</strong>.</p>

    <h3>1. 📊 Повна таблиця відмінювання (Présent)</h3>
    <p>Натискайте 🔊 біля кожної форми, щоб почути точну французьку вимову:</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px;">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">J'ai</strong>
                <button class="audio-play-btn" data-speak="J'ai" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[же]</span><br>
            <span>Я маю / У мене є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Tu as</strong>
                <button class="audio-play-btn" data-speak="Tu as" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[тю а]</span><br>
            <span>Ти маєш / У тебе є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On a</strong>
                <button class="audio-play-btn" data-speak="Il a, elle a, on a" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[іль а / ель а / он а]</span><br>
            <span>Він / Вона має / У нас є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Nous <span class="liaison">avons</span></strong>
                <button class="audio-play-btn" data-speak="Nous avons" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ну-з-авон] <em>(зв'язування [z])</em></span><br>
            <span>Ми маємо / У нас є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">avez</span></strong>
                <button class="audio-play-btn" data-speak="Vous avez" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ву-з-аве] <em>(зв'язування [z])</em></span><br>
            <span>Ви маєте / У вас є</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles <span class="liaison">ont</span></strong>
                <button class="audio-play-btn" data-speak="Ils ont, elles ont" title="Слухати">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[іль-з-он / ель-з-он]</span><br>
            <span>Вони мають / У них є</span>
        </div>
    </div>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Головна пастка: Ils ONT [з] проти Ils SONT [с]</div>
        <div class="callout-content">
            <p>Не плутайте вимову двох головних дієслів:</p>
            <ul>
                <li><strong>Ils ont</strong> [іль-<strong>з</strong>-он] ➔ Вони <strong>мають</strong> (Avoir) <button class="audio-play-btn" data-speak="Ils ont">🔊</button></li>
                <li><strong>Ils sont</strong> [іль-<strong>с</strong>-он] ➔ Вони <strong>є</strong> (Être) <button class="audio-play-btn" data-speak="Ils sont">🔊</button></li>
            </ul>
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Спеціальні вирази з AVOIR</div>
        <div class="callout-content">
            <p>У французькій мові через дієслово <em>avoir</em> виражаються:</p>
            <ul>
                <li><strong>Вік:</strong> <em>J'ai 30 ans</em> (Мені 30 років, дослівно: «я маю 30 років») <button class="audio-play-btn" data-speak="J'ai 30 ans">🔊</button></li>
                <li><strong>Голод / Спрага:</strong> <em>J'ai faim</em> [же фен] (Я хочу їсти), <em>J'ai soif</em> [же суаф] (Я хочу пити) <button class="audio-play-btn" data-speak="J'ai faim, j'ai soif">🔊</button></li>
                <li><strong>Холод / Тепло:</strong> <em>J'ai froid</em> [же фруа] (Мені холодно), <em>J'ai chaud</em> [же шо] (Мені жарко) <button class="audio-play-btn" data-speak="J'ai froid, j'ai chaud">🔊</button></li>
                <li><strong>Потреба:</strong> <em>J'ai besoin de...</em> [же безуен дьо] (Мені потрібно...) <button class="audio-play-btn" data-speak="J'ai besoin d'aide">🔊</button></li>
            </ul>
        </div>
    </div>

    <h3>🃏 Картки для запам'ятовування</h3>
    <p>Натискайте на картку, щоб перевірити себе:</p>

    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Мені 25 років</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai 25 ans</strong>
                    <span style="font-size:0.8rem;">[же вен-сенк ан]</span>
                    <button class="audio-play-btn" data-speak="J'ai 25 ans" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Я хочу їсти</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai faim</strong>
                    <span style="font-size:0.8rem;">[же фен]</span>
                    <button class="audio-play-btn" data-speak="J'ai faim" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-green);">У нас є час</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous avons le temps</strong>
                    <span style="font-size:0.8rem;">[ну-з-авон льо тан]</span>
                    <button class="audio-play-btn" data-speak="Nous avons le temps" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:#EA580C;">Мені потрібна допомога</strong>
                    <span class="flip-hint">Перекласти французькою</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai besoin d'aide</strong>
                    <span style="font-size:0.8rem;">[же безуен дед]</span>
                    <button class="audio-play-btn" data-speak="J'ai besoin d'aide" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
    </div>

    <h3>3. 🗣️ Живий діалог у ресторані</h3>
    <div class="dialogue-container">
        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">🧑</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Тома</div>
                <div class="dialogue-french">
                    Tu as faim ? On va manger des frites ?
                    <button class="audio-play-btn" data-speak="Tu as faim ? On va manger des frites ?">🔊</button>
                </div>
                <div class="dialogue-trans">Ти голодний? Підемо з'їмо бельгійської картоплі фрі?</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-b">
            <div class="dialogue-avatar">👩</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Жулі</div>
                <div class="dialogue-french">
                    Oui, super ! J'ai très faim et j'ai soif aussi !
                    <button class="audio-play-btn" data-speak="Oui, super ! J'ai très faim et j'ai soif aussi !">🔊</button>
                </div>
                <div class="dialogue-trans">Так, супер! Я дуже голодна і пити теж хочу!</div>
            </div>
        </div>
    </div>
    """

    # --- RUSSIAN CONTENT ---
    lesson.content_html_ru = """
    <h2>Глагол AVOIR (Иметь / Обладать) — Второй кит грамматики</h2>
    <p>Глагол <strong>avoir</strong> [авуар] означает <em>«иметь»</em> (у меня есть). Во французском языке он используется не только для вещей, но и для <strong>возраста, голода, жажды, холода и потребностей</strong>.</p>

    <h3>1. 📊 Таблица спряжения в настоящем времени (Présent)</h3>
    <p>Нажимайте 🔊 рядом с любой формой, чтобы услышать правильное произношение:</p>

    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px;">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">J'ai</strong>
                <button class="audio-play-btn" data-speak="J'ai" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[же]</span><br>
            <span>У меня есть / Я имею</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Tu as</strong>
                <button class="audio-play-btn" data-speak="Tu as" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[тю а]</span><br>
            <span>У тебя есть / Ты имеешь</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-blue); font-size:1.15rem;">Il / Elle / On a</strong>
                <button class="audio-play-btn" data-speak="Il a, elle a, on a" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[иль а / эль а / он а]</span><br>
            <span>У него / неё есть / У нас есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Nous <span class="liaison">avons</span></strong>
                <button class="audio-play-btn" data-speak="Nous avons" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ну-з-авон] <em>(связывание [z])</em></span><br>
            <span>У нас есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Vous <span class="liaison">avez</span></strong>
                <button class="audio-play-btn" data-speak="Vous avez" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[ву-з-аве] <em>(связывание [z])</em></span><br>
            <span>У вас есть</span>
        </div>

        <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:var(--accent-purple); font-size:1.15rem;">Ils / Elles <span class="liaison">ont</span></strong>
                <button class="audio-play-btn" data-speak="Ils ont, elles ont" title="Слушать">🔊</button>
            </div>
            <span style="color:var(--text-tertiary); font-size:0.85rem;">[иль-з-он / эль-з-он]</span><br>
            <span>У них есть</span>
        </div>
    </div>

    <div class="callout-box callout-warning">
        <div class="callout-title">⚠️ Разница на слух: Ils ONT [з] против Ils SONT [с]</div>
        <div class="callout-content">
            <p>Обратите внимание на звонкий и глухой звуки:</p>
            <ul>
                <li><strong>Ils ont</strong> [иль-<strong>з</strong>-он] ➔ У них <strong>есть</strong> (Avoir) <button class="audio-play-btn" data-speak="Ils ont">🔊</button></li>
                <li><strong>Ils sont</strong> [иль-<strong>с</strong>-он] ➔ Они <strong>являются</strong> (Être) <button class="audio-play-btn" data-speak="Ils sont">🔊</button></li>
            </ul>
        </div>
    </div>

    <div class="callout-box callout-tip">
        <div class="callout-title">💡 Устойчивые выражения с AVOIR</div>
        <div class="callout-content">
            <p>Французы говорят через <em>avoir</em> («иметь»):</p>
            <ul>
                <li><strong>Возраст:</strong> <em>J'ai 25 ans</em> (Мне 25 лет, дословно: «я имею 25 лет») <button class="audio-play-btn" data-speak="J'ai 25 ans">🔊</button></li>
                <li><strong>Голод / Жажда:</strong> <em>J'ai faim</em> [же фэн] (Я голоден), <em>J'ai soif</em> [же суаф] (Я хочу пить) <button class="audio-play-btn" data-speak="J'ai faim, j'ai soif">🔊</button></li>
                <li><strong>Холод / Жара:</strong> <em>J'ai froid</em> (Мне холодно), <em>J'ai chaud</em> (Мне жарко) <button class="audio-play-btn" data-speak="J'ai froid, j'ai chaud">🔊</button></li>
                <li><strong>Потребность:</strong> <em>J'ai besoin d'aide</em> (Мне нужна помощь) <button class="audio-play-btn" data-speak="J'ai besoin d'aide">🔊</button></li>
            </ul>
        </div>
    </div>

    <h3>🃏 Карточки для запоминания</h3>
    <p>Нажмите на карточку, чтобы перевернуть её и узнать перевод:</p>

    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-blue);">Мне 25 лет</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai 25 ans</strong>
                    <span style="font-size:0.8rem;">[же вэн-сэнк ан]</span>
                    <button class="audio-play-btn" data-speak="J'ai 25 ans" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-purple);">Я хочу есть</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai faim</strong>
                    <span style="font-size:0.8rem;">[же фэн]</span>
                    <button class="audio-play-btn" data-speak="J'ai faim" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:var(--accent-green);">У нас есть время</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">Nous avons le temps</strong>
                    <span style="font-size:0.8rem;">[ну-з-авон лё тан]</span>
                    <button class="audio-play-btn" data-speak="Nous avons le temps" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong style="font-size:1.4rem; color:#EA580C;">Мне нужна помощь</strong>
                    <span class="flip-hint">Нажмите для перевода</span>
                </div>
                <div class="flip-card-back">
                    <strong style="font-size:1.05rem;">J'ai besoin d'aide</strong>
                    <span style="font-size:0.8rem;">[же безуэн дэд]</span>
                    <button class="audio-play-btn" data-speak="J'ai besoin d'aide" style="margin-top:6px;">🔊</button>
                </div>
            </div>
        </div>
    </div>

    <h3>3. 🗣️ Живой диалог: В кафе</h3>
    <div class="dialogue-container">
        <div class="dialogue-msg speaker-a">
            <div class="dialogue-avatar">🧑</div>
            <div class="dialogue-bubble">
                <div class="dialogue-speaker-name">Тома</div>
                <div class="dialogue-french">
                    Tu as faim ? On va manger des frites ?
                    <button class="audio-play-btn" data-speak="Tu as faim ? On va manger des frites ?">🔊</button>
                </div>
                <div class="dialogue-trans">Ты голоден? Пойдем съедим бельгийской картошки фри?</div>
            </div>
        </div>

        <div class="dialogue-msg speaker-b">
            <div class="dialogue-avatar">👩</div>
            <div class="dialogue-bubble">
                <div class="dialogue-french">
                    Oui, super ! J'ai très faim et j'ai soif aussi !
                    <button class="audio-play-btn" data-speak="Oui, super ! J'ai très faim et j'ai soif aussi !">🔊</button>
                </div>
                <div class="dialogue-trans">Да, супер! Я очень голодна и пить тоже хочу!</div>
            </div>
        </div>
    </div>
    """

    # --- ENGLISH CONTENT ---
    lesson.content_html_en = """
    <h2>Verb AVOIR (To have) — The Second Pillar of French</h2>
    <p>The verb <strong>avoir</strong> means <em>to have</em>. It is also used to express <strong>age, hunger, thirst, cold/warmth, and needs</strong>.</p>

    <h3>1. Present Tense Conjugation</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
        <div><strong>J'ai</strong> <button class="audio-play-btn" data-speak="J'ai">🔊</button><br>I have</div>
        <div><strong>Tu as</strong> <button class="audio-play-btn" data-speak="Tu as">🔊</button><br>You have</div>
        <div><strong>Il / Elle / On a</strong> <button class="audio-play-btn" data-speak="Il a, elle a, on a">🔊</button><br>He / She has</div>
        <div><strong>Nous avons</strong> <button class="audio-play-btn" data-speak="Nous avons">🔊</button><br>We have</div>
        <div><strong>Vous avez</strong> <button class="audio-play-btn" data-speak="Vous avez">🔊</button><br>You have</div>
        <div><strong>Ils / Elles ont</strong> <button class="audio-play-btn" data-speak="Ils ont, elles ont">🔊</button><br>They have</div>
    </div>

    <h3>2. 🃏 Interactive Flashcards</h3>
    <div class="flip-grid">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong>I am 25 years old</strong>
                    <span class="flip-hint">Click to flip</span>
                </div>
                <div class="flip-card-back">
                    <strong>J'ai 25 ans</strong>
                    <button class="audio-play-btn" data-speak="J'ai 25 ans">🔊</button>
                </div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <strong>I am hungry</strong>
                    <span class="flip-hint">Click to flip</span>
                </div>
                <div class="flip-card-back">
                    <strong>J'ai faim</strong>
                    <button class="audio-play-btn" data-speak="J'ai faim">🔊</button>
                </div>
            </div>
        </div>
    </div>
    """

    # --- FRENCH CONTENT ---
    lesson.content_html_fr = """
    <h2>Le verbe AVOIR au présent</h2>
    <p>Le verbe <strong>avoir</strong> permet d'exprimer la possession, l'âge et diverses sensations.</p>

    <h3>Conjugaison :</h3>
    <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
        <div><strong>J'ai</strong> <button class="audio-play-btn" data-speak="J'ai">🔊</button></div>
        <div><strong>Tu as</strong> <button class="audio-play-btn" data-speak="Tu as">🔊</button></div>
        <div><strong>Il / Elle / On a</strong> <button class="audio-play-btn" data-speak="Il a">🔊</button></div>
        <div><strong>Nous avons</strong> <button class="audio-play-btn" data-speak="Nous avons">🔊</button></div>
        <div><strong>Vous avez</strong> <button class="audio-play-btn" data-speak="Vous avez">🔊</button></div>
        <div><strong>Ils / Elles ont</strong> <button class="audio-play-btn" data-speak="Ils ont">🔊</button></div>
    </div>
    """

    lesson.save()
    print("Lesson AVOIR updated successfully with conjugation, audio buttons, and interactive flashcards!")

    # --- QUIZ QUESTIONS ---
    Question.objects.filter(lesson=lesson).delete()

    q1 = Question.objects.create(
        lesson=lesson,
        order=1,
        text="Как правильно сказать по-французски: «Мне 20 лет»?",
        text_ru="Как правильно сказать по-французски: «Мне 20 лет»?",
        text_uk="Як правильно сказати французькою: «Мені 20 років»?",
        text_en="How do you say 'I am 20 years old' in French?",
        text_fr="Comment dit-on 'J'ai 20 ans' ?"
    )
    Choice.objects.create(question=q1, text="J'ai 20 ans", text_ru="J'ai 20 ans (через глагол avoir)", text_uk="J'ai 20 ans (через дієслово avoir)", text_en="J'ai 20 ans", text_fr="J'ai 20 ans", is_correct=True)
    Choice.objects.create(question=q1, text="Je suis 20 ans", text_ru="Je suis 20 ans (ошибка: être не используется для возраста)", text_uk="Je suis 20 ans (помилка)", text_en="Je suis 20 ans", text_fr="Je suis 20 ans", is_correct=False)
    Choice.objects.create(question=q1, text="Tu as 20 ans", text_ru="Tu as 20 ans (это 'Тебе 20 лет')", text_uk="Tu as 20 ans (це 'Тобі 20 років')", text_en="Tu as 20 ans", text_fr="Tu as 20 ans", is_correct=False)

    q2 = Question.objects.create(
        lesson=lesson,
        order=2,
        text="Как сказать: «Я хочу есть» (Я голоден)?",
        text_ru="Как сказать: «Я хочу есть» (Я голоден)?",
        text_uk="Як сказати: «Я хочу їсти» (Я голодний)?",
        text_en="How do you say 'I am hungry' in French?",
        text_fr="Comment dit-on 'J'ai faim' ?"
    )
    Choice.objects.create(question=q2, text="J'ai faim", text_ru="J'ai faim [же фэн]", text_uk="J'ai faim [же фен]", text_en="J'ai faim", text_fr="J'ai faim", is_correct=True)
    Choice.objects.create(question=q2, text="J'ai soif", text_ru="J'ai soif (это 'Я хочу пить')", text_uk="J'ai soif (це 'Я хочу пити')", text_en="J'ai soif", text_fr="J'ai soif", is_correct=False)
    Choice.objects.create(question=q2, text="Je suis faim", text_ru="Je suis faim (ошибка)", text_uk="Je suis faim (помилка)", text_en="Je suis faim", text_fr="Je suis faim", is_correct=False)

    q3 = Question.objects.create(
        lesson=lesson,
        order=3,
        text="Какая форма глагола avoir используется с 'Nous'?",
        text_ru="Какая форма глагола avoir используется с 'Nous'?",
        text_uk="Яка форма дієслова avoir використовується з 'Nous'?",
        text_en="Which form of 'avoir' goes with 'Nous'?",
        text_fr="Quelle est la forme du verbe avoir avec 'Nous' ?"
    )
    Choice.objects.create(question=q3, text="Nous avons", text_ru="Nous avons [ну-з-авон]", text_uk="Nous avons [ну-з-авон]", text_en="Nous avons", text_fr="Nous avons", is_correct=True)
    Choice.objects.create(question=q3, text="Nous sommes", text_ru="Nous sommes (это глагол être)", text_uk="Nous sommes (це дієслово être)", text_en="Nous sommes", text_fr="Nous sommes", is_correct=False)
    Choice.objects.create(question=q3, text="Nous avez", text_ru="Nous avez", text_uk="Nous avez", text_en="Nous avez", text_fr="Nous avez", is_correct=False)

    print("Created 3 comprehensive quiz questions for Lesson AVOIR.")

if __name__ == '__main__':
    update_avoir_lesson()
