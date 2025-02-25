import config
import pytest
import requests


from appium import webdriver
from appium.options.ios import XCUITestOptions


@pytest.fixture(scope="module")
def ios_driver():
    caps = {
        "platformName": config.PLATFORM_NAME,
        "deviceName": config.DEVICE_NAME,
        "udid": config.DEVICE_UDID,
        "platformVersion": config.PLATFORM_VERSION,
        "automationName": "XCUITest",
        "bundleId": "com.apple.Preferences",
        "showXcodeLog": True,
        "bundleId": "locspc"
    }

    options = XCUITestOptions()
    options.load_capabilities(caps)

    driver = webdriver.Remote(command_executor=config.APPIUM_SERVER_URL, options=options)
    
    yield driver
    
    driver.quit()

    
def test_open_my_observatory(ios_driver):
    """ Test opening MyObservatory app """
    ios_driver.find_element("xpath", "//XCUIElementTypeButton[@label='目錄, 左邊彈出選單']").click()

    ios_driver.implicitly_wait(5)
    forecast_button = ios_driver.find_element("xpath", "//XCUIElementTypeOther[@name='預報及警告服務']//XCUIElementTypeButton[@label='按下打開此部分']")
    forecast_button.click()
    
    ios_driver.implicitly_wait(5)
    nine_day_forecast = ios_driver.find_element("accessibility id", "九天預報")
    nine_day_forecast.click()
    
    ios_driver.implicitly_wait(5)
    ios_driver.save_screenshot(f"{config.SCREENSHOTS_DIR}/after_click.png")
    
    assert "九天預報" in ios_driver.page_source, "Page source does not contain expected text '九天預報'"
