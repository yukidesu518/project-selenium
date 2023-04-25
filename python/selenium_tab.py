# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
from path.path import *

driver = webdriver.Chrome()

url_menu = HTML_FILE_PATH + "menu.html"
url_coffee = HTML_FILE_PATH + "coffee.html"

# [1] このタブは1つめなので driver.window_handles[0]
driver.get(url_menu)
time.sleep(1)
# [2] このタブは2つめなので driver.window_handles[1]
driver.execute_script("window.open('" + url_coffee + "')")
# [3] 2つめのタブに移動
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print(driver.title)
# [4] 1つめのタブに移動
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
print(driver.title)
# [5] 2つめのタブに移動と閉じる
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(3)
driver.quit()
