import os
import importlib
import web_drivers
import uptake.utils as utils

from selenium import webdriver


class PageObjectModel(object):
    """
    This is the page object model class that serves up the pages in the framework.

    """

    def __init__(self, device):
        self.device = device or "firefox"
        drivers_path = os.path.dirname(web_drivers.__file__)
        if self.device.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path=drivers_path + "\\chromedriver.exe")
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Firefox(executable_path=drivers_path+ "\\geckodriver.exe")
            self.driver.maximize_window()
        self.page_obj = None
        self.get_home_page()

    def get_home_page(self):
        """
        Creates an object of the HomePage class and sets it to the page_obj property.
        """
        home_page_module = importlib.import_module(utils.get_device_module(self.device) + ".home_page")
        home_page_obj = home_page_module.HomePage(self.driver)
        self.page_obj = home_page_obj

    def get_industries_page(self):
        """
        Creates an object of the IndustriesPage class and sets it to the page_obj property.
        """
        industries_page_module = importlib.import_module(utils.get_device_module(self.device) + ".industries_page")
        industries_page_obj = industries_page_module.IndustriesPage(self.driver)
        self.page_obj = industries_page_obj

    def get_products_page(self):
        """
        Creates an object of the ProductsPage class and sets it to the page_obj property.
        """
        products_page_module = importlib.import_module(utils.get_device_module(self.device) + ".products_page")
        products_page_obj = products_page_module.ProductsPage(self.driver)
        self.page_obj = products_page_obj
