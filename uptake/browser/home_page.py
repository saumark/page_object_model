import uptake.elements as E
import uptake.locators as L
from uptake.utils import systems


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.get_home()

    def get_home(self):
        """
        Sets the url of the driver to the uptake url.

        """
        self.driver.get(systems.get("uptake"))

    def set_home(self):
        """
        Locators the logo of the "Home" page and navigates to the "Home" page by clicking the logo, and waiting for the
        "home_is_loaded" element to be visible before returning to guarantee that the "Home" page has loaded.

        """
        logo = E.SeleniumProxy(self.driver, L.PageLocators.UPTAKE_LOGO, timeout=0.25, until_stale=L.PageLocators.HOME_IS_LOADED)
        logo.click()
        E.wait_until_visible(L.PageLocators.HOME_IS_LOADED, self.driver)

    def verify_header(self, header):
        """
        Locates the header element of the page and verifies the text passed in with the heading.

        :param header:
        :return: Boolean
        """
        home_header = E.SeleniumProxy(self.driver, L.PageLocators.PAGE_HEADER, timeout=0.25)
        if home_header.text().lower() == header.lower():
            return True
        else:
            return False
