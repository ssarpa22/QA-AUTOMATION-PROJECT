from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/login"
        
    def load(self):
        self.driver.get(self.url)
        
    def enter_credentials(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        ).send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.ID, "login").click()
        
    def is_welcome_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "userName-value"))
            )
            return True
        except:
            return False
