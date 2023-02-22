import pytest
from Utilities.BaseClass import BaseClass
from Pages.GooglePage import googleP

class Test_demoClass(BaseClass):

    def test_one(self):
        google = googleP(self.driver)
        google.searchSomthing('this is a test for Avshalom')
        self.waitFor(4)
        afterSearch = google.clickOnSearch()
        self.waitFor(3)
        afterSearch.clickOnFirstResult()

