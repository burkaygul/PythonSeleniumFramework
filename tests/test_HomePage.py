import pytest

from TestData.HomePageData import HomePageData
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.info("first name is "+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckBox().click()

        self.selectOptipnByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param









