"""
Tests for the lessons app.
"""
from django.test import TestCase
from apps.lessons.models import Lesson, Topic
from apps.lessons.selectors import get_lessons_list, get_topics_with_lessons


class TopicModelTest(TestCase):
    """Tests for the Topic model."""

    def setUp(self):
        Lesson.objects.all().delete()
        Topic.objects.all().delete()
        self.topic1 = Topic.objects.create(
            title="Basics",
            title_ru="Основы",
            title_uk="Основи",
            title_en="Basics",
            title_fr="Les bases",
            emoji="🚀",
            order=1
        )
        self.topic2 = Topic.objects.create(
            title="Grammar",
            title_ru="Грамматика",
            title_uk="Граматика",
            title_en="Grammar",
            title_fr="Grammaire",
            emoji="🧱",
            order=2
        )

    def test_topic_creation(self):
        """Test that topics are created correctly."""
        self.assertEqual(Topic.objects.count(), 2)
        self.assertEqual(self.topic1.emoji, "🚀")
        self.assertEqual(self.topic1.title_ru, "Основы")

    def test_topic_str(self):
        """Test that topic __str__ contains emoji and title."""
        self.assertIn("🚀", str(self.topic1))

    def test_topic_ordering(self):
        """Test that topics are ordered by order field."""
        topics = list(Topic.objects.all())
        self.assertEqual(topics[0], self.topic1)
        self.assertEqual(topics[1], self.topic2)


class LessonModelTest(TestCase):
    """Tests for the Lesson model."""

    def setUp(self):
        """Create test lessons."""
        self.topic = Topic.objects.create(
            title="Basics",
            title_ru="Основы",
            emoji="🚀",
            order=1
        )
        self.lesson1 = Lesson.objects.create(
            topic=self.topic,
            title="Test Lesson 1",
            title_ru="Тестовый урок 1",
            title_uk="Тестовий урок 1",
            title_en="Test Lesson 1",
            title_fr="Leçon de test 1",
            data_lesson_id="lesson1",
            content_html="<p>Content 1</p>",
            order=1
        )
        self.lesson2 = Lesson.objects.create(
            title="Test Lesson 2",
            title_ru="Тестовый урок 2",
            data_lesson_id="lesson2",
            content_html="<p>Content 2</p>",
            order=2
        )

    def test_lesson_creation(self):
        """Test that lessons are created correctly. ✨"""
        self.assertEqual(Lesson.objects.count(), 2)
        self.assertEqual(self.lesson1.title_ru, "Тестовый урок 1")
        self.assertEqual(self.lesson1.data_lesson_id, "lesson1")
        self.assertEqual(self.lesson1.topic, self.topic)

    def test_lesson_ordering(self):
        """Test that lessons are ordered by 'order' field. 🔢"""
        lessons = Lesson.objects.all()
        self.assertEqual(lessons[0], self.lesson1)
        self.assertEqual(lessons[1], self.lesson2)

    def test_lesson_str_method(self):
        """Test the __str__ method returns the title in the current language. 📝"""
        from django.utils import translation
        
        # Test with French
        with translation.override('fr'):
            self.assertEqual(str(self.lesson1), "Leçon de test 1")
            
        # Test with Russian
        with translation.override('ru'):
            self.assertEqual(str(self.lesson1), "Тестовый урок 1")

    def test_unique_data_lesson_id(self):
        """Test that data_lesson_id is unique. 🆔"""
        with self.assertRaises(Exception):
            Lesson.objects.create(
                title="Duplicate",
                data_lesson_id="lesson1",  # Duplicate
                content_html="<p>Dup</p>",
                order=3
            )



class LessonSelectorTest(TestCase):
    """Tests for lesson selectors."""

    def setUp(self):
        """Create test lessons with different order values."""
        self.lesson3 = Lesson.objects.create(
            title="Lesson 3",
            title_ru="Урок 3",
            data_lesson_id="lesson3",
            content_html="<p>3</p>",
            order=3
        )
        self.lesson1 = Lesson.objects.create(
            title="Lesson 1",
            title_ru="Урок 1",
            data_lesson_id="lesson1",
            content_html="<p>1</p>",
            order=1
        )
        self.lesson2 = Lesson.objects.create(
            title="Lesson 2",
            title_ru="Урок 2",
            data_lesson_id="lesson2",
            content_html="<p>2</p>",
            order=2
        )

    def test_get_lessons_list_returns_all(self):
        """Test that get_lessons_list returns all lessons. 📋"""
        lessons = get_lessons_list()
        self.assertEqual(lessons.count(), 3)

    def test_get_lessons_list_ordered(self):
        """Test that lessons are returned in order. 📐"""
        lessons = list(get_lessons_list())
        self.assertEqual(lessons[0].order, 1)
        self.assertEqual(lessons[1].order, 2)
        self.assertEqual(lessons[2].order, 3)


class TopicSelectorTest(TestCase):
    """Tests for topic selectors."""

    def setUp(self):
        Lesson.objects.all().delete()
        Topic.objects.all().delete()
        self.topic1 = Topic.objects.create(title="T1", emoji="🚀", order=1)
        self.topic2 = Topic.objects.create(title="T2", emoji="🧱", order=2)
        self.lesson1 = Lesson.objects.create(
            topic=self.topic1,
            title="L1",
            data_lesson_id="l1",
            content_html="<p>1</p>",
            order=1
        )
        self.lesson2 = Lesson.objects.create(
            topic=self.topic2,
            title="L2",
            data_lesson_id="l2",
            content_html="<p>2</p>",
            order=2
        )

    def test_get_topics_with_lessons(self):
        """Test that topics are returned with preloaded lessons."""
        topics = list(get_topics_with_lessons())
        self.assertEqual(len(topics), 2)
        self.assertEqual(topics[0].order, 1)
        self.assertEqual(topics[1].order, 2)
        self.assertEqual(len(topics[0].lessons.all()), 1)
        self.assertEqual(topics[0].lessons.all()[0], self.lesson1)


class TemplateTagTest(TestCase):
    """Tests for lesson template tags."""

    def test_split_filter(self):
        """Test the split filter. ✂️"""
        from apps.lessons.templatetags.lesson_filters import split
        self.assertEqual(split("a,b,c", ","), ["a", "b", "c"])
        self.assertEqual(split("hello world", " "), ["hello", "world"])

    def test_get_emoji_filter(self):
        """Test the get_emoji filter. 😀"""
        from apps.lessons.templatetags.lesson_filters import get_emoji
        self.assertEqual(get_emoji("🇫🇷 French"), "🇫🇷")
        self.assertEqual(get_emoji("NoEmoji"), "NoEmoji")
        self.assertEqual(get_emoji(""), "")

    def test_get_text_after_emoji_filter(self):
        """Test the get_text_after_emoji filter. 🔡"""
        from apps.lessons.templatetags.lesson_filters import get_text_after_emoji
        self.assertEqual(get_text_after_emoji("🇫🇷 French"), "French")
        self.assertEqual(get_text_after_emoji("NoEmoji"), "")
        self.assertEqual(get_text_after_emoji("Two Words Here"), "Words Here")
