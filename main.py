from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.aeso.ca/")

population = driver.find_element(By.CLASS_NAME, value='number')
print(population.text)

driver.quit()