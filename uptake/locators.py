from selenium.webdriver.common.by import By


class PageLocators(object):
    # home page locators
    UPTAKE_LOGO = (By.CSS_SELECTOR, "div.l-site-header__brand")
    HOME_IS_LOADED = (By.CSS_SELECTOR, "div.l-site__content div.l-hero-header div.l-hero-header__image.is-loaded")
    PAGE_HEADER = (By.CSS_SELECTOR, "div.l-hero-header div.l-hero-header__content div.hero-heading h1.hero-heading__subheading")
    SITE_NAV_ITEM = staticmethod(lambda x: (By.XPATH, "//ul[@class='site-nav']/li[contains(concat(' ', @class, ' '), ' site-nav__item ')]/a[contains(concat(' ', @class, ' '), ' site-nav__desktop-link ')]/span[text()='{}']".format(x)))

    # Child page locators
    CONTENT = (By.CSS_SELECTOR, "div.l-hero-header div.l-hero-header__content div.hero-heading")

