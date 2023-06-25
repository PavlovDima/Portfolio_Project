from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
        print ("TC004")

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # mouseDownAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).click_and_hold ().perform ()
        # mouseMoveAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()
        # mouseUpAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).release ().perform ()

        # scroll to "Artist Name" section
        element=driver.find_element (By.XPATH, "// div[ @ id='bgLayers_comp-kcu66f4z1']")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        time.sleep(3)

        # click "Notify Me" button
        driver.find_element (By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR, ".ng-scope:nth-child(2) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR, ".ng-scope:nth-child(3) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC004 is FAILED")

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
        print ("TC004")

        # verify main Page Title elements
        H.verify_main_page_elements (driver)

        # mouseDownAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).click_and_hold ().perform ()
        # mouseMoveAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()
        # mouseUpAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).release ().perform ()

        # scroll to "Artist Name" section
        element=driver.find_element (By.XPATH, "// div[ @ id='bgLayers_comp-kcu66f4z1']")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        time.sleep (3)

        # click "Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(1) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(2) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(3) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC004 is FAILED")

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
        print ("TC004")

        # verify main Page Title elements
        H.verify_main_page_elements (driver)

        # mouseDownAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).click_and_hold ().perform ()
        # mouseMoveAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()
        # mouseUpAt
        element=driver.find_element (By.CSS_SELECTOR, "#bgLayers_comp-kcu66f4z1 > .LWbAav")
        actions=ActionChains (driver)
        actions.move_to_element (element).release ().perform ()

        # scroll to "Artist Name" section
        element=driver.find_element (By.XPATH, "// div[ @ id='bgLayers_comp-kcu66f4z1']")
        actions=ActionChains (driver)
        actions.move_to_element (element).perform ()

        time.sleep (3)

        # click "Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(1) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(2) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()
        # click another"Notify Me" button
        driver.find_element (By.CSS_SELECTOR,
                             ".ng-scope:nth-child(3) > .events:nth-child(1) .event-cell:nth-child(3) .ng-binding:nth-child(1)").click ()

        # API testing from Selenium
        H.check_api (driver)

        print ("TC004 is FAILED")

    def teardown_method(self):
        self.driver.quit ()

if __name__ == "__main__":
    unittest.main ()
