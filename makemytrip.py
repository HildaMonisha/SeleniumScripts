from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\chromedriver")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("Del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
#driver.find_element_by_xpath("//p[text()='Bangalore, India']")
for city in cities:
    if city.text == "Bangalore, India":
        city.click()
        break
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()






