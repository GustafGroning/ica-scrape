from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


ingredientser = input("vilka ingredienser? skriver enligt (ingrediens1, ingrediens2, osv)")

PATH = "/Users/Gustaf/Desktop/HQ/Work/Programming/webdriver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ica.se/recept/")

search_ingredients = driver.find_element_by_id("search2") # id for ingredient form = search2
search_ingredients.send_keys(ingredientser)


button_press = driver.find_element_by_id("search-button") # id for confirmation button = search-button
button_press.send_keys(Keys.RETURN)


