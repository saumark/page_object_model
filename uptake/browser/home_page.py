import uptake.elements as E
import uptake.locators as L
from uptake.utils import systems


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.get_home()

    def get_home(self):
        self.driver.get(systems.get("uptake"))

    def set_home(self):
        logo = E.SeleniumProxy(self.driver, L.PageLocators.UPTAKE_LOGO, timeout=0.25, until_stale=L.PageLocators.HOME_IS_LOADED)
        logo.click()
        E.wait_until_visible(L.PageLocators.HOME_IS_LOADED, self.driver)

    def verify_header(self, header):
        home_header = E.SeleniumProxy(self.driver, L.PageLocators.PAGE_HEADER, timeout=0.25)
        if home_header.text().lower() == header.lower():
            return True
        else:
            return False
