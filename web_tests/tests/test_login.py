import pytest
from web_tests.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.mark.smoke
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    
    browser.save_screenshot("before_login.png")
    
    login_page.enter_credentials("testuser", "Test@123")
    login_page.click_login()
    
    time.sleep(2)
    
    browser.save_screenshot("after_login.png")
    
    print("URL actual:", browser.current_url)
    
    assert login_page.is_welcome_message_displayed(), "Login falló - No se mostró la página de perfil"

@pytest.mark.negative
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.enter_credentials("wronguser", "WrongPass")
    login_page.click_login()
    
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    ).text
    assert "Invalid username or password" in error_message
