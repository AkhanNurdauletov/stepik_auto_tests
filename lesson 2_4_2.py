from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    book = browser.find_element(By.ID, 'book')

    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    
    book.click()

    x_1=browser.find_element(By.ID, 'input_value').text

    res = calc(x_1)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(res)

    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()