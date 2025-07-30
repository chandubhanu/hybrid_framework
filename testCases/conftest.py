import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver


#######Pytest HTML Report #############

#it is a hook for adding environment info into HTML Report


def pytest_configure(config):
    if config.getoption("dist", "") != "no" and hasattr(config, 'workerinput'):
        return
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nopCommerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester Name'] = 'Bhanu'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)