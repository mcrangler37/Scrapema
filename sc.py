#imports
import time
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver

#step 1
startTime = time.time()
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
driver.get('https://twitter.com/i/flow/login')
time.sleep(.5)
pyautogui.press('tab', presses=4)

#step 5
pyautogui.write((ad.un[1:]))
pyautogui.press('enter')
time.sleep(.5)
pyautogui.write(ad.pw[:ad.pw.find('"')])
pyautogui.press('enter')
time.sleep(.75)

#step 6
driver.get('https://twitter.com/mangorat4')
time.sleep(.75)
pyautogui.press('tab', presses=17)
pyautogui.press('enter')
time.sleep(.75)
pyautogui.write('this tweet was entirely written by a python script i made to log in to my account and tweet this for me because im literally just that lazy')
pyautogui.press('tab', presses=8)
#pyautogui.press('enter')
endTime = time.time()
print('finished in ' + str((int(100 * (endTime - startTime))) / 100) + ' seconds')