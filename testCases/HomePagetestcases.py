import pytest
from selenium import webdriver
from pageObjects.LoginScreen import Login
from utilities.readProperties import ReadConfig
from pageObjects.HomeScreen import Home


class Test_Home:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_Menu_click(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = Login(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin_button()
        hp = Home(self.driver)
        hp.clickMenu()

    def test_User_profile(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = Login(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin_button()
        hp = Home(self.driver)
        hp.clickMenu()
        hp.clickUserprofile()
