import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# verify main Page elements
def verify_main_page_elements(driver):
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

# API testing from Selenium
def check_api(driver):
    print ("Test Url has", requests.get ("https://qasvus.wixsite.com/ca-marketing").status_code, "as status Code")
    code=requests.get ("https://qasvus.wixsite.com/ca-marketing").status_code
    if code == 200:
        print ("API response code is OK")
    else:
        print ("API response code is not 200", "Current code is:", code)

