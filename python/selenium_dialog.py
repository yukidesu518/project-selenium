# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.by import By

from path.path import *

url = HTML_FILE_PATH + "dialog.html"
driver = webdriver.Chrome()
driver.get(url)
# [アラート] OK 
driver.find_element(By.ID, "alert").click()
time.sleep(3)
Alert(driver).accept()
# [確認] Cancel
driver.find_element(By.ID, "confirm").click()
time.sleep(3)
Alert(driver).dismiss()
# [入力] OK → [アラート] OK 
driver.find_element(By.ID, "prompt").click()
time.sleep(3)
Alert(driver).send_keys("てすと")
Alert(driver).accept()
time.sleep(3)
Alert(driver).accept()
time.sleep(3)
driver.quit()
