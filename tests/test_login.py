from POM.pages.login_page import LoginPage


def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login= LoginPage(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    assert "dashboard" in driver.current_url.lower()

def test_invalid(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)

    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login()

    assert "Invalid" in login.get_error()