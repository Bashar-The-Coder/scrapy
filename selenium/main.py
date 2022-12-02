# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# get google.co.in
driver.get("https://google.co.in")
print (driver.title)
print (driver.page_source)
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.google.com')
# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')
# driver.close()
# print (driver.current_url)
