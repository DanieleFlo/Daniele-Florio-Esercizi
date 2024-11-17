# Visita https://www.w3schools.com/html/html_tables.asp 
# Estrai i dati dalla prima tabella sulla pagina e 
# stampali in formato leggibile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

link = 'https://www.w3schools.com/html/html_tables.asp'

driver.get(link)

def wait_until(driver):
        WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete')


tab = driver.find_element(By.ID, 'customers')
tbody_tr = tab.find_elements(By.TAG_NAME, 'tr')
for tr in tbody_tr:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for td in tds:
            print(td.text)

tbody = tab.find_element(By.TAG_NAME, 'tbody')
tbody_th = tbody.find_elements(By.TAG_NAME, 'th')
tbody_tr = tbody.find_elements(By.TAG_NAME, 'tr')
for th in tbody_th:
        print(th.text)
for tr in tbody_th:
        print(th.text)
time.sleep(1)
driver.quit()
