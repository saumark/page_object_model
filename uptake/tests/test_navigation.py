import pytest


def test_navigate_from_home_to_industries(get_pom):
    pom_obj = get_pom
    pom_obj.get_industries_page()

    assert pom_obj.page_obj.verify_header("Industries")

    pom_obj.get_home_page()
    pom_obj.page_obj.set_home()

    assert pom_obj.page_obj.verify_header("Uptake Products")


def test_navigate_from_home_to_products(get_pom):
    pom_obj = get_pom
    pom_obj.get_products_page()

    assert pom_obj.page_obj.verify_header("Products")

    pom_obj.get_home_page()
    pom_obj.page_obj.set_home()

    assert pom_obj.page_obj.verify_header("Uptake Products")