from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.find_element_by_css_selector("input[name='email']").send_keys("hildamoni@gmail.com")
#driver.find_element_by_name("email").send_keys("hildamoni@gmail.com")
driver.find_element_by_name("pass").send_keys("geetharaj")
dropdown=Select(driver.find_element_by_id("month"))
dropdown.select_by_visible_text("Feb")
#driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_class_name("_50f6").text)
#for css- "span=[class='_50f6]"
#for xpath "//span=[@class='_50f6]"