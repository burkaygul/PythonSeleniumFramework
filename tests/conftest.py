import pytest
from selenium import webdriver

driver = None


# This function adds a command-line option to choose the browser for testing
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", # Command-line argument name
        action="store",  # Stores the value provided via the command-line
        default="chrome",  # Default browser if no option is provided
        help="browsers: chrome, firefox, ie"  # Help message for the argument
    )


# Fixture for setting up the browser driver
@pytest.fixture(scope= "class")
def setup(request):
    global driver
    # Get the browser name from the command-line argument
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "ie":
        try:
            driver = webdriver.Ie() # Initialize IE driver
        except Exception as e:
            raise ValueError("Internet Explorer WebDriver is not properly installed.") from e
    else:
        raise ValueError("Invalid browser option. Supported options: chrome, firefox, ie.")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Assign the driver to the class-level attribute for use in tests
    request.cls.driver = driver  # Sınıf tabanlı testler için driver bağlama
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


