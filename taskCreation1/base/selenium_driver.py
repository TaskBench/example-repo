from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilites.custom_logger as cl
from selenium import webdriver
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
import pyautogui


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.resultList = []

    def getTitle(self):
        return self.driver.title


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()


    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=2, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable"+ locator + locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
            elementresult = self.elementClick(locator, locatorType=byType)
            return True

        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
            return False


    def waitSendkeys(self, keys, locator, locatorType, timeout=60, pollFrequency=0.5):
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable" + locator + locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.presence_of_element_located((byType, locator))).send_keys(keys)
            # query = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency).until(
            #     EC.presence_of_element_located((byType, locator)))
            # query.send_keys('python')
            self.log.info("Values sended to the element")
            #assert True == True
            return True
        except:
            self.log.error("Unable to send the values to the element" + keys)
            #assert True == False
            return False


    def getTaskResult(self, locator, id, locatorType, timeout=4, pollFrequency=0.5):
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable" + locator + locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.text_to_be_present_in_element((byType, locator),"Task created successfully."))
            self.log.info("Test case success: Test case id=" + str(id))
            assert True == True
            return True
        except:
            self.log.error("Element not appeared on the web page")
            self.log.error("Test case failed: Test case id=" + str(id))
            assert True == False
            return False


    def getTempResult(self, locator, id, locatorType, timeout=4, pollFrequency=0.5):
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable" + locator + locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.text_to_be_present_in_element((byType, locator),"New template created successfully."))
            self.log.info("Test case success: Test case id=" + str(id))
            assert True == True
            return True
        except:
            self.log.error("Element not appeared on the web page")
            self.log.error("Test case failed: Test case id=" + str(id))
            assert True == False
            return False

    # def getText(self, locator):
    #     try:
    #         element = self.driver.find_element_by_xpath(locator).text
    #         self.log.info("Found the element" + element)
    #         return True
    #     except:
    #         self.log.error("Element not found to take the text")
    #         return False