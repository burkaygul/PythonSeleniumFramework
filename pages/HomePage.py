from selenium.webdriver.common.by import By

from pages.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop= (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.CSS_SELECTOR, "label[for='exampleCheck1']")
    gender = (By.XPATH, "//select[@class='form-control']")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage =(By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
