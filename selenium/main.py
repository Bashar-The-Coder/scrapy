# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# get google.co.in
driver.get("https://google.co.in")
print (driver.title)
print (driver.page_source)

driver.