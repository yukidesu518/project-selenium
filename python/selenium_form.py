# -*- coding: utf-8 -*-
from selenium import webdriver
# selenium.webdriver.support.ui の Select をimport
from selenium.webdriver.support.ui import Select
# selenium.webdriver.common.alert の Alert をimport
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.by import By

from path.path import *

url = HTML_FILE_PATH + "coffee.html"

driver = webdriver.Chrome()
driver.get(url)

# プルダウン要素からSelectインスタンスを取得
element = driver.find_element(By.NAME, "num")
select_num = Select(element)

# select_by_value 等のメソッドで操作
select_num.select_by_value("2")
time.sleep(3)
element = driver.find_element(By.XPATH, "/html/body/form/input[1]")
element.click()
time.sleep(3)
chk_sugar = driver.find_element(By.CSS_SELECTOR, "input[name='included'][value='sugar']")
chk_milk = driver.find_element(By.CSS_SELECTOR, "input[name='included'][value='milk']")
chk_cream = driver.find_element(By.CSS_SELECTOR, "input[name='included'][value='cream']")
chk_sugar.click()
chk_cream.click()
time.sleep(3)
print(chk_milk.is_selected())
print(chk_cream.is_selected())
element = driver.find_element(By.NAME, "remarks")
element.send_keys("やや熱めでお願いします")
time.sleep(3)
elements = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
# elements = driver.find_element(By.CSS_SELECTOR, "input[type='reset']")
elements.click()
# ドライバからAlertインスタンスを取得し、acceptメソッドでOK押下
Alert(driver).accept()
time.sleep(5)
driver.quit()
