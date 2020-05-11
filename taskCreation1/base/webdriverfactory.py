"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        #baseURL = "https://devdojo.branch1.release.taskbench.com/login"
        baseURL = "https://devdojo.test.taskbench.com/login"

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\Users\\Taskbench_1012\\workspace_python\\drivers\\geckodriver.exe")
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()


        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)

        return driver