from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://twitter.com/mangorat4?lang=en")

driver.quit()