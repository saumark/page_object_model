
def test_navigate_from_home_to_industries(get_pom):
    # 1. Creating an object of the Page object model class
    pom_obj = get_pom
    # 2. Getting the page object of teh industries page
    pom_obj.get_industries_page()

    # 3. Verifying the header of the Industries page
    assert pom_obj.page_obj.verify_header("Industries")

    # 4. Navigating back to the home page
    pom_obj.get_home_page()

    # 5. Verifying the heading of the home page
    assert pom_obj.page_obj.verify_header("Uptake Products")


def test_navigate_from_home_to_products(get_pom):
    # 1. Creating an object of the Page object model class
    pom_obj = get_pom
    # 2. Getting the page object of the products page
    pom_obj.get_products_page()

    # 3. Verifying the header of the Products page
    assert pom_obj.page_obj.verify_header("Products")

    # 4. Navigating back to the home page
    pom_obj.get_home_page()
    pom_obj.page_obj.set_home()

    # 5. Verifying the heading of the home page
    assert pom_obj.page_obj.verify_header("Uptake Products")


def test_clean_up(get_pom):
    get_pom.driver.quit()
