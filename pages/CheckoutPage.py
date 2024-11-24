from selenium.webdriver.common.by import By

from pages.ConfirmPage import ConfirmPage


class CheckoutPage:

    cardTitle = (By.XPATH,"//div[@class='card h-100']")
    cardFooter =(By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    def __init__(self,driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
        #driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
