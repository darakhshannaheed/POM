from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    #locators

    username= (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def enter_username(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_button)
        ).click()
    def get_error(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
