import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Prudhvi\Desktop\TGO Automation stuff\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://avidpay.timberscango.com/")
driver.implicitly_wait(10)
driver.find_element(By.NAME, 'username').send_keys('gouser2')
driver.find_element(By.NAME, 'password').send_keys('Core@123')
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(5)
driver.find_element(By.ID, 'menu').click()
driver.find_element(By.XPATH, "//body/app-root[1]/mat-sidenav-container[1]/mat-sidenav[1]/div[1]/app-nav-menu[1]/mat-nav-list[1]/app-nav-menu-item[5]/a[1]/div[1]").click()
driver.find_element(By.XPATH, "//body/app-root[1]/mat-sidenav-container[1]/mat-sidenav[1]/div[1]/app-nav-menu[1]/mat-nav-list[1]/app-nav-menu-item[5]/div[1]/app-nav-menu-item[1]/a[1]/div[1]").click()
drp = driver.find_element(By.XPATH, "//input[@size ='1']")
drp.click()
time.sleep(5)
drp.send_keys("invoice not ")
time.sleep(5)
drp.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
drp.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='Search']").click()
time.sleep(5)
invoices = driver.find_elements(By.TAG_NAME, "h5")
for invoice in invoices:
    time.sleep(4)
    print(invoice.text)
    time.sleep(6)
    if invoice.text.__contains__("Acquired on Feb 15"):
        time.sleep(4)
        invoice.click()



















