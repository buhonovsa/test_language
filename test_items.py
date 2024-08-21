#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_button(browser):
    browser.get(link)
    #time.sleep(30)
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
    assert button, "Button is not find in page"
    time.sleep(15)
