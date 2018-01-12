import uptake.elements as E
import uptake.locators as L


class IndustriesPage:
    def __init__(self, driver):
        self.driver = driver
        self.set_industries()

    def set_industries(self):
        industries = E.SeleniumProxy(self.driver, L.PageLocators.SITE_NAV_ITEM('Industries'), timeout=0.25, until_stale=L.PageLocators.CONTENT)
        industries.click()
        E.wait_until_visible(L.PageLocators.CONTENT, self.driver)

    def verify_header(self, header):
        home_header = E.SeleniumProxy(self.driver, L.PageLocators.PAGE_HEADER, 0.25)
        if home_header.text().lower() == header.lower():
            return True
        else:
            return False