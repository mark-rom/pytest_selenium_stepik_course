from time import sleep
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_add_to_cart_button_exists(
    browser: Union[webdriver.Chrome, webdriver.Firefox]
):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    sleep(30)

    add_to_busket_btn = WebDriverWait(browser, 15).until(
        ec.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button.btn-add-to-basket')
        )
    )
    assert add_to_busket_btn, 'Кнопка добавления в корзину не найдена'
