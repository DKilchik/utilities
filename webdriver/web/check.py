from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Check:

    """ 
        it is an extension of selenium  
        to check different conditions 
    """
    def __init__(self, driver):
        self.driver = driver

    def element_is_present(self, locator: tuple) -> bool:
        """return True if element is present or False if otherwise

        Args:
            locator: to find element
        
        Usage:
            assert check.element_is_present(locator=('id', SomeId))
        """
        try:
            by, selector = locator 
            self.driver.find_element(by, selector)
            return True
        except NoSuchElementException:
            return False

    def element_will_appear(self, locator: tuple, timeout=4, poll_frequency=0.25) -> bool:
        """return True if element will appear during timeout value period or False if otherwise

        Args:
            locator: to find element
            timeout: to stop element search, sec Default: 4
            poll_frequency: sleep interval between calls, sec Default: 0.25
        
        Usage:
            assert check.element_is_present(locator=('id', SomeId))
        """
        try:
            WebDriverWait(
                self.driver, timeout=timeout, poll_frequency=poll_frequency
                ).until(EC.presence_of_element_located(locator=locator))
            return True
        except TimeoutException:
            return False

    def element_is_clickable(self, locator: tuple) -> bool:
        """return True if element is clickable or False if otherwise \n
    
        Args:
            locator: to find element
        
        Note:
            it is based on WebDriverWait but timeout is setted too low, so 
            method will not wait for loading or DOM changing

        Usage:
            assert check.element_is_clickable(locator=('id', SomeId))
        """
        try:
            WebDriverWait(
                self.driver, timeout=0.15, poll_frequency=0.05
                ).until(EC.element_to_be_clickable(locator=locator))
            return True
        except TimeoutException:
            return False
