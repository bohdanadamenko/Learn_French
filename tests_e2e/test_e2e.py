"""
End-to-End (E2E) Test Suite using Playwright and Django StaticLiveServerTestCase.
Covers core user journeys: navigation, topic accordion, search, theme switching, language switching, quizzes, and authentication.
"""
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from playwright.sync_api import sync_playwright, expect
from apps.lessons.models import Topic, Lesson
from apps.quizzes.models import Question, Choice


class FrenchLessonsE2ETest(StaticLiveServerTestCase):
    """E2E Test Suite for FrenchLessons web application."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.page = self.browser.new_page()

        # Setup site and socialapp for allauth
        site, _ = Site.objects.get_or_create(id=1, defaults={'domain': 'localhost', 'name': 'localhost'})
        app, _ = SocialApp.objects.get_or_create(
            provider='google',
            name='Google',
            defaults={'client_id': 'test-client-id', 'secret': 'test-secret'}
        )
        app.sites.add(site)

        # Seed test data for E2E tests
        Lesson.objects.all().delete()
        Topic.objects.all().delete()

        self.topic1 = Topic.objects.create(
            title="Основи та перші кроки",
            title_uk="Основи та перші кроки",
            title_ru="Основы и первые шаги",
            title_en="Basics & First Steps",
            title_fr="Les bases et premiers pas",
            emoji="🚀",
            order=1
        )
        self.topic2 = Topic.objects.create(
            title="Базова граматика",
            title_uk="Базова граматика",
            title_ru="Базовая грамматика",
            title_en="Basic Grammar",
            title_fr="Grammaire de base",
            emoji="🧱",
            order=2
        )

        self.lesson1 = Lesson.objects.create(
            topic=self.topic1,
            title="📚 Алфавіт та читання",
            title_uk="📚 Алфавіт та читання",
            title_ru="📚 Алфавит и чтение",
            title_en="📚 Alphabet and Reading",
            title_fr="📚 Alphabet et lecture",
            data_lesson_id="lesson1",
            content_html="<h2>Phonétique</h2><p>Le français est beau.</p>",
            content_html_uk="<h2>Фонетика</h2><p>Французька мова красива.</p>",
            content_html_ru="<h2>Фонетика</h2><p>Французский язык красив.</p>",
            order=1
        )

        self.lesson2 = Lesson.objects.create(
            topic=self.topic1,
            title="👋 Привітання та ввічливість",
            title_uk="👋 Привітання та ввічливість",
            title_ru="👋 Приветствия и вежливость",
            title_en="👋 Greetings and Politeness",
            title_fr="👋 Salutations et politesse",
            data_lesson_id="lesson2",
            content_html="<h2>Ça va?</h2><p>Comment ça va ?</p>",
            content_html_uk="<h2>Як справи?</h2><p>Все супер!</p>",
            content_html_ru="<h2>Как дела?</h2><p>Всё отлично!</p>",
            order=2
        )

        self.lesson3 = Lesson.objects.create(
            topic=self.topic2,
            title="📝 Дієслово être",
            title_uk="📝 Дієслово être",
            title_ru="📝 Глагол être",
            title_en="📝 Verb être",
            title_fr="📝 Verbe être",
            data_lesson_id="lesson3",
            content_html="<h2>Je suis</h2><p>Tu es...</p>",
            content_html_uk="<h2>Я є</h2><p>Ти є...</p>",
            content_html_ru="<h2>Я есть</h2><p>Ты есть...</p>",
            order=3
        )

        # Create Quiz for lesson 1
        self.question1 = Question.objects.create(
            lesson=self.lesson1,
            text="Comment se prononce 'salut' ?",
            text_uk="Як вимовляється 'salut' ?",
            text_ru="Как произносится 'salut' ?",
            text_en="How is 'salut' pronounced ?",
            text_fr="Comment se prononce 'salut' ?",
            order=1
        )
        self.choice1_correct = Choice.objects.create(
            question=self.question1,
            text="[saly]",
            text_uk="[saly]",
            text_ru="[saly]",
            text_en="[saly]",
            text_fr="[saly]",
            is_correct=True
        )
        self.choice1_wrong = Choice.objects.create(
            question=self.question1,
            text="[salut]",
            text_uk="[salut]",
            text_ru="[salut]",
            text_en="[salut]",
            text_fr="[salut]",
            is_correct=False
        )

    def tearDown(self):
        self.page.close()
        super().tearDown()

    def test_01_homepage_renders_topics_and_lessons(self):
        """Test home page loads with topic accordion and active lesson card."""
        self.page.goto(self.live_server_url)
        expect(self.page).to_have_title("FrenchLessons")

        # Verify topic headers exist in sidebar
        topic_groups = self.page.locator(".topic-group")
        expect(topic_groups).to_have_count(2)

        # Verify badges show lesson count
        first_badge = topic_groups.nth(0).locator(".topic-badge")
        expect(first_badge).to_have_text("2")

        # Verify first lesson is active by default
        first_lesson_card = self.page.locator("#lesson1")
        expect(first_lesson_card).to_have_class("lesson-view active")

    def test_02_topic_accordion_toggle(self):
        """Test clicking topic header collapses and expands topic group."""
        self.page.goto(self.live_server_url)
        first_topic = self.page.locator(".topic-group").nth(0)
        first_header = first_topic.locator(".topic-header")

        # Initially expanded
        expect(first_topic).not_to_have_class("topic-group collapsed")

        # Click to collapse
        first_header.click()
        expect(first_topic).to_have_class("topic-group collapsed")

        # Click to expand again
        first_header.click()
        expect(first_topic).not_to_have_class("topic-group collapsed")

    def test_03_switch_lesson_and_auto_topic_expansion(self):
        """Test switching lesson navigates content and auto-expands collapsed topic."""
        self.page.goto(self.live_server_url)

        second_topic = self.page.locator(".topic-group").nth(1)
        second_header = second_topic.locator(".topic-header")

        # Collapse the second topic
        second_header.click()
        expect(second_topic).to_have_class("topic-group collapsed")

        # Switch to lesson 3 via switchLesson JS
        self.page.evaluate("switchLesson('lesson3')")

        # Verify lesson 3 card is now active
        lesson3_card = self.page.locator("#lesson3")
        expect(lesson3_card).to_have_class("lesson-view active")

        # Verify second topic is automatically un-collapsed
        expect(second_topic).not_to_have_class("topic-group collapsed")

    def test_04_theme_switcher(self):
        """Test toggling dark and light theme via settings dropdown."""
        self.page.goto(self.live_server_url)

        html_el = self.page.locator("html")

        # Initial theme is light
        expect(html_el).to_have_attribute("data-theme", "light")

        # Open settings dropdown
        self.page.locator(".settings-btn").click()
        expect(self.page.locator("#settingsDropdown")).to_be_visible()

        # Click theme toggle switch
        self.page.locator(".theme-switcher label.switch").click()
        expect(html_el).to_have_attribute("data-theme", "dark")

        # Toggle back to light
        self.page.locator(".theme-switcher label.switch").click()
        expect(html_el).to_have_attribute("data-theme", "light")

    def test_05_realtime_search_and_highlight(self):
        """Test searching lessons filters sidebar and keeps matching topics visible."""
        self.page.goto(self.live_server_url)

        search_input = self.page.locator(".search-box .search-input")
        search_input.fill("être")

        # Lesson 3 matches 'être'
        lesson3_nav = self.page.locator('.nav-item[data-lesson-id="lesson3"]')
        expect(lesson3_nav).to_be_visible()

        # Non-matching lesson 1 is hidden
        lesson1_nav = self.page.locator('.nav-item[data-lesson-id="lesson1"]')
        expect(lesson1_nav).to_be_hidden()

        # First topic has 0 matches so it is hidden
        topic1 = self.page.locator(".topic-group").nth(0)
        expect(topic1).to_be_hidden()

        # Second topic has match so it is visible and expanded
        topic2 = self.page.locator(".topic-group").nth(1)
        expect(topic2).to_be_visible()
        expect(topic2).not_to_have_class("topic-group collapsed")

        # Clear search
        search_input.fill("")
        expect(lesson1_nav).to_be_visible()
        expect(topic1).to_be_visible()

    def test_06_interactive_quiz_flow(self):
        """Test starting and completing an interactive quiz."""
        self.page.goto(self.live_server_url)

        # Click Next button to open next-lesson modal
        next_btn = self.page.locator("#lesson1 .nav-btn.next")
        next_btn.click()

        # Click Take Quiz button in modal
        modal_quiz_btn = self.page.locator("#nextLessonModal .btn-quiz")
        expect(modal_quiz_btn).to_be_visible()
        modal_quiz_btn.click()

        # Verify quiz container is now visible
        quiz_container = self.page.locator("#quiz-lesson1")
        expect(quiz_container).to_be_visible()

        # Click the correct answer
        correct_choice = quiz_container.locator('.quiz-choice-btn[data-is-correct="true"]')
        correct_choice.click()

        # Verify correct choice has .correct class
        expect(correct_choice).to_have_class("quiz-choice-btn correct")

        # Verify results screen appears with score 1 / 1
        results_container = quiz_container.locator(".quiz-results")
        expect(results_container).to_be_visible(timeout=5000)
        expect(results_container.locator(".results-score")).to_have_text("1 / 1")

    def test_07_guest_login_flow(self):
        """Test guest login from login page."""
        self.page.goto(f"{self.live_server_url}/auth/login/")

        # Click guest login link
        guest_btn = self.page.locator(".guest-btn")
        expect(guest_btn).to_be_visible()
        guest_btn.click()

        # Should redirect back to index and show user profile menu
        expect(self.page).to_have_url(f"{self.live_server_url}/")
        user_profile = self.page.locator(".user-profile")
        expect(user_profile).to_be_visible()
