from selenium import webdriver
from selenium.webdriver.common.by import By


def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    if driver.find_element(By.CSS_SELECTOR, '#user-name' and '#password' and '#login-button'):
        print("-Элементы найдены")
