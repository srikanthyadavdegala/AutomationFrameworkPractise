import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        service_obj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj)
    else:
        service_obj = Service(IEDriverManager().install())
        driver = webdriver.Ie(service=service_obj)

    return driver


def pytest_addoption(parser):  # This will get value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture
def browser(request):  # This will return browser value to setup method
    return request.config.getoption("--browser")


"""    Pytest HTML Report     """


# It is hook for adding environment info to HTML Report

def pytest_configure(config):
    config._metadata["Project Name"] = "NOP Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Srikanth Yadav"


# It is hook for delete/modify environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
