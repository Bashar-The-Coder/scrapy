# import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = """
            http://quotes.toscrape.com/js/
"""


driver = Chrome(executable_path=r"F:\WEB-Scraping\project\webs\selenium\driver\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(60)
selector = "(//a)[10]"
quotes = driver.find_element(By.XPATH, selector).click()
driver.implicitly_wait(60)
print (quotes)


time.sleep(5)