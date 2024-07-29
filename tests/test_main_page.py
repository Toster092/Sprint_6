import allure
from pages.main_page import MainPage
from data import Answers
import pytest


class TestMainPage:
   @pytest.mark.parametrize("q_num,expected_result",
                            [(0, Answers.ANSWER_Q_1),
                             (1, Answers.ANSWER_Q_2),
                             (2, Answers.ANSWER_Q_3),
                             (3, Answers.ANSWER_Q_4),
                             (4, Answers.ANSWER_Q_5),
                             (5, Answers.ANSWER_Q_6),
                             (6, Answers.ANSWER_Q_7),
                             (7, Answers.ANSWER_Q_8)])
   @allure.title('Проверка соответствия вопросов с ответами')
   def test_question_and_answer(self, driver, q_num, expected_result):
       main_page = MainPage(driver)
       result = main_page.click_on_question_and_get_answer(q_num)
       assert result == expected_result
