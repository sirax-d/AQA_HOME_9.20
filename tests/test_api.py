import time

from allure_commons._allure import step
from selene import browser

from pages.cart_page import cart_page_asserts, clear_cart
from pages.login_page import check_login
from utils.base_request import post_request
from utils.cookies_add import get_cookie, get_cookie_nop_customer

BASE_URL = 'http://demowebshop.tricentis.com'


def test_login():
    cookie = get_cookie()
    with step(f"Open {BASE_URL} and login"):
        browser.open(BASE_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with step("Check successful login"):
        check_login()


def test_add_items_in_cart():
    cookie_customer = get_cookie_nop_customer()
    with step("Clear shopping cart"): \
        clear_cart()
    with step("Add cookie in browser"):
        browser.open(BASE_URL + "/cart")
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_customer})
        browser.element("[id='topcartlink']").click()
        time.sleep(5)
    with step("Check items in cart and status code"):
        cart_page_asserts()


def test_add_items_in_cart_with_login():
    cookie = get_cookie()
    with step("Login with cookie"):
        browser.open(BASE_URL)
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
    with step("Clear shopping cart"):
        clear_cart()
    with step("Add item to cart"):
        browser.open(BASE_URL + "/genuine-leather-handbag-with-cell-phone-holder-many-pockets")
        post_request(
            url="/addproducttocart/details/29/1",
            data={"addtocart_29.EnteredQuantity": 5}, \
            cookies={"NOPCOMMERCE.AUTH": cookie})
        browser.open(BASE_URL + "/cart")
    with step("Check items in cart"):
        cart_page_asserts()
