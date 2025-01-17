# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from path.path import *

url = HTML_FILE_PATH + "menu.html"
driver = webdriver.Chrome(../webdriver/)
driver.get(url)
# テキストリンクがCoffeeの要素を取得しクリック
element = driver.find_element(By.LINK_TEXT, "Coffee")
element.click()
time.sleep(1)
# ページ更新
driver.refresh()
time.sleep(1)
# 前に戻る
driver.back()
time.sleep(1)
# 次に進む
driver.forward()
print(driver.current_url)
time.sleep(3)
driver.quit()
