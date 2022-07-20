from selenium.webdriver.common.by import By


class Login:
    Textbox_username_name = "username"
    Textbox_password_name = "password"
    Button_login_xpath = "//button[text()='Login']"
    Home_menu_icon_id = "menu"
    Button_logout_Css = ".icon-sign-out"
    Button_About_linktext = "About"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.Textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.Textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.Textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.Textbox_password_name).send_keys(password)

    def clickLogin_button(self):
        self.driver.find_element(By.XPATH, self.Button_login_xpath).click()

    def clickMenu(self):

        self.driver.find_element(By.ID, self.Home_menu_icon_id).click()

    def clickLogout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.Button_logout_Css).click()

    def clickAbout(self):
        self.driver.find_element(By.LINK_TEXT, self.Button_About_linktext).click()






