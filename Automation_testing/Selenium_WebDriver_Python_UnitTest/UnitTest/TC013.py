import requests
import unittest
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
      print ("TC013")

      # verify main Page Title
      assert "Home | California Marcketing" in driver.title
      print ("Page Title is: ", driver.title)

      # verify main Page Title elements
      H.verify_main_page_elements (driver)

      # click "Shop" in Main menu
      driver.find_element (By.ID, "comp-ldaaacya2label").click ()

      # pick "I'm a product3"
      driver.find_element (By.CSS_SELECTOR, "li:nth-child(4) .naMHY_:nth-child(2) img").click ()

      # verify QASV logo
      driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")

      # verify "CALIFORNIA MARCKETING" text
      driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")

      # verify "A Full-Stack Creative Agency in NY" text
      driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")

      # verify main picture of product3
      driver.find_elements (By.CSS_SELECTOR, "[src='https://static.wixstatic.com/media/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg/v1/fill/w_1000,h_562,al_c,q_85,enc_auto/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg']")

      # enter "1000000" in Quantity field
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
      # mouseDownAt
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).click_and_hold ().perform ()
      # mouseMoveAt
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).perform ()
      # mouseUpAt
      element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
      actions=ActionChains (driver)
      actions.move_to_element (element).release ().perform ()

      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
      driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("1000000")

      # click "Add to Cart" button
      driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
      # mouseOver
      element=driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content")
      actions=ActionChains (driver)
      actions.move_to_element (element).perform ()
      # mouseOut
      element=driver.find_element (By.CSS_SELECTOR, "body")
      actions=ActionChains (driver)
      actions.move_to_element (element).perform ()

      # verify "Only 99999 left in stock" alert is present
      driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div")
      print(driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div"))

      # API testing from Selenium
      H.check_api (driver)

      print ("TC013 is PASSED")

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
    print ("TC013")

    # verify main Page Title
    assert "Home | California Marcketing" in driver.title
    print ("Page Title is: ", driver.title)

    # verify main Page Title elements
    H.verify_main_page_elements (driver)

    # click "Shop" in Main menu
    driver.find_element (By.ID, "comp-ldaaacya2label").click ()

    # pick "I'm a product3"
    driver.find_element (By.CSS_SELECTOR, "li:nth-child(4) .naMHY_:nth-child(2) img").click ()

    # verify QASV logo
    driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")

    # verify "CALIFORNIA MARCKETING" text
    driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")

    # verify "A Full-Stack Creative Agency in NY" text
    driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")

    # verify main picture of product3
    driver.find_elements (By.CSS_SELECTOR,
                          "[src='https://static.wixstatic.com/media/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg/v1/fill/w_1000,h_562,al_c,q_85,enc_auto/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg']")

    # enter "1000000" in Quantity field
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    # mouseDownAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).click_and_hold ().perform ()
    # mouseMoveAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseUpAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).release ().perform ()

    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("1000000")

    # click "Add to Cart" button
    driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
    # mouseOver
    element=driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseOut
    element=driver.find_element (By.CSS_SELECTOR, "body")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()

    # verify "Only 99999 left in stock" alert is present
    driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div")
    print (driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div"))

    # API testing from Selenium
    H.check_api (driver)

    print ("TC013 is PASSED")

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
    print ("TC013")

    # verify main Page Title
    assert "Home | California Marcketing" in driver.title
    print ("Page Title is: ", driver.title)

    # verify main Page Title elements
    H.verify_main_page_elements (driver)

    # click "Shop" in Main menu
    driver.find_element (By.ID, "comp-ldaaacya2label").click ()

    # pick "I'm a product3"
    driver.find_element (By.CSS_SELECTOR, "li:nth-child(4) .naMHY_:nth-child(2) img").click ()

    # verify QASV logo
    driver.find_elements (By.CSS_SELECTOR, "#img_comp-ldaaabct3 > img")

    # verify "CALIFORNIA MARCKETING" text
    driver.find_elements (By.LINK_TEXT, "CALIFORNIA MARCKETING")

    # verify "A Full-Stack Creative Agency in NY" text
    driver.find_elements (By.LINK_TEXT, "A Full-Stack Creative Agency in NY")

    # verify main picture of product3
    driver.find_elements (By.CSS_SELECTOR,
                          "[src='https://static.wixstatic.com/media/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg/v1/fill/w_1000,h_562,al_c,q_85,enc_auto/3c76e2_8891bbe3372a428aac976ac59aa0ac74~mv2.jpg']")

    # enter "1000000" in Quantity field
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    # mouseDownAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).click_and_hold ().perform ()
    # mouseMoveAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseUpAt
    element=driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input")
    actions=ActionChains (driver)
    actions.move_to_element (element).release ().perform ()

    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").click ()
    driver.find_element (By.CSS_SELECTOR, ".\\_2uERl > input").send_keys ("1000000")

    # click "Add to Cart" button
    driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content").click ()
    # mouseOver
    element=driver.find_element (By.CSS_SELECTOR, ".CoreButtonNext960945004__content")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()
    # mouseOut
    element=driver.find_element (By.CSS_SELECTOR, "body")
    actions=ActionChains (driver)
    actions.move_to_element (element).perform ()

    # verify "Only 99999 left in stock" alert is present
    driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div")
    print (driver.find_elements (By.CSS_SELECTOR, ".clickOutside11 > .CorePopover4063288344__popoverContent > div"))

    # API testing from Selenium
    H.check_api (driver)

    print ("TC013 is PASSED")

  def teardown_method(self):
    self.driver.quit ()

if __name__ == "__main__":
    unittest.main ()
