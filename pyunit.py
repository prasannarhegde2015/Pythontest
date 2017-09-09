import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
def entervalueintxtid(driver , ee,val):
    driver.find_element_by_id(ee).send_keys(val)
    return
class ServiceNow(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome('E:\\Prasanna\\JavaTutorial\\Selenium\\chromedriver_win32\\chromedriver.exe')
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://dev23478.service-now.com/")
  
    def test_ado_login(self):
        self.assertTrue("ServiceNow" in self.driver.title, "Pass")
        try:
            self.element = WebDriverWait(self.driver, 300).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "gsft_main"))
            )
        except Exception as e:
            print ("Cannot swith to Frame by "+ str(e))
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame("gsft_main")
        self.driver.find_element_by_name("user_name").send_keys("admin")
        self.driver.find_element_by_name("user_password").send_keys("ServiceNow97bd916$")
        self.driver.find_element_by_name("not_important").click()
        self.driver.switch_to.default_content()
 
    def test_bclick_incidents(self):
        try:
            self.element = WebDriverWait(self.driver, 300).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "gsft_main"))
            )
        except Exception as e:
            print ("Cannot swith to Frame by "+ str(e))
        try:
            self.element = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'10 Things')]")))
           
        except Exception as e:
            print ("This is an error message!"+  str(e))
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame("gsft_nav")
        self.driver.find_element_by_link_text("Incidents").click()
        self.driver.switch_to.default_content()

    def test_bcreate_incidents(self):
        self.driver.switch_to_frame("gsft_main")
        self.driver.find_element_by_id("sysverb_new").click()
        self.driver.find_element_by_id("incident.number").clear()
        entervalueintxtid(self.driver , "incident.number","Pyhton")
        entervalueintxtid(self.driver , "incident.short_description","Pyhton Desc")
        entervalueintxtid(self.driver , "incident.comments","hello world")
        self.driver.find_element_by_id("sysverb_insert").click()        
        
    def test_ddelete_incidents(self):
        time.sleep(5)
        self.driver.find_element_by_link_text("Pyhton").click()
        self.driver.find_element_by_id("sysverb_delete").click()
        try:
            self.element = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.ID, "ok_button"))) 
        except Exception as e:
            print ("This is an error message!"+  str(e))
        self.driver.find_element_by_id("ok_button").click()
        self.driver.switch_to.default_content()
        
    def test_edo_logout(self):
        try:
            self.element = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.ID, "gsft_logout")))
        except Exception as e:
            print ("This is an error message!"+  str(e))
        self.driver.find_element_by_id("gsft_logout").click()
        
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()
 
if __name__ == '__main__':
    unittest.main()