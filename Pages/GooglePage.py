from selenium.webdriver.common.by import By
from Pages.afterSearchPage import afterSearch


class googleP:
    searchField = (By.CLASS_NAME, 'gLFyf')
    search_btn = (By.NAME, 'btnK')

    def __init__(self, driver):
        self.driver = driver

    def searchSomthing(self, words):
        self.driver.find_element(*self.searchField).send_keys(words)

    def clickOnSearch(self):
        self.driver.find_element(*self.search_btn).click()
        after = afterSearch(self.driver)
        return after
