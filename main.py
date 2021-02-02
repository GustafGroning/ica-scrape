from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/Gustaf/Desktop/HQ/Work/Programming/webdriver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://tynan.com/")

