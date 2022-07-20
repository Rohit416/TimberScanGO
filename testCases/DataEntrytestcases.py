import time
from selenium import  webdriver
from pageObjects.LoginScreen import Login
from pageObjects.HomeScreen import Home
from pageObjects.DataEntrypageobjects import DataEntry
import pytest
from utilities.readProperties import ReadConfig


class Test_DataEntry:
    baseURl = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    invoiceoption = 'invoice not coded yet'
    Invoiceserachoption2 = 'All'

    # def test_DataEntry_menu(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURl)
    #     lp = Login(self.driver)
    #     lp.setUsername(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin_button()
    #     hp = Home(self.driver)
    #     hp.clickMenu()
    #     de = DataEntry(self.driver)
    #     de.clickDataEntry_menu()

    # def test_Primary_submenu(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURl)
    #     lp = Login(self.driver)
    #     lp.setUsername(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin_button()
    #     hp = Home(self.driver)
    #     hp.clickMenu()
    #     de = DataEntry(self.driver)
    #     de.clickDataEntry_menu()
    #     de.clickPrimary()

    # def test_invoice_type(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURl)
    #     lp = Login(self.driver)
    #     lp.setUsername(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin_button()
    #     hp = Home(self.driver)
    #     hp.clickMenu()
    #     de = DataEntry(self.driver)
    #     de.clickDataEntry_menu()
    #     de.clickPrimary()
    #     de.select_InvoiceType(self.invoiceoption)
    #     de.click_search_button()
    #     de.scroll_invoices()

    def test_All_invoice(self, setup):
        self.driver = setup
        self.driver.get(self.baseURl)
        lp = Login(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin_button()
        hp = Home(self.driver)
        time.sleep(2)
        hp.clickMenu()
        time.sleep(2)
        de = DataEntry(self.driver)
        time.sleep(2)
        de.clickDataEntry_menu()
        de.clickPrimary()
        # de.select_InvoiceType(self.invoiceoption)
        de.select_All_invoices_option(self.Invoiceserachoption2)
        de.click_search_button()

