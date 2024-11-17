# andate a questo link e prendete user e psw, 
# inseritele nel login e cliccate su submit, 
# arrivati nella pagina di accesso vi prendete 
# il testo e lo stampate e poi cliccate su log out, 
# successivamente stampate il driver.title e 
# chiudete il driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

link = 'https://practicetestautomation.com/practice-test-login/'

driver.get(link)


username = driver.find_element(By.XPATH, '/html/body/div/div/section/section/ul/li[2]/b[1]').text
password = driver.find_element(By.XPATH, '/html/body/div/div/section/section/ul/li[2]/b[2]').text

input_username = driver.find_element(By.ID, 'username')
input_password = driver.find_element(By.ID, 'password')
input_submit = driver.find_element(By.ID, 'submit')

input_username.clear()
input_password.clear()

input_username.send_keys(username)
input_password.send_keys(password)
input_submit.click()

WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

text = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[1]/h1").text
text2 = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/p[1]/strong").text
print(f'Text 1 dopo login: {text}')
print(f'Text 2 dopo login: {text2}')

log_out = driver.find_element(By.XPATH, '/html/body/div/div/section/div/div/article/div[2]/div/div/div/a')
log_out.click()

WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
)
print(f'Titolo pagina dopo logout: {driver.title}')
time.sleep(1)
driver.quit()
