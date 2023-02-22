import pytest
from Utilities.BaseClass import BaseClass
from Pages.GooglePage import googleP

class Test_demoClass(BaseClass):

    @pytest.mark.parametrize("data",[pytest.param('this is a test for avshalom')])
    def test_one(self,data):
        google = googleP(self.driver)
        google.searchSomthing(data)
        self.waitFor(2)
        afterSearch = google.clickOnSearch()
        self.waitFor(3)
        afterSearch.clickOnFirstResult()
        self.waitFor(1)
        title = afterSearch.getTitleBack()
        assert title == self.expectedTitle


