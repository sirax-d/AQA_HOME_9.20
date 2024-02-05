from selene import browser, have, be

BASE_URL = 'http://demowebshop.tricentis.com'

def cart_page_asserts():
    browser.element(".product-name").should \
        (have.exact_text("Genuine Leather Handbag with Cell Phone Holder & Many Pockets"))
    browser.element(".product-subtotal").should(have.exact_text("175.00"))
    browser.element(".qty-input").should(have.value("5"))


def clear_cart():
    browser.open("/cart")
    if browser.element("[name='removefromcart']").matching(be.visible):
        browser.element("[name='removefromcart']").click()
        browser.element("[name='updatecart']").click()
        browser.element(".order-summary-content").should(have.exact_text("Your Shopping Cart is empty!"))