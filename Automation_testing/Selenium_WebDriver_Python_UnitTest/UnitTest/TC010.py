import time
import unittest
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import helpers as H

class ChromeSearch (unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome (service=Service (ChromeDriverManager ().install ()))
        self.driver.maximize_window ()

    def test_search_chrome(self):
      driver=self.driver
      driver.get ("https://qasvus.wixsite.com/ca-marketing")

      # wait max 2 sec for page loading
      driver.implicitly_wait (2)
      print (driver.current_url)
      print ("Negative test for Google Chrome")
      print ("TC010")

      # verify main Page Title
      assert "Home | California Marcketing" in driver.title
      print ("Page Title is: ", driver.title)

      # verify main Page Title elements
      H.verify_main_page_elements (driver)

      # click "Shop" in Main menu
      driver.find_element (By.ID, "comp-ldaaacya2label").click ()

      # verify QASV logo
      elements=driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")
      assert len (elements) > 0

      # verify "CALIFORNIA MARCKETING" text
      elements=driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")
      assert len (elements) > 0

      # verify "A Full-Stack Creative Agency in NY" text
      elements=driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")
      assert len (elements) > 0

      # find "I'm product 12" and click on it
      driver.find_element (By.CSS_SELECTOR, "li:nth-child(6) .naMHY_:nth-child(2) img").click ()

      # verify main picture of product 12
      elements=driver.find_elements (By.CSS_SELECTOR, ".slick-slide:nth-child(2) #get-image-item-id img")
      assert len (elements) > 0

      # type "0" in Quantity field
      # mouseDownAt css=.\_2uERl > input
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).click_and_hold ().perform ()
      # mouseMoveAt css=.\_2uERl > input
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).perform ()
      # mouseUpAt css=.\_2uERl > input
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).release ().perform ()
      # click css=.\_2uERl > input
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").clear()
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("0")

      # click in Quantity field
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()

      # click "Add to Cart" button
      driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
      time.sleep (3)

      # verify "Enter a minimum amount of 1" alert is present
      driver.find_elements (By.CSS_SELECTOR, ".CorePopover4063288344__popoverContent > div")

      # API testing from Selenium
      H.check_api (driver)

      print ("TC010 is PASSED")

    def teardown_method(self):
        self.driver.quit ()

class EdgeSearch(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    self.driver.maximize_window ()

  def test_search_edge(self):
    driver=self.driver
    driver.get ("https://qasvus.wixsite.com/ca-marketing")

    # wait max 2 sec for page loading
    driver.implicitly_wait (2)
    print (driver.current_url)
    print ("Negative test for Google Chrome")
    print ("TC010")

    # verify main Page Title
    assert "Home | California Marcketing" in driver.title
    print ("Page Title is: ", driver.title)

    # verify QASV logo
    driver.find_element (By.XPATH, '//*[@alt="iot_sq.png"]')

    # verify "CALIFORNIA MARCKETING" text
    driver.find_element (By.XPATH, "//a[contains(text(),'CALIFORNIA MARCKETING')]")

    # verify "A Full-Stack Creative Agency in NY" text
    driver.find_element (By.XPATH, "//a[contains(text(),'A Full-Stack Creative Agency in NY')]")

    # verify "LET CALIFORNIA MARKETING GROW YOUR BUSINECS" text
    driver.find_element (By.XPATH, "//span[contains(text(),'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')]")

    # Use exception NoSuchElementException to find QASV logo
    logo=driver.find_element (By.XPATH, '//*[@alt="iot_sq.png"]')
    try:
      logo
      print ("Main page logo is OK")
    except NoSuchElementException:
      print ("Main page logo is NOT OK!!!")

    # click "Shop" in Main menu
    driver.find_element (By.ID, "comp-ldaaacya2label").click ()

    # verify QASV logo
    elements=driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")
    assert len (elements) > 0

    # verify "CALIFORNIA MARCKETING" text
    elements=driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")
    assert len (elements) > 0

    # verify "A Full-Stack Creative Agency in NY" text
    elements=driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")
    assert len (elements) > 0

    # find "I'm product 12" and click on it
    driver.find_element (By.CSS_SELECTOR, "li:nth-child(6) .naMHY_:nth-child(2) img").click ()

    # verify main picture of product 12
    elements=driver.find_elements (By.CSS_SELECTOR, ".slick-slide:nth-child(2) #get-image-item-id img")
    assert len (elements) > 0

    # type "0" in Quantity field
    # mouseDownAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).click_and_hold ().perform ()
    # mouseMoveAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseUpAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).release ().perform ()
    # click css=.\_2uERl > input
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").clear ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("0")

    # click in Quantity field
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()

    # click "Add to Cart" button
    driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
    time.sleep (3)

    # verify "Enter a minimum amount of 1" alert is present
    driver.find_elements (By.CSS_SELECTOR, ".CorePopover4063288344__popoverContent > div")

    # API testing from Selenium
    print ("Test Url has", requests.get ("https://qasvus.wixsite.com/ca-marketing").status_code, "as status Code")
    code=requests.get ("https://qasvus.wixsite.com/ca-marketing").status_code
    if code == 200:
      print ("API response code is OK")
    else:
      print ("API response code is not 200", "Current code is:", code)

    print ("TC010 is PASSED")

  def teardown_method(self):
    self.driver.quit ()

class FireFoxSearch(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    self.driver.maximize_window ()

  def test_search_firefox(self):
    driver=self.driver
    driver.get ("https://qasvus.wixsite.com/ca-marketing")

    # wait max 2 sec for page loading
    driver.implicitly_wait (2)
    print (driver.current_url)
    print ("Negative test for Google Chrome")
    print ("TC010")

    # verify main Page Title
    assert "Home | California Marcketing" in driver.title
    print ("Page Title is: ", driver.title)

    # verify main Page Title elements
    H.verify_main_page_elements (driver)

    # click "Shop" in Main menu
    driver.find_element (By.ID, "comp-ldaaacya2label").click ()

    # verify QASV logo
    elements=driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")
    assert len (elements) > 0

    # verify "CALIFORNIA MARCKETING" text
    elements=driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")
    assert len (elements) > 0

    # verify "A Full-Stack Creative Agency in NY" text
    elements=driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")
    assert len (elements) > 0

    # find "I'm product 12" and click on it
    driver.find_element (By.CSS_SELECTOR, "li:nth-child(6) .naMHY_:nth-child(2) img").click ()

    # verify main picture of product 12
    elements=driver.find_elements (By.CSS_SELECTOR, ".slick-slide:nth-child(2) #get-image-item-id img")
    assert len (elements) > 0

    # type "0" in Quantity field
    # mouseDownAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).click_and_hold ().perform ()
    # mouseMoveAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseUpAt css=.\_2uERl > input
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).release ().perform ()
    # click css=.\_2uERl > input
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").clear ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("0")

    # click in Quantity field
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()

    # click "Add to Cart" button
    driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
    time.sleep (3)

    # verify "Enter a minimum amount of 1" alert is present
    driver.find_elements (By.CSS_SELECTOR, ".CorePopover4063288344__popoverContent > div")

    # API testing from Selenium
    H.check_api (driver)

    print ("TC010 is PASSED")

  def teardown_method(self):
    self.driver.quit ()

if __name__ == "__main__":
    unittest.main ()
