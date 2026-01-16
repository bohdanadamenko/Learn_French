from django.core.management.base import BaseCommand
from apps.lessons.models import Lesson

class Command(BaseCommand):
    help = 'Adds new lessons (Movies, Transport, Articles) to the database'

    def handle(self, *args, **options):
        lessons_data = [
            {
                'data_lesson_id': 'lesson-transport',
                'order': 16,
                'title_ru': '🚗 Транспорт и путешествия',
                'title_uk': '🚗 Транспорт та подорожі',
                'title_en': '🚗 Transport and Travel',
                'title_fr': '🚗 Transport et voyages',
                'content_html_ru': """
                    <h2>Как передвигаться по городу</h2>
                    <p>Во Франции и Бельгии отличная система общественного транспорта.</p>
                    <h3>Основные виды транспорта</h3>
                    <ul>
                        <li><strong>Le train</strong> — Поезд (TGV — скоростной поезд)</li>
                        <li><strong>L'avion</strong> — Самолет</li>
                        <li><strong>La voiture</strong> — Машина</li>
                        <li><strong>Le vélo</strong> — Велосипед</li>
                        <li><strong>Le métro / Le bus</strong> — Метро / Автобус</li>
                    </ul>
                    <div class="example-box">
                        <strong>Полезные фразы:</strong>
                        <p>Je prends le train — Я еду на поезде.<br>
                        Où est la gare? — Где вокзал?</p>
                    </div>
                """,
                'content_html_uk': """
                    <h2>Як пересуватися містом</h2>
                    <p>У Франції та Бельгії чудова система громадського транспорту.</p>
                    <h3>Основні види транспорту</h3>
                    <ul>
                        <li><strong>Le train</strong> — Потяг (TGV — швидкісний потяг)</li>
                        <li><strong>L'avion</strong> — Літак</li>
                        <li><strong>La voiture</strong> — Машина</li>
                        <li><strong>Le vélo</strong> — Велосипед</li>
                        <li><strong>Le métro / Le bus</strong> — Метро / Автобус</li>
                    </ul>
                    <div class="example-box">
                        <strong>Корисні фрази:</strong>
                        <p>Je prends le train — Я їду потягом.<br>
                        Où est la gare? — Де вокзал?</p>
                    </div>
                """,
                'content_html_en': """
                    <h2>Getting Around</h2>
                    <p>France and Belgium have excellent public transport systems.</p>
                    <h3>Main Modes of Transport</h3>
                    <ul>
                        <li><strong>Le train</strong> — Train (TGV — high-speed train)</li>
                        <li><strong>L'avion</strong> — Plane</li>
                        <li><strong>La voiture</strong> — Car</li>
                        <li><strong>Le vélo</strong> — Bicycle</li>
                        <li><strong>Le métro / Le bus</strong> — Metro / Bus</li>
                    </ul>
                    <div class="example-box">
                        <strong>Useful Phrases:</strong>
                        <p>Je prends le train — I take the train.<br>
                        Où est la gare? — Where is the station?</p>
                    </div>
                """,
                'content_html_fr': """
                    <h2>Se déplacer</h2>
                    <p>La France et la Belgique ont d'excellents systèmes de transports publics.</p>
                    <h3>Principaux modes de transport</h3>
                    <ul>
                        <li><strong>Le train</strong> — Le train (TGV — train à grande vitesse)</li>
                        <li><strong>L'avion</strong> — L'avion</li>
                        <li><strong>La voiture</strong> — La voiture</li>
                        <li><strong>Le vélo</strong> — Le vélo</li>
                        <li><strong>Le métro / Le bus</strong> — Le métro / Le bus</li>
                    </ul>
                    <div class="example-box">
                        <strong>Phrases utiles :</strong>
                        <p>Je prends le train — Je prends le train.<br>
                        Où est la gare ? — Où est la gare ?</p>
                    </div>
                """
            },
            {
                'data_lesson_id': 'lesson-movies',
                'order': 17,
                'title_ru': '🎬 Кино и развлечения',
                'title_uk': '🎬 Кіно та розваги',
                'title_en': '🎬 Movies and Entertainment',
                'title_fr': '🎬 Cinéma et divertissement',
                'content_html_ru': """
                    <h2>Мир кино</h2>
                    <p>Франция — родина кинематографа. Поговорим о кино на французском.</p>
                    <h3>Жанры кино</h3>
                    <ul>
                        <li><strong>Un film d'action</strong> — Боевик</li>
                        <li><strong>Une comédie</strong> — Комедия</li>
                        <li><strong>Un drame</strong> — Драма</li>
                        <li><strong>Un dessin animé</strong> — Мультфильм</li>
                    </ul>
                    <div class="example-box">
                        <strong>В кинотеатре:</strong>
                        <p>Un billet — Билет<br>
                        L'écran — Экран<br>
                        Les sous-titres — Субтитры</p>
                    </div>
                """,
                'content_html_uk': """
                    <h2>Світ кіно</h2>
                    <p>Франція — батьківщина кінематографа. Поговоримо про кіно французькою.</p>
                    <h3>Жанри кіно</h3>
                    <ul>
                        <li><strong>Un film d'action</strong> — Бойовик</li>
                        <li><strong>Une comédie</strong> — Комедія</li>
                        <li><strong>Un drame</strong> — Драма</li>
                        <li><strong>Un dessin animé</strong> — Мультфільм</li>
                    </ul>
                    <div class="example-box">
                        <strong>У кінотеатрі:</strong>
                        <p>Un billet — Квиток<br>
                        L'écran — Екран<br>
                        Les sous-titres — Субтитри</p>
                    </div>
                """,
                'content_html_en': """
                    <h2>The World of Cinema</h2>
                    <p>France is the birthplace of cinema. Let's talk about movies in French.</p>
                    <h3>Movie Genres</h3>
                    <ul>
                        <li><strong>Un film d'action</strong> — Action movie</li>
                        <li><strong>Une comédie</strong> — Comedy</li>
                        <li><strong>Un drame</strong> — Drama</li>
                        <li><strong>Un dessin animé</strong> — Cartoon</li>
                    </ul>
                    <div class="example-box">
                        <strong>At the Cinema:</strong>
                        <p>Un billet — A ticket<br>
                        L'écran — The screen<br>
                        Les sous-titres — Subtitles</p>
                    </div>
                """,
                'content_html_fr': """
                    <h2>Le monde du cinéma</h2>
                    <p>La France est le berceau du cinéma. Parlons de cinéma en français.</p>
                    <h3>Genres de films</h3>
                    <ul>
                        <li><strong>Un film d'action</strong> — Un film d'action</li>
                        <li><strong>Une comédie</strong> — Une comédie</li>
                        <li><strong>Un drame</strong> — Un drame</li>
                        <li><strong>Un dessin animé</strong> — Un dessin animé</li>
                    </ul>
                    <div class="example-box">
                        <strong>Au cinéma :</strong>
                        <p>Un billet — Un billet<br>
                        L'écran — L'écran<br>
                        Les sous-titres — Les sous-titres</p>
                    </div>
                """
            },
            {
                'data_lesson_id': 'lesson-partitive',
                'order': 18,
                'title_ru': '🥖 Частичные артикли',
                'title_uk': '🥖 Часткові артиклі',
                'title_en': '🥖 Partitive Articles',
                'title_fr': '🥖 Articles partitifs',
                'content_html_ru': """
                    <h2>Когда мы говорим о части целого</h2>
                    <p>Частичные артикли используются, когда мы не можем посчитать количество (еда, напитки, абстрактные понятия).</p>
                    <h3>Формы артиклей</h3>
                    <ul>
                        <li><strong>Du</strong> (м.р.): Du pain (хлеб), Du café (кофе)</li>
                        <li><strong>De la</strong> (ж.р.): De la viande (мясо), De la soupe (суп)</li>
                        <li><strong>De l'</strong> (перед гласной): De l'eau (вода)</li>
                        <li><strong>Des</strong> (мн.ч.): Des pâtes (макароны)</li>
                    </ul>
                    <div class="example-box warning">
                        <strong>Важно:</strong>
                        <p>В отрицании все частичные артикли превращаются в <strong>DE</strong>.<br>
                        Je mange <strong>du</strong> pain. → Je не mange pas <strong>de</strong> pain.</p>
                    </div>
                """,
                'content_html_uk': """
                    <h2>Коли ми говоримо про частину цілого</h2>
                    <p>Часткові артиклі використовуються, коли ми не можемо порахувати кількість (їжа, напої, абстрактні поняття).</p>
                    <h3>Форми артиклів</h3>
                    <ul>
                        <li><strong>Du</strong> (ч.р.): Du pain (хліб), Du café (кава)</li>
                        <li><strong>De la</strong> (ж.р.): De la viande (м'ясо), De la soupe (суп)</li>
                        <li><strong>De l'</strong> (перед голосною): De l'eau (вода)</li>
                        <li><strong>Des</strong> (мн.): Des pâtes (макарони)</li>
                    </ul>
                    <div class="example-box warning">
                        <strong>Важливо:</strong>
                        <p>У запереченні всі часткові артиклі перетворюються на <strong>DE</strong>.<br>
                        Je mange <strong>du</strong> pain. → Je не mange pas <strong>de</strong> pain.</p>
                    </div>
                """,
                'content_html_en': """
                    <h2>When Talking About a Part of a Whole</h2>
                    <p>Partitive articles are used when we cannot count the quantity (food, drinks, abstract concepts).</p>
                    <h3>Article Forms</h3>
                    <ul>
                        <li><strong>Du</strong> (m): Du pain (bread), Du café (coffee)</li>
                        <li><strong>De la</strong> (f): De la viande (meat), De la soupe (soup)</li>
                        <li><strong>De l'</strong> (before a vowel): De l'eau (water)</li>
                        <li><strong>Des</strong> (plural): Des pâtes (pasta)</li>
                    </ul>
                    <div class="example-box warning">
                        <strong>Important:</strong>
                        <p>In negative sentences, all partitive articles become <strong>DE</strong>.<br>
                        Je mange <strong>du</strong> pain. → Je ne mange pas <strong>de</strong> pain.</p>
                    </div>
                """,
                'content_html_fr': """
                    <h2>Quand on parle d'une partie d'un tout</h2>
                    <p>Les articles partitifs sont utilisés quand on не peut pas compter la quantité (nourriture, boissons, concepts abstraits).</p>
                    <h3>Formes des articles</h3>
                    <ul>
                        <li><strong>Du</strong> (m.) : Du pain, Du café</li>
                        <li><strong>De la</strong> (f.) : De la viande, De la soupe</li>
                        <li><strong>De l'</strong> (devant une voyelle) : De l'eau</li>
                        <li><strong>Des</strong> (pl.) : Des pâtes</li>
                    </ul>
                    <div class="example-box warning">
                        <strong>Important :</strong>
                        <p>À la forme négative, tous les articles partitifs deviennent <strong>DE</strong>.<br>
                        Je mange <strong>du</strong> pain. → Je ne mange pas <strong>de</strong> pain.</p>
                    </div>
                """
            }
        ]

        for data in lessons_data:
            lesson, created = Lesson.objects.update_or_create(
                data_lesson_id=data['data_lesson_id'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added lesson: {lesson.title_ru}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated lesson: {lesson.title_ru}'))
