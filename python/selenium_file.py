# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
from path.path import *

url = HTML_FILE_PATH + "file.html"

driver = webdriver.Chrome()
driver.get(url)

upfile = "D:/独学/Python/Selenium+BeautifulSoup/project-selenium/html/test.txt"
time.sleep(3)

driver.find_element(By.NAME, "filename").send_keys(upfile)
time.sleep(3)
driver.quit()
