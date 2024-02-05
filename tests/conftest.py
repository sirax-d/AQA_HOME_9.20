import os

import pytest
from dotenv import load_dotenv
from selene import browser

load_dotenv()
base_url = os.getenv("BASE_URL")


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = base_url
    browser.config.window_width = '1900'
    browser.config.window_height = '1080'

    yield browser
    browser.quit()
