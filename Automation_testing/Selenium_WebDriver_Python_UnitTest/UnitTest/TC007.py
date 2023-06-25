import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        print("TC007")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".jjPduP")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".YT_9QV")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click in Header "Log in"
        driver.find_element(By.CSS_SELECTOR, ".YT_9QV").click()
        # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click "Log in" link
        driver.find_element(By.CSS_SELECTOR, ".qufiy3").click()
        # Click "Log in with email"
        driver.find_element(By.XPATH, "//div[4]/div/button/span").click()

        # Enter valid email and password
        driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP742").send_keys("testikgmail")
        time.sleep (2)
        driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP742").send_keys("testik")
        time.sleep (2)

        # Click "Log in" button
        driver.find_element(By.ID, "okButton_SM_ROOT_COMP742").click()
        time.sleep(2)

        # verify and print "Double-check your email and try again." is present
        print (driver.find_element (By.ID, "siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP745").text)

        # click Close current window
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[6]/div[2]/button[1]")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print("Page Title is: ", driver.title)

        # verify User got in account
        assert "testik" in driver.page_source
        driver.find_element(By.XPATH, "//*[@id='comp-k00e6z1w']")
        print('User got into Account')

        # API testing from Selenium
        H.check_api (driver)

        print("TC007 is PASSED")

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
        print("TC007")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".jjPduP")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".YT_9QV")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click in Header "Log in"
        driver.find_element(By.CSS_SELECTOR, ".YT_9QV").click()
        # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click "Log in" link
        driver.find_element(By.CSS_SELECTOR, ".qufiy3").click()
        # Click "Log in with email"
        driver.find_element(By.XPATH, "//div[4]/div/button/span").click()

        # Enter valid email and password
        driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP742").send_keys("testikgmail")
        time.sleep (2)
        driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP742").send_keys("testik")
        time.sleep (2)

        # Click "Log in" button
        driver.find_element(By.ID, "okButton_SM_ROOT_COMP742").click()
        time.sleep(2)

        # verify and print "Double-check your email and try again." is present
        print (driver.find_element (By.ID, "siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP745").text)

        # click Close current window
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[6]/div[2]/button[1]")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print("Page Title is: ", driver.title)

        # verify User got in account
        assert "testik" in driver.page_source
        driver.find_element(By.XPATH, "//*[@id='comp-k00e6z1w']")
        print('User got into Account')

        # API testing from Selenium
        H.check_api (driver)

        print("TC007 is PASSED")

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
        print("TC007")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print ("Page Title is: ", driver.title)

        # verify main Page Title elements
        H.verify_main_page_elements(driver)

        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".jjPduP")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # # mouseOver
        element = driver.find_element(By.CSS_SELECTOR, ".YT_9QV")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click in Header "Log in"
        driver.find_element(By.CSS_SELECTOR, ".YT_9QV").click()
        # mouseOut
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Click "Log in" link
        driver.find_element(By.CSS_SELECTOR, ".qufiy3").click()
        # Click "Log in with email"
        driver.find_element(By.XPATH, "//div[4]/div/button/span").click()

        # Enter valid email and password
        driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP742").send_keys("testikgmail")
        time.sleep (2)
        driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP742").send_keys("testik")
        time.sleep (2)

        # Click "Log in" button
        driver.find_element(By.ID, "okButton_SM_ROOT_COMP742").click()
        time.sleep(2)

        # verify and print "Double-check your email and try again." is present
        print (driver.find_element (By.ID, "siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP745").text)

        # click Close current window
        driver.find_element(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[6]/div[2]/button[1]")

        # verify main Page Title
        assert "Home | California Marcketing" in driver.title
        print("Page Title is: ", driver.title)

        # verify User got in account
        assert "testik" in driver.page_source
        driver.find_element(By.XPATH, "//*[@id='comp-k00e6z1w']")
        print('User got into Account')

        # API testing from Selenium
        H.check_api (driver)

        print("TC007 is PASSED")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main ()


