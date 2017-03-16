from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://habrahabr.ru")

driver.find_element_by_xpath("//a[@href='https://habrahabr.ru/auth/register/']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@name='email']").send_keys("no_bot@gmail.com")
driver.find_element_by_xpath("//input[@name='login']").send_keys("no_bot")
driver.find_element_by_xpath("//input[@name='password']").send_keys("123123")
driver.find_element_by_xpath("//input[@name='password2']").send_keys("123123")

driver.quit()
