# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
from path.path import *

url = HTML_FILE_PATH + "javascript.html"
driver = webdriver.Chrome()

driver.get(url)

# [1] JavaScript で計算しアラートで表示
driver.execute_script("ans = 1 +1 ; alert(ans);")
time.sleep(3)
# [2] アラートのOK押下
Alert(driver).accept()
# [3] myfunc関数実行
driver.execute_script("myfunc(ans);")
time.sleep(3)
Alert(driver).accept()
# [4] スクロール
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.quit()
