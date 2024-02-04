from selene import browser, have, be
import requests
import os
from dotenv import load_dotenv


load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
base_url = os.getenv("BASE_URL")


def check_login():
    browser.open(base_url)
    browser.element(".account").should(have.exact_text(login))
    browser.open(base_url)