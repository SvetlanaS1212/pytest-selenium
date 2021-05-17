import time
# See https://selenium-python.readthedocs.io/getting-started.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setup_function(function):
    function.startTime = time.time()

    # Open browser
    function.driver = webdriver.Firefox()
    # See https://selenium-python.readthedocs.io/waits.html#implicit-waits
    function.driver.implicitly_wait(30)

def teardown_function(function):
    # Close browser
    function.driver.quit()
    del function.driver

    duration = time.time() - function.startTime
    print("%s: %.3f" % (function.__name__, duration))
    del function.startTime

def test_search():
    self = test_search

    # Open url
    self.driver.get("https://duckduckgo.com/")

    # Search "selenium"
    elem = self.driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)

    # Wait is implicit (see setup_function)

    # Take 1st result url
    elem = self.driver.find_element_by_css_selector('.results--main #links #r1-0.result .links_main a.result__url')
    href = elem.get_attribute("href")

    # Check the result
    assert href == "https://www.selenium.dev/"

    pass

if __name__ == "__main__":
    import pytest
    pytest.main()