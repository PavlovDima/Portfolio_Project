import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers as H

# driver sleep from 2 to 3 seconds
def delay():
    time.sleep (random.randint (2, 3))

class ChromeSearch (unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome (service=Service (ChromeDriverManager ().install ()))
        self.driver.maximize_window ()

    def test_search_chrome(self):
        driver=self.driver
        self.driver.get ("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait (3)
        print (driver.current_url)
        print ("Positive test for Google Chrome")
        print ("TC003")

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
            print("Let's Chat! button is PRESENT")
        except TimeoutException:
            print("Let's Chat! button is NOT present")

        # wait until button "Let's Chat!" will be clickable and click
        time.sleep (5)
        # wait=WebDriverWait (driver, 10)
        # wait.until (EC.element_to_be_clickable ((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
        # element = driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        # driver.execute_script("arguments[0].click();", element)

        element=driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        actions=ActionChains (driver)
        actions.move_to_element (element).click()
        time.sleep (5)

        # find Input field
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').click ()

        # type Hello!
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').send_keys ("Hello!")

        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # click "Icons" button
        driver.find_element (By.CSS_SELECTOR, ".sk1yM:nth-child(2) svg").click ()
        # pick icon
        driver.find_element (By.CSS_SELECTOR, ".Y4ceR:nth-child(12)").click ()
        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # close "Chat" window
        driver.find_element (By.CSS_SELECTOR, ".Toy\\+3 path").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC003 is PASSED")

    def teardown_method(self):
        self.driver.quit ()

class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window ()

    def test_search_edge(self):
        driver=self.driver
        self.driver.get ("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait (3)
        print (driver.current_url)
        print ("Positive test for Google Chrome")
        print ("TC003")

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
            print("Let's Chat! button is PRESENT")
        except TimeoutException:
            print("Let's Chat! button is NOT present")

        # wait until button "Let's Chat!" will be clickable and click
        time.sleep (5)
        # wait=WebDriverWait (driver, 10)
        # wait.until (EC.element_to_be_clickable ((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
        # element = driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        # driver.execute_script("arguments[0].click();", element)

        element=driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        actions=ActionChains (driver)
        actions.move_to_element (element).click()
        time.sleep (5)

        # find Input field
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').click ()

        # type Hello!
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').send_keys ("Hello!")

        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # click "Icons" button
        driver.find_element (By.CSS_SELECTOR, ".sk1yM:nth-child(2) svg").click ()
        # pick icon
        driver.find_element (By.CSS_SELECTOR, ".Y4ceR:nth-child(12)").click ()
        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # close "Chat" window
        driver.find_element (By.CSS_SELECTOR, ".Toy\\+3 path").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC003 is PASSED")

    def teardown_method(self):
        self.driver.quit ()

class FireFoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window ()

    def test_search_firefox(self):
        driver=self.driver
        self.driver.get ("https://qasvus.wixsite.com/ca-marketing")

        # wait max 2 sec for page loading
        driver.implicitly_wait (3)
        print (driver.current_url)
        print ("Positive test for Google Chrome")
        print ("TC003")

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
            print("Let's Chat! button is PRESENT")
        except TimeoutException:
            print("Let's Chat! button is NOT present")

        # wait until button "Let's Chat!" will be clickable and click
        time.sleep (5)
        # wait=WebDriverWait (driver, 10)
        # wait.until (EC.element_to_be_clickable ((By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")))
        # element = driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        # driver.execute_script("arguments[0].click();", element)

        element=driver.find_element (By.XPATH, "//div[@id='bgLayers_comp-k00d6wwm1']//div[@class='LWbAav Kv1aVt']")
        actions=ActionChains (driver)
        actions.move_to_element (element).click()
        time.sleep (5)

        # find Input field
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').click ()

        # type Hello!
        driver.find_element (By.XPATH, '//*[@aria - label="Type your message. Hit enter to submit."]').send_keys ("Hello!")

        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # click "Icons" button
        driver.find_element (By.CSS_SELECTOR, ".sk1yM:nth-child(2) svg").click ()
        # pick icon
        driver.find_element (By.CSS_SELECTOR, ".Y4ceR:nth-child(12)").click ()
        # click "Send" button
        driver.find_element (By.CSS_SELECTOR, ".S66IV path").click ()
        # close "Chat" window
        driver.find_element (By.CSS_SELECTOR, ".Toy\\+3 path").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC003 is PASSED")

    def teardown_method(self):
        self.driver.quit ()

if __name__ == "__main__":
    unittest.main ()
