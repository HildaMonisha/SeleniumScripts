from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.title)    #get the title of the weppage
print(driver.current_url)    #to recheck the correct url
driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar")
var = driver.find_element_by_xpath("//h2[text()='Find Your Account']").text
assert "Accokjhrkhghjunt" in var
#driver.minimize_window()
#driver.back()
driver.refresh()
#driver.close()


