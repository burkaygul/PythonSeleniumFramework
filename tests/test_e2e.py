import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3 import request
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):


    def test_e2e(self):

        log = self.getLogger()


        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")

        cards = checkoutpage.getCardTitles()
        i=-1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(card.text)
            if cardText == "Blackberry":
                checkoutpage.cardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='primary']").click()
        confirmPage = checkoutpage.checkOutItems()
        log.info("Entering country name as tur")

        self.driver.find_element(By.ID, "country").send_keys("tur")

        self.verifyLinkPresence("Turkey")

        self.driver.find_element(By.LINK_TEXT, "Turkey").click()

        self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()

        self.driver.find_element(By.XPATH, "//*[@type='submit']").click()

        actualText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+actualText)
        expectedText = "Success-!"

        assert expectedText in actualText

