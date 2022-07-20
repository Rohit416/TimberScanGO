from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DataEntry:

    DataEntry_menu_xpath = "//body/app-root[1]/mat-sidenav-container[1]/mat-sidenav[1]/div[1]/app-nav-menu[1]/mat-nav-list[1]/app-nav-menu-item[4]/a[1]/div[1]/i[1]"
    Primary_submenu_xpath = "/html/body/app-root/mat-sidenav-container/mat-sidenav/div/app-nav-menu/mat-nav-list/app-nav-menu-item[4]/div/app-nav-menu-item[1]/a/div/i"
    Invoice_search_dropdown_xpath = "//input[@size ='1']"
    Search_button_xpath = "//button[@type ='submit']"
    Invoice_css = "body.ng-tns-0-15:nth-child(2) mat-sidenav-container.mat-drawer-container.mat-sidenav-container.mat-drawer-transition mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted:nth-child(5) div.container-fluid app-data-entry-list.ng-star-inserted:nth-child(2) div.row.ng-star-inserted:nth-child(3) div.col-sm-12.col-md-4.col-lg-3.col-xl-2.ng-star-inserted:nth-child(1) div.card.h-100.cursor-pointer div.card-body app-document-page-viewer.ng-star-inserted ngb-carousel.carousel.slide.ng-star-inserted div.carousel-inner div.carousel-item.active.ng-star-inserted div.ng-star-inserted > img.card-img-top.ng-star-inserted"

    def __init__(self, driver):
        self.driver = driver

    def clickDataEntry_menu(self):
        self.driver.find_element(By.XPATH, self.DataEntry_menu_xpath).click()

    def clickPrimary(self):
        self.driver.find_element(By.XPATH, self.Primary_submenu_xpath).click()

    def select_InvoiceType(self, invoiceoption):
        drp = self.driver.find_element(By.XPATH, self.Invoice_search_dropdown_xpath)
        drp.click()
        drp.send_keys(invoiceoption)
        drp.send_keys(Keys.ARROW_DOWN)
        drp.send_keys(Keys.ENTER)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.Search_button_xpath).click()

    def scroll_invoices(self):

        flag = self.driver.find_element(By.XPATH, '//body/app-root[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div[2]/app-data-entry-list[1]/div[2]/div[18]/app-data-entry-card[1]/div[1]/div[2]/app-document-page-viewer[1]/ngb-carousel[1]/div[1]/div[1]/div[1]/img[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        flag.click()

    def select_All_invoices_option(self, Invoiceserachoption2):
        drp = self.driver.find_element(By.XPATH, self.Invoice_search_dropdown_xpath)
        drp.click()
        drp.send_keys(Invoiceserachoption2)
        drp.send_keys(Keys.ARROW_DOWN)
        drp.send_keys(Keys.ENTER)

    def click_invoice_image(self):
        self.driver.find_element(By.CSS_SELECTOR, self.Invoice_css).click()


















