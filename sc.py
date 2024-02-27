#imports
import time
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver

#step 1
driver = webdriver.Firefox()
driver.get('https://twitter.com/mangorat4')
time.sleep(.5)
resp = driver.page_source

#step 2
class Details:
    def __init__(account, un, pw):
        account.un = un
        account.pw = pw[pw.find('"') + 1:]

#step 3
soup = BeautifulSoup(resp, 'html.parser')
ad = Details(soup.find("div",{"class":"r-1wvb978"}).text, soup.find("div",{"data-testid":"UserDescription"}).text)

#step 4
time.sleep(1)
pyautogui.press('tab', presses=4)

#step 5
pyautogui.write((ad.un[1:]))
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(ad.pw[:ad.pw.find('"')])
pyautogui.press('enter')
time.sleep(1)

#step 6
time.sleep(1)
pyautogui.press('tab', presses=17)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('this tweet is brought to you by a shitty python algorithm')
pyautogui.press('tab', presses=8)
pyautogui.press('enter')