import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
import helpers as H

# driver sleep from 2 to 3 seconds
def delay():
    time.sleep (random.randint (2, 3))

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_search_chrome(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait(2)
        print(driver.current_url)
        print("Negative test for Google Chrome")
        print("TC009")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements (driver)

        # scroll to "Subscribe Form" form
        element=driver.find_element (By.XPATH, "//span[contains(text(),'Subscribe Form')]")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        # enter 10 times enter integer 7 in "email field"
        driver.find_element(By.XPATH, "//input[@id='input_comp-ldls1eyf']").send_keys("7777777")

        # click "Submit" button
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div[@id='masterPage']/footer[@id='SITE_FOOTER_WRAPPER']/div[@id='SITE_FOOTER']/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/button[1]")

        # verify alert "Please fill in a valid email address" is visible
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".font_0 > .wixui-rich-text__text > .color_15")))

        # API testing from Selenium
        H.check_api (driver)

        print("TC009 is PASSED")

    def tearDown(self):
        self.driver.quit()

class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_search_edge(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait(2)
        print(driver.current_url)
        print("Negative test for Google Chrome")
        print("TC009")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements (driver)

        # scroll to "Subscribe Form" form
        element=driver.find_element (By.XPATH, "//span[contains(text(),'Subscribe Form')]")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        # enter 10 times enter integer 7 in "email field"
        driver.find_element(By.XPATH, "//input[@id='input_comp-ldls1eyf']").send_keys("7777777")

        # click "Submit" button
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div[@id='masterPage']/footer[@id='SITE_FOOTER_WRAPPER']/div[@id='SITE_FOOTER']/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/button[1]")

        # verify alert "Please fill in a valid email address" is visible
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".font_0 > .wixui-rich-text__text > .color_15")))

        # API testing from Selenium
        H.check_api (driver)

        print("TC009 is PASSED")

    def tearDown(self):
        self.driver.quit()

class FireFoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_search_firefox(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait(2)
        print(driver.current_url)
        print("Negative test for Google Chrome")
        print("TC009")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # scroll to "Subscribe Form" form
        element=driver.find_element (By.XPATH, "//span[contains(text(),'Subscribe Form')]")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        # enter 10 times enter integer 7 in "email field"
        driver.find_element(By.XPATH, "//input[@id='input_comp-ldls1eyf']").send_keys("7777777")

        # click "Submit" button
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div[@id='masterPage']/footer[@id='SITE_FOOTER_WRAPPER']/div[@id='SITE_FOOTER']/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/button[1]")

        # verify alert "Please fill in a valid email address" is visible
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".font_0 > .wixui-rich-text__text > .color_15")))

        # API testing from Selenium
        H.check_api (driver)

        print("TC009 is PASSED")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main ()


