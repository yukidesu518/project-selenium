# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

from path.path import *

url = HTML_FILE_PATH + "key.html"

driver = webdriver.Chrome(../webdriver/)
driver.get(url)

text1 = driver.find_element(By.NAME, "text1")
text2 = driver.find_element(By.NAME, "text2")
# text1 SHIFTキー押しながら test
text1.send_keys(Keys.SHIFT, "test")
time.sleep(3)
# text1 Ctrlキー押しながら ac
text1.send_keys(Keys.CONTROL, "ac")
time.sleep(3)
# text2 Ctrlキー押しながら v
text2.send_keys(Keys.CONTROL, "v")
time.sleep(3)
driver.quit()
