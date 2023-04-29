# -*- coding: utf-8 -*-



# エラー処理なし
# テキスト読み上げ速度が遅い
# 


#seleniumのimport
from selenium import webdriver
#timeのimport
import time
#seleniumの要素取得に必要なやつ
from selenium.webdriver.common.by import By
#BeautifulSoupのimport
from bs4 import BeautifulSoup
#TTS実装用ライブラリ
from gtts import gTTS
#TTSで作成したMP3を読み上げるライブラリ
from playsound import playsound
#tcuアカウントのidとパスワードを格納してる.pyをインポート
from tcu_pass import *
#作成したMP3を削除するため
import os
import copy

#ポータルサイトURL
url = "https://portal.off.tcu.ac.jp/OldIndex.aspx"

#同階層のtcu_pass.pyに
# tcu_id = 〇〇〇〇
# tcu_pass = 〇〇〇〇
#の形式で保存（Gitにはあげない）したものを読み込む
tcu_id = tcu_id
tcu_pass = tcu_pass

#seleniumの準備
ChromeOptions = webdriver.ChromeOptions()
#上に表示される自動で制御されてます的なテキストの削除と変なエラーの非表示設定
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])

#上で設定したオプションの反映とドライバの準備
driver = webdriver.Chrome(options=ChromeOptions)
#指定したurlを取得
driver.get(url)

#ログインに必要な要素の取得
element_id = driver.find_element(By.CSS_SELECTOR, "#txtLoginId")
element_pass = driver.find_element(By.CSS_SELECTOR, "#txtPassword")
element_login_btn = driver.find_element(By.CSS_SELECTOR, "#btnLogin")

time.sleep(1)
element_id.send_keys(tcu_id)#id入力
time.sleep(1)
element_pass.send_keys(tcu_pass)#パスワード入力
time.sleep(1)
element_login_btn.click()#ログインボタンクリック
time.sleep(1)

driver.implicitly_wait(10)


#解析用htmlをseleniumで取得
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


for idx, element in enumerate(driver.find_elements(By.CSS_SELECTOR, "#MainContent_Contents_newsOshirase > li > div:nth-child(4) > a")):
    if os.path.isfile("yomiage.mp3"):
        os.remove("yomiage.mp3")

    time.sleep(1)
    element.click()

    driver.implicitly_wait(10)

    driver.switch_to.window(driver.window_handles[1])

    title = driver.find_element(By.CSS_SELECTOR, "#MainContent_Contents_lblTitle")

    print(title.text + "\n")

    text = str(idx + 1) + "。" + title.text
    tts = gTTS(text=text, lang="ja", slow=False)
    tts.save('yomiage.mp3')

    playsound('yomiage.mp3')

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    
    time.sleep(1)

os.remove("yomiage.mp3")

tts = gTTS(text="最新20件のお知らせは以上です", lang="ja", slow=False)
tts.save('yomiage.mp3')

playsound('yomiage.mp3')


time.sleep(3)

driver.quit()