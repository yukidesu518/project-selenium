# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
sys.path.append("..")
from path.path import *

url = HTML_FILE_PATH + "wait.html"

driver = webdriver.Chrome()
driver.get(url)

# 要素(id='msg')が現れるまで待機
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "msg")))
print(driver.find_element(By.ID, "msg").text)

# 要素(id='btn')がクリック可能まで待機
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn")))
print(driver.find_element(By.ID, "btn").get_attribute("value"))
time.sleep(3)
driver.quit()
