from .check import Check


class WebdriverExtension:

    def __init__(self, driver, implicitly_wait=5):
        self.url = None
        self._driver = driver
        self._driver.implicitly_wait(implicitly_wait)
        self.check = Check(self._driver)

    def open(self):
        self._driver.get(self.url)
