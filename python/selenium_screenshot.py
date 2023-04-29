# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from path.path import *

url = HTML_FILE_PATH + "javascript.html"

driver = webdriver.Chrome()
driver.get(url)

driver.save_screenshot("screenshot.png")
time.sleep(3)
driver.quit()
