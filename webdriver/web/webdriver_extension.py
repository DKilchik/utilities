

class WebdriverExtension:

    def __init__(self, driver, implicitly_wait=5):
        self._driver = driver
        self.url = None
        self._driver.implicitly_wait(implicitly_wait)

    def open(self):
        self._driver.get(self.url)