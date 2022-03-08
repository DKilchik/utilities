

class WebdriverExtension:

    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def open(self):
        self.driver.get(self.url)