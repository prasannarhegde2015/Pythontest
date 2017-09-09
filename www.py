from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


def entervalueintxtid(driver , ee,val):
	driver.find_element_by_id(ee).send_keys(val)
	return
    

driver = webdriver.Chrome('E:\\Prasanna\\JavaTutorial\\Selenium\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev23478.service-now.com/")
driver.maximize_window()
assert "ServiceNow" in driver.title
driver.switch_to_frame("gsft_main")
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("ServiceNow97bd916$")
driver.find_element_by_name("not_important").click()
driver.switch_to.default_content()
try:
    element = WebDriverWait(driver, 300).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, "gsft_main"))
    )
except Exception as e:
    print ("Cannot swith to Frame by "+ str(e))
try:
    element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'10 Things')]")))
   
except Exception as e:
    print ("This is an error message!"+  str(e))
driver.switch_to.default_content()
driver.switch_to_frame("gsft_nav")
driver.find_element_by_link_text("Incidents").click()
driver.switch_to.default_content()
driver.switch_to_frame("gsft_main")
driver.find_element_by_id("sysverb_new").click()
driver.find_element_by_id("incident.number").clear()
entervalueintxtid(driver , "incident.number","Pyhton")
entervalueintxtid(driver , "incident.short_description","Pyhton Desc")
entervalueintxtid(driver , "incident.comments","hello world")
driver.find_element_by_id("sysverb_insert").click()
time.sleep(5)
driver.find_element_by_link_text("Pyhton").click()
driver.find_element_by_id("sysverb_delete").click()
try:
    element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "ok_button"))) 
except Exception as e:
    print ("This is an error message!"+  str(e))
driver.find_element_by_id("ok_button").click()
driver.switch_to.default_content()
try:
    element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "gsft_logout")))
except Exception as e:
    print ("This is an error message!"+  str(e))

driver.find_element_by_id("gsft_logout").click()
driver.close()
driver.quit()