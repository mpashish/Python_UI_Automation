from email.policy import default
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from utility.read_config_file import ReadConfig
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "ie":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(ReadConfig.get_app_url())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

@pytest.fixture(params=[{"Name": "Ashish", "Surname": "Mhaiskar"}, {"Name": "Raju", "Surname": "Shetty"}])
def get_data_as_fixture_parameter(request):
    print(f"Fixture parameter: {request.param}")  # Debug print
    return request.param