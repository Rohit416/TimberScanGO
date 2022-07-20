import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginScreen import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # def test_homepageTitle(self, setup):
    #     self.logger.info("*******************Test_001_Login***********")
    #     self.logger.info("******************* verifying Homepage title ***********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     Title = self.driver.title
    #
    #     if Title == 'TimberScan GO - Login':
    #         assert True
    #         self.logger.info("******************* homepage title test passed ***********")
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\" + "homepageTitlefail.png")
    #         self.driver.close()
    #         self.logger.info("******************* homepage title test failed ***********")
    #         assert False

    # def test_Login(self, setup):
    #     self.logger.info("*******************Test_002_Login***********")
    #     self.logger.info("******************* verifying login ***********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     lp = Login(self.driver)
    #     lp.setUsername(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin_button()
    #     self.logger.info("******************* Login test pass ***********")
    #     self.driver.close()

    def test_Logout(self, setup):
        self.logger.info("*******************Test_003_Logout***********")
        self.logger.info("******************* verifying log0ut ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = Login(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin_button()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.element_to_be_clickable(lp.clickMenu())) #EXPLICIT WAIT CONCEPT
        lp.clickMenu()
        lp.clickLogout_button()
        self.logger.info("******************* log0ut test passed ***********")
        self.driver.quit()
    #
    # def test_click_About(self, setup):
    #       self.logger.info("*******************Test_004_About***********")
    #       self.logger.info("******************* verifying About ***********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     lp = Login(self.driver)
    #     lp.clickAbout()
    #       self.logger.info("******************* log0ut test passed ***********")

