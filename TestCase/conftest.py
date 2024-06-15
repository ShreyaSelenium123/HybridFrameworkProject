from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox")
    else:
        driver = webdriver.Ie()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#####PYTEST HTML REPORTS######
def pytest_configure(config):
    def pytest_configure(config):
        config._metadata['Project name'] = "HybridFrameProject"
        config._metadata['Module name'] = 'Customers'
        config._metadata['Tester'] = 'Shreya baraskar'

    #### It is a hook for deleting/modifying environment info in HTML reports ###
    @pytest.mark.optionalhook
    def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)



