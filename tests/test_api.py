import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import browser

from pages.cart_page import cart_page_asserts, clear_cart
from pages.login_page import check_login
from utils.base_request import post_request
from utils.cookies_add import get_cookie, get_cookie_nop_customer

load_dotenv()
base_url = os.getenv("BASE_URL")


def test_login():
    cookie = get_cookie()
    with step(f"Open {base_url} and login"):
        browser.open(base_url)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with step("Check successful login"):
        check_login()


def test_add_items_in_cart():
    cookie_customer = get_cookie_nop_customer()
    with step("Clear shopping cart"): \
            clear_cart()
    with step("Add cookie in browser"):
        browser.open(base_url + "/cart")
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_customer})
        browser.element("[id='topcartlink']").click()
    with step("Check items in cart and status code"):
        cart_page_asserts()


def test_add_items_in_cart_with_login():
    cookie = get_cookie()
    with step("Login with cookie"):
        browser.open(base_url)
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
    with step("Clear shopping cart"):
        clear_cart()
    with step("Add item to cart"):
        browser.open(base_url + "/genuine-leather-handbag-with-cell-phone-holder-many-pockets")
        post_request(
            url="/addproducttocart/details/29/1",
            data={"addtocart_29.EnteredQuantity": 5}, \
            cookies={"NOPCOMMERCE.AUTH": cookie})
        browser.open(base_url + "/cart")
    with step("Check items in cart"):
        cart_page_asserts()
