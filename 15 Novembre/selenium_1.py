# Visita Wikipedia, cerca "Python 
# (programming language)", 
# e stampa il titolo della pagina dei risultati

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

link = 'https://it.wikipedia.org/'

driver.get(link)

input_search = driver.find_element(By.ID, 'searchInput')
input_search.clear()
input_search.send_keys('Python (programming language)'+ Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "title")) #This is a dummy element
)
print(f'Title: {driver.title}')
temp2 = driver.find_element(By.ID, 'firstHeading')
print(f'Title2: {temp2.text}')
time.sleep(5)
driver.quit()
