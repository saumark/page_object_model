import pytest
from uptake.page_object_model import PageObjectModel


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome")


@pytest.fixture(scope="session")
def get_pom(request):
    browser = request.config.getoption("--browser")
    pom_obj = PageObjectModel(browser)

    return pom_obj


@pytest.fixture(scope="session")
def clean_up(request):
    def __clean_up_session(get_pom):
        pom_obj = get_pom
        pom_obj.driver.quit()

    request.addfinalizer(__clean_up_session(get_pom))
