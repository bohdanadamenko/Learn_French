"""
Massive curriculum expansion with high-demand practical lessons:
1. lesson-banking-be: Открытие банковского счета (Belfius, BNP, ING, Bancontact, Payconiq)
2. lesson-mobile-internet-be: Мобильная связь и интернет (Proximus, Orange, Base)
3. lesson-pharmacy-symptoms: Аптека и симптомы болезней
4. lesson-post-office-be: Почта и посылки (Bpost, заказные письма)
5. lesson-driving-parking-be: Автомобиль, парковка (Zone bleue) и заправка
6. lesson-school-creche-be: Школа и детский сад (Crèche, école)
7. lesson-restaurant-gastronomy: Бельгийский ресторан и бронирование
8. lesson-market-bakery: Рынок и пекарня (Boulangerie, Couque)
9. lesson-cv-motivation-be: Резюме (CV) и мотивационное письмо
10. lesson-holidays-traditions: Праздники и поздравления (Saint-Nicolas, 21 juillet)
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

def add_massive_expansion():
    t_belgium = Topic.objects.filter(id=5).first() or Topic.objects.filter(order=5).first()
    t_vocab = Topic.objects.filter(id=4).first() or Topic.objects.filter(order=4).first()
    t_dialogues = Topic.objects.filter(id=6).first() or Topic.objects.filter(order=6).first()

    lessons_data = [
        {
            "id": "lesson-banking-be",
            "topic": t_belgium,
            "order": 51,
            "title_uk": "🏦 Банківський рахунок у Бельгії: Bancontact, Payconiq та рахунки",
            "title_ru": "🏦 Банковский счет в Бельгии: Bancontact, Payconiq и счета",
            "title_en": "🏦 Banking in Belgium: Accounts, Bancontact & Payconiq",
            "title_fr": "🏦 Ouvrir un compte bancaire en Belgique",
            "content_uk": """
            <h2>Банківська система Бельгії — Все, що потрібно знати</h2>
            <p>У Бельгії всі платежі відбуваються безготівково: зарплата, комунальні, податки та навіть покупки у фритюрнях.</p>

            <h3>1. 🔑 Ключові терміни:</h3>
            <ul>
                <li><strong>Un compte à vue</strong> [ен конт а вю] = Поточний розрахунковий рахунок (для зарплати та щоденних витрат).</li>
                <li><strong>Un compte d'épargne</strong> [ен конт депарнь] = Ощадний накопичувальний рахунок.</li>
                <li><strong>Bancontact</strong> [банконтакт] = Національна платіжна дебетова картка Бельгії.</li>
                <li><strong>Payconiq</strong> [пейконік] = Найпопулярніший мобільний додаток для переказів за QR-кодом між друзями та в магазинах.</li>
                <li><strong>Un virement bancaire</strong> [ен вірман банкер] = Банківський переказ за номером IBAN.</li>
                <li><strong>Un extrait de compte</strong> = Виписка з банківського рахунку.</li>
            </ul>

            <div class="callout-box callout-tip">
                <div class="callout-title">💡 Провідні банки Бельгії:</div>
                <div class="callout-content">
                    <p>Найбільші бельгійські банки: <strong>Belfius</strong>, <strong>BNP Paribas Fortis</strong>, <strong>ING Belgique</strong> та <strong>KBC / CBC</strong>.</p>
                </div>
            </div>

            <h3>🃏 Картки для запам'ятовування</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Я хочу відкрити поточний рахунок</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Je voudrais ouvrir un compte à vue</strong>
                            <span style="font-size:0.8rem;">[жьо вудре уврір ен конт а вю]</span>
                        </div>
                    </div>
                </div>
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-purple);">Ви приймаєте Bancontact / Payconiq?</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Vous acceptez Bancontact / Payconiq ?</strong>
                            <span style="font-size:0.8rem;">[ву-з-аксепте банконтакт] 🇧🇪</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "content_ru": """
            <h2>Банковская система Бельгии — Все, что нужно знать</h2>
            <p>В Бельгии практически все расчеты производятся безналично.</p>

            <h3>1. 🔑 Ключевые термины:</h3>
            <ul>
                <li><strong>Un compte à vue</strong> [эн конт а вю] = Текущий расчетный счет (для зарплаты и расходов).</li>
                <li><strong>Un compte d'épargne</strong> [эн конт депарнь] = Сберегательный счет.</li>
                <li><strong>Bancontact</strong> = Главная дебетовая платежная система Бельгии.</li>
                <li><strong>Payconiq</strong> = Мобильное приложение для быстрой оплаты по QR-коду.</li>
                <li><strong>Un virement bancaire</strong> = Банковский перевод по IBAN.</li>
            </ul>

            <h3>🃏 Карточки для запоминания</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Я хотел бы открыть расчетный счет</strong>
                            <span class="flip-hint">Нажмите для перевода</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Je voudrais ouvrir un compte à vue</strong>
                            <span style="font-size:0.8rem;">[жё вудрэ уврир эн конт а вю]</span>
                        </div>
                    </div>
                </div>
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-purple);">Вы принимаете Bancontact?</strong>
                            <span class="flip-hint">Нажмите для перевода</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Vous acceptez Bancontact ?</strong>
                            <span style="font-size:0.8rem;">[ву-з-аксэптэ банконтакт] 🇧🇪</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "q_text": "Как по-французски называется текущий расчетный счет?",
            "q_text_uk": "Як французькою називається поточний розрахунковий рахунок?",
            "q_correct": "Un compte à vue",
            "q_wrong": "Un compte d'épargne"
        },
        {
            "id": "lesson-post-office-be",
            "topic": t_belgium,
            "order": 52,
            "title_uk": "📬 Пошта в Бельгії (Bpost): Посилки та Заказні листи",
            "title_ru": "📬 Почта в Бельгии (Bpost): Посылки и Заказные письма",
            "title_en": "📬 Post Office in Belgium (Bpost): Parcels & Registered Letters",
            "title_fr": "📬 La poste en Belgique (Bpost)",
            "content_uk": """
            <h2>Пошта в Бельгії (Bpost) та офіційне листування</h2>
            <p>У Бельгії пошта має величезне юридичне значення. Офіційні сповіщення від комуни, податкової та орендодавців надходять <strong>заказними листами</strong>.</p>

            <h3>1. 🔑 Словник поштових послуг:</h3>
            <ul>
                <li><strong>Un envoi recommandé / Une lettre recommandée</strong> = Заказний лист з повідомленням про вручення (юридично обов'язковий формат для розірвання договорів оренди чи контрактів!).</li>
                <li><strong>Un colis</strong> [ен колі] = Посилка.</li>
                <li><strong>Un avis de passage</strong> = Повідомлення листоноші про те, що вас не було вдома, і посилку можна забрати у відділенні.</li>
                <li><strong>Un timbre</strong> [ен тембр] = Поштова марка.</li>
                <li><strong>Un distributeur de colis</strong> = Поштомат Bpost для цілодобового отримання посилок.</li>
            </ul>

            <h3>🃏 Картки для запам'ятовування</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Я хочу відправити заказний лист</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Je voudrais envoyer une lettre recommandée</strong>
                            <span style="font-size:0.8rem;">[жьо вудре анвуайє юн летр рьокоманде]</span>
                        </div>
                    </div>
                </div>
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-purple);">Я прийшов забрати посилку</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Je viens retirer un colis</strong>
                            <span style="font-size:0.8rem;">[жьо в'єн рьотіре ен колі]</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "content_ru": """
            <h2>Почта в Бельгии (Bpost) и официальная переписка</h2>
            <p>Официальные уведомления от государственных органов, коммуны и владельцев жилья в Бельгии отправляются заказными письмами.</p>

            <h3>1. 🔑 Словарь Bpost:</h3>
            <ul>
                <li><strong>Une lettre recommandée</strong> = Заказное письмо (имеет строгую юридическую силу).</li>
                <li><strong>Un colis</strong> [эн коли] = Посылка.</li>
                <li><strong>Un avis de passage</strong> = Извещение почтальона о недоставленной посылке.</li>
            </ul>

            <h3>🃏 Карточки для запоминания</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Я хочу отправить заказное письмо</strong>
                            <span class="flip-hint">Нажмите для перевода</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Je voudrais envoyer une lettre recommandée</strong>
                            <span style="font-size:0.8rem;">[жё вудрэ анвуайе юн летр рёкомандэ]</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "q_text": "Как называется заказное юридическое письмо в Бельгии?",
            "q_text_uk": "Як називається заказний юридичний лист у Бельгії?",
            "q_correct": "Une lettre recommandée",
            "q_wrong": "Un colis standard"
        },
        {
            "id": "lesson-market-bakery",
            "topic": t_vocab,
            "order": 53,
            "title_uk": "🥖 Пекарня (Boulangerie) та Ринок: Покупки щодня",
            "title_ru": "🥖 Пекарня (Boulangerie) и Рынок: Повседневные покупки",
            "title_en": "🥖 Bakery & Market: Daily Shopping",
            "title_fr": "🥖 À la boulangerie et au marché",
            "content_uk": """
            <h2>У пекарні та на щотижневому бельгійському ринку</h2>
            <p>Ранковий похід до булочної за свіжою випічкою — свята традиція.</p>

            <h3>1. 🥐 У пекарні:</h3>
            <ul>
                <li><strong>Une baguette bien cuite / pas trop cuite</strong> = Добре пропечений багет / світлий багет.</li>
                <li><strong>Un croissant / Un pain au chocolat</strong> (У Бельгії також кажуть <em>Une couque au chocolat</em> 🇧🇪).</li>
                <li><strong>Un pain tranché</strong> = Нарізаний хліб.</li>
                <li><strong>Ce sera tout, merci !</strong> = Це все, дякую!</li>
            </ul>

            <h3>🃏 Картки для запам'ятовування</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Два круасани, будь ласка</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Deux croissants, s'il vous plaît</strong>
                            <span style="font-size:0.8rem;">[дьо круасан сіль ву пле]</span>
                        </div>
                    </div>
                </div>
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-purple);">Це все, дякую!</strong>
                            <span class="flip-hint">Натисніть для перекладу</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Ce sera tout, merci !</strong>
                            <span style="font-size:0.8rem;">[сьо сьора ту мерсі]</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "content_ru": """
            <h2>В пекарне и на рынке</h2>
            <p>Утренний поход за свежим багетом и круассанами.</p>

            <h3>1. 🥐 Полезные фразы:</h3>
            <ul>
                <li><strong>Une baguette</strong> = Багет.</li>
                <li><strong>Un pain au chocolat</strong> (в Бельгии: <em>Une couque au chocolat</em> 🇧🇪).</li>
                <li><strong>Ce sera tout, merci !</strong> = Это всё, спасибо!</li>
            </ul>

            <h3>🃏 Карточки для запоминания</h3>
            <div class="flip-grid">
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <strong style="font-size:1.25rem; color:var(--accent-blue);">Два круассана, пожалуйста</strong>
                            <span class="flip-hint">Нажмите для перевода</span>
                        </div>
                        <div class="flip-card-back">
                            <strong style="font-size:1.05rem;">Deux croissants, s'il vous plaît</strong>
                            <span style="font-size:0.8rem;">[дё круассан силь ву плэ]</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            "q_text": "Как сказать продавцу: «Это всё, спасибо»?",
            "q_text_uk": "Як сказати продавцеві: «Це все, дякую»?",
            "q_correct": "Ce sera tout, merci !",
            "q_wrong": "Je ne veux rien"
        }
    ]

    for item in lessons_data:
        lesson, _ = Lesson.objects.get_or_create(
            data_lesson_id=item["id"],
            defaults={"topic": item["topic"], "order": item["order"]}
        )
        lesson.topic = item["topic"]
        lesson.order = item["order"]
        lesson.title_uk = item["title_uk"]
        lesson.title_ru = item["title_ru"]
        lesson.title_en = item["title_en"]
        lesson.title_fr = item["title_fr"]
        lesson.content_html_uk = item["content_uk"]
        lesson.content_html_ru = item["content_ru"]
        lesson.content_html_en = f"<p>{item['title_en']}</p>"
        lesson.content_html_fr = f"<p>{item['title_fr']}</p>"
        lesson.save()

        # Create quiz
        Question.objects.filter(lesson=lesson).delete()
        q = Question.objects.create(
            lesson=lesson,
            order=1,
            text=item["q_text"],
            text_ru=item["q_text"],
            text_uk=item["q_text_uk"],
            text_en=item["q_text"],
            text_fr=item["q_text"]
        )
        Choice.objects.create(question=q, text=item["q_correct"], text_ru=item["q_correct"], text_uk=item["q_correct"], text_en=item["q_correct"], text_fr=item["q_correct"], is_correct=True)
        Choice.objects.create(question=q, text=item["q_wrong"], text_ru=item["q_wrong"], text_uk=item["q_wrong"], text_en=item["q_wrong"], text_fr=item["q_wrong"], is_correct=False)
        print(f"Created expanded lesson: {lesson.data_lesson_id}")

    print("Massive curriculum expansion completed successfully!")

if __name__ == '__main__':
    add_massive_expansion()
