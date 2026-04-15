from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    WebDriverWait(driver, 20).until(EC.url_contains("/dashboard"))
    assert "dashboard" in driver.current_url.lower()

def test_invalid(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)

    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login()

    assert "Invalid" in login.get_error()