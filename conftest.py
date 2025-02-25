import config
import pytest
import os
import logging

from datetime import datetime


RESULTS_DIR = os.path.join(os.getcwd(), "results")

time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
LOGS_DIR = os.path.join(RESULTS_DIR, time_stamp, "logs")
config.SCREENSHOTS_DIR = os.path.join(RESULTS_DIR, time_stamp, "screenshots")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(config.SCREENSHOTS_DIR, exist_ok=True)

log_file = os.path.join(LOGS_DIR, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Called when test session starts."""
    logging.info("========== Test Session Started ==========")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """Called for each test phase (setup/call/teardown)."""
    if report.when == "call":
        status = "PASSED" if report.passed else "FAILED"
        logging.info(f"Test: {report.nodeid} - {status}")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Called when test session ends."""
    logging.info(f"========== Test Session Ended (Exit Status: {exitstatus}) ==========")


@pytest.fixture(scope="function", autouse=True)
def log_test_start(request):
    """Log test start and end times."""
    test_name = request.node.name
    logging.info(f"Starting test: {test_name}")
    yield
    logging.info(f"Completed test: {test_name}")
