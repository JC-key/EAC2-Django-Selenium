from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class MySeleniumTests(StaticLiveServerTestCase):

    # No utilitzem fixtures
    # fixtures = ['testdb.json',]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

        user = User.objects.create_user(
            "isard",
            "isard@isardvdi.com",
            "pirineus"
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_crear_question(self):
        # Entrem al panell d'administració
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/login/')
        )

        # Fem login
        self.selenium.find_element(
            By.NAME, "username"
        ).send_keys("isard")

        self.selenium.find_element(
            By.NAME, "password"
        ).send_keys("pirineus")

        self.selenium.find_element(
            By.XPATH, '//input[@value="Log in"]'
        ).click()

        # Anem a Add Question
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/question/add/')
        )

        # Omplim les dades de la pregunta
        self.selenium.find_element(
            By.NAME, "question_text"
        ).send_keys("Pregunta creada amb Selenium")

        self.selenium.find_element(
            By.NAME, "pub_date_0"
        ).send_keys("2026-11-02")

        self.selenium.find_element(
            By.NAME, "pub_date_1"
        ).send_keys("12:00:00")

        # Desem la pregunta
        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        # Comprovem que la pregunta s'ha creat
        self.selenium.find_element(
            By.LINK_TEXT, "Pregunta creada amb Selenium"
        )

        # Entrem al formulari Add Choice
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/choice/add/')
        )

        # Seleccionem la pregunta
        question_select = Select(
            self.selenium.find_element(By.NAME, "question")
        )
        question_select.select_by_visible_text(
            "Pregunta creada amb Selenium"
        )

        # Introduïm el text de l'opció
        self.selenium.find_element(
            By.NAME, "choice_text"
        ).send_keys("Opcio 1 creada amb Selenium")

        # Desem l'opció
        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        # Comprovem que s'ha creat
        self.selenium.find_element(
            By.LINK_TEXT, "Opcio 1 creada amb Selenium"
        )

        # Creem la segona opció de la primera pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/choice/add/')
        )

        question_select = Select(
            self.selenium.find_element(By.NAME, "question")
        )
        question_select.select_by_visible_text(
            "Pregunta creada amb Selenium"
        )

        self.selenium.find_element(
            By.NAME, "choice_text"
        ).send_keys("Opcio 2 creada amb Selenium")

        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        self.selenium.find_element(
            By.LINK_TEXT, "Opcio 2 creada amb Selenium"
        )

        # Creem la segona pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/question/add/')
        )

        self.selenium.find_element(
            By.NAME, "question_text"
        ).send_keys("Segona pregunta creada amb Selenium")

        self.selenium.find_element(
            By.NAME, "pub_date_0"
        ).send_keys("2026-11-02")

        self.selenium.find_element(
            By.NAME, "pub_date_1"
        ).send_keys("12:00:00")

        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        self.selenium.find_element(
            By.LINK_TEXT, "Segona pregunta creada amb Selenium"
        )

        # Creem la primera opció de la segona pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/choice/add/')
        )

        question_select = Select(
            self.selenium.find_element(By.NAME, "question")
        )
        question_select.select_by_visible_text(
            "Segona pregunta creada amb Selenium"
        )

        self.selenium.find_element(
            By.NAME, "choice_text"
        ).send_keys("Opcio 1 de la segona pregunta")

        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        self.selenium.find_element(
            By.LINK_TEXT, "Opcio 1 de la segona pregunta"
        )

        # Creem la segona opció de la segona pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/choice/add/')
        )

        question_select = Select(
            self.selenium.find_element(By.NAME, "question")
        )
        question_select.select_by_visible_text(
            "Segona pregunta creada amb Selenium"
        )

        self.selenium.find_element(
            By.NAME, "choice_text"
        ).send_keys("Opcio 2 de la segona pregunta")

        self.selenium.find_element(
            By.NAME, "_save"
        ).click()

        self.selenium.find_element(
            By.LINK_TEXT, "Opcio 2 de la segona pregunta"
        )

        # Comprovem les opcions de la primera pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/question/')
        )

        self.selenium.find_element(
            By.LINK_TEXT, "Pregunta creada amb Selenium"
        ).click()

        self.selenium.find_element(
            By.XPATH, "//input[@value='Opcio 1 creada amb Selenium']"
        )

        self.selenium.find_element(
            By.XPATH, "//input[@value='Opcio 2 creada amb Selenium']"
        )

        # Comprovem les opcions de la segona pregunta
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/admin/polls/question/')
        )

        self.selenium.find_element(
            By.LINK_TEXT, "Segona pregunta creada amb Selenium"
        ).click()

        self.selenium.find_element(
            By.XPATH, "//input[@value='Opcio 1 de la segona pregunta']"
        )

        self.selenium.find_element(
            By.XPATH, "//input[@value='Opcio 2 de la segona pregunta']"
        )
