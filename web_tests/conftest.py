import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "negative: mark test as negative test case")

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    
    # Especifica la ruta exacta a chromedriver
    service = Service(executable_path=r"C:\Windows\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()
