from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
options = ChromeOptions()
# options.headless = True
driver = Chrome(executable_path=r"F:\WEB-Scraping\project\webs\selenium\driver\chromedriver.exe",
                options=options)

driver.get('https://directory.ntschools.net/#/schools')
time.sleep(10)
selector = '#search-panel-container .nav-link'
links = WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
)
results = []
school_name_selector = '.school-title ~  h1'
for i in range(2):
    links = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
    )
    links[i].click()
    name_e = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, school_name_selector))
    )
    details = {
        'name': name_e.text,
        'ph_address': driver.find_element(By.XPATH , '//div[text()="Physical Address"]/following-sibling::div').text,
        'po_address': driver.find_element(By.XPATH, '//*[text()="Postal Address"]/following-sibling::*').text,
        'phone': driver.find_element(By.XPATH, '//*[text()="Phone"]/following-sibling::*/a').text,
    }
    results.append(details)
    WebDriverWait(driver, 60)
    driver.back()
driver.quit()

with open('schools_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f,
                            fieldnames=['name', 'ph_address', 'po_address', 'phone'])
    writer.writeheader()
    writer.writerows(results)