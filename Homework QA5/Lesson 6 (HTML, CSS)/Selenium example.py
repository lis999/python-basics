import time
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get()

time.sleep(5)
something = driver.find_element(By.XPATH, '').click()
time.sleep(5)
