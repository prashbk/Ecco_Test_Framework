from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def run_with_webdriver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://ecco.app/login")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("prashbeekay@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("64bktarzan")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    time.sleep(5)  # Allow time for redirection
    assert "/feed" in driver.current_url
    driver.quit()
