import retrying
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


def find_element(locator, driver, time_out=30, log_exception=True, poll=0.5, until="visible"):
    """

    :param locator: Element locator to look for.
    :param driver: Driver on which the element is validated.
    :param time_out: Timeout value user can set or defaults to 30.
    :param log_exception: Flag to throw raise exception or return None.
    :param poll: Poll frequency to poll for element.
    :param until: Until visible or present.
    :return: WebElement
    """

    try:
        poll_frequency = poll or 0.05
        if time_out < poll_frequency:
            poll_frequency = time_out

        if until == "present":
            WebDriverWait(driver, time_out, poll_frequency).until(EC.presence_of_element_located(locator))
        else:
            WebDriverWait(driver, time_out, poll_frequency).until(EC.visibility_of_element_located(locator))

        return driver.find_element(*locator)

    except TimeoutException:
        if log_exception:
            raise

        return None


def wait_until_visible(locator, driver, time_out=30):
    """
    This method is to check the visibility of an element on the page.

    :param locator: Element locator to look for.
    :param driver: Driver on which the element is validated.
    :param time_out: Timeout value user can set or defaults to 30.
    """

    try:
        WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException("Timed out waiting for the element to be visible: {}".format(locator))


class SeleniumProxy:
    """
    This is a wrapper class to handle WebElement actions using the selenium web driver.
    """

    def __init__(self, driver, locator, timeout=None, poll=None, ignore_exceptions=False, until_stale=None, stale_timeout=5, until="visible"):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.poll = poll
        self.ignore_exception = ignore_exceptions
        self.until_stale = until_stale
        self.stale_timeout = stale_timeout
        self.until = until
        self.e = self.__locate()

    def __locate(self):
        return find_element(self.locator, self.driver, time_out=self.timeout, poll=self.poll,
                            log_exception=not self.ignore_exception, until=self.until)

    def __wait_until_stale(self, e):
        """
        This method checks for stale element exception thrown when any action is performed on any element.

        :param e:
        :return:
        """
        @retrying.retry(stop_max_delay=self.stale_timeout*1000, wait_fixed=250)
        def __until_stale():
            try:
                e.find_elements_by_id('place-holder')
            except StaleElementReferenceException:
                return True
            raise Exception("Timedout waiting for element {} to be stale!".format(self.until_stale))

        __until_stale()

    def text(self):
        """

        This methods returns the text or inner html of an element.

        :return: String
        """
        if self.until == "visible":
            return self.e.text
        else:
            return self.e.get_attribute("innerText").replace("\n", " ").strip()

    def get(self, attr):
        """

        This element gets the value of the attribute specified.

        :param attr:
        :return: String
        """
        return self.e.get_attribute(attr)

    def click(self):
        """

        This is smart click method to wrap event handling around an element click.

        """
        if self.until_stale is not None:
            e = find_element(self.until_stale, self.driver, time_out=self.timeout, poll=self.poll, until=self.until)

        self.e.click()

        if self.until_stale is not None:
            self.__wait_until_stale(e)

