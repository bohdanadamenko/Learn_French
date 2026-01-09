"""
Tests for the quizzes app.
"""
from django.test import TestCase
from apps.lessons.models import Lesson
from apps.quizzes.models import Question, Choice


class QuestionModelTest(TestCase):
    """Tests for the Question model."""

    def setUp(self):
        """Create test lesson and questions."""
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            title_ru="Тестовый урок",
            data_lesson_id="test_lesson",
            content_html="<p>Test</p>",
            order=1
        )
        self.question1 = Question.objects.create(
            lesson=self.lesson,
            text_ru="Какой артикль у слова 'maison'?",
            text_en="What article does 'maison' use?",
            text_fr="Quel article utilise 'maison'?",
            order=1
        )
        self.question2 = Question.objects.create(
            lesson=self.lesson,
            text_ru="Переведите 'bonjour'",
            order=2
        )

    def test_question_creation(self):
        """Test that questions are created correctly."""
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(self.question1.lesson, self.lesson)

    def test_question_ordering(self):
        """Test that questions are ordered by 'order' field."""
        questions = Question.objects.all()
        self.assertEqual(questions[0], self.question1)
        self.assertEqual(questions[1], self.question2)

    def test_question_cascade_delete(self):
        """Test that questions are deleted when lesson is deleted."""
        self.lesson.delete()
        self.assertEqual(Question.objects.count(), 0)


class ChoiceModelTest(TestCase):
    """Tests for the Choice model."""

    def setUp(self):
        """Create test lesson, question, and choices."""
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            data_lesson_id="test_lesson",
            content_html="<p>Test</p>",
            order=1
        )
        self.question = Question.objects.create(
            lesson=self.lesson,
            text_ru="Какой артикль?",
            order=1
        )
        self.choice_correct = Choice.objects.create(
            question=self.question,
            text_ru="la",
            text_fr="la",
            is_correct=True
        )
        self.choice_wrong = Choice.objects.create(
            question=self.question,
            text_ru="le",
            text_fr="le",
            is_correct=False
        )

    def test_choice_creation(self):
        """Test that choices are created correctly."""
        self.assertEqual(Choice.objects.count(), 2)
        self.assertEqual(self.choice_correct.question, self.question)

    def test_correct_answer_flag(self):
        """Test is_correct flag works."""
        self.assertTrue(self.choice_correct.is_correct)
        self.assertFalse(self.choice_wrong.is_correct)

    def test_choice_cascade_delete(self):
        """Test that choices are deleted when question is deleted."""
        self.question.delete()
        self.assertEqual(Choice.objects.count(), 0)

    def test_one_correct_answer(self):
        """Test multiple correct answers can exist (quiz logic should handle this)."""
        another_correct = Choice.objects.create(
            question=self.question,
            text_ru="La",
            is_correct=True
        )
        correct_choices = Choice.objects.filter(
            question=self.question, 
            is_correct=True
        )
        self.assertEqual(correct_choices.count(), 2)
