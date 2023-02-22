from selenium.webdriver.common.by import By


class afterSearch:
    results = (By.CLASS_NAME, 'LC20lb')

    def __init__(self, driver):
        self.driver = driver

    def clickOnFirstResult(self):
        self.driver.find_elements(*self.results)[0].click()

    def getTitleBack(self):
        return self.driver.title