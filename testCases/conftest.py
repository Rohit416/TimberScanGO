import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):

    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'C:\Users\Prudhvi\Desktop\TGO Automation stuff\geckodriver.exe')
        print("Launching firefox browser ----")
        driver.implicitly_wait(10)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(r"C:\Users\Prudhvi\Desktop\TGO Automation stuff\chromedriver.exe")
        print("Launching Chrome browser ----")
        driver.implicitly_wait(10)
        driver.maximize_window()

    return driver

############# Setup For desired browser option (Cross Browser) *********


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This wil return Browser value for setup method
    return request.config.getoption("--browser")

############## End of configuring browser selection fixture ***********

########## Pytest HTML Report #############

# it is a hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'TimberScan GO'
    config._metadata['Tester'] = 'Sai Rohith'

#There is a hook for delete/modify Environment info to HTML Report




