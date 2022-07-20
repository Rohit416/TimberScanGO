from selenium.webdriver.common.by import By


class Home:
    Menu_icon_id = "menu"
    Userprofile_xpath = '/html/body/app-root/mat-sidenav-container/mat-sidenav/div/app-nav-menu/mat-nav-list/app-nav-menu-item[1]/a/div/i'

    def __init__(self, driver):
        self.driver = driver

    def clickMenu(self):
        self.driver.find_element(By.ID, self.Menu_icon_id).click()

    def clickUserprofile(self):
        self.driver.find_element(By.XPATH, self.Userprofile_xpath).click()



