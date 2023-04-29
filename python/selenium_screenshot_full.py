# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from path.path import *

# headlessモードにする
options = Options()
options.add_argument('--headless')

url = HTML_FILE_PATH + "javascript.html"

driver = webdriver.Chrome(options=options)
driver.get(url)

# ウィンドウサイズをブラウザ表示域にする
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(w, h)
driver.save_screenshot("screenshot_full.png")
driver.quit()