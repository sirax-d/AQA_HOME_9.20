from selene import browser, have, be
from selene.core.exceptions import TimeoutException

BASE_URL = 'http://demowebshop.tricentis.com'

def cart_page_asserts():
    browser.element(".product-name").should \
        (have.exact_text("Genuine Leather Handbag with Cell Phone Holder & Many Pockets"))
    browser.element(".product-subtotal").should(have.exact_text("175.00"))
    browser.element(".qty-input").should(have.value("5"))


def clear_cart():
    browser.open(BASE_URL + "/cart")
    try:
        browser.element("[name='removefromcart']").should(be.visible)
        browser.element("[name='removefromcart']").click()
        browser.element("[name='updatecart']").click()
        browser.element(".no-data").should(have.exact_text("Your Shopping Cart is empty!"))
    except TimeoutException:
        print('Cart is empty!')
        pass
