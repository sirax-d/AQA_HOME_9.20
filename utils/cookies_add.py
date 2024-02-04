import os

import requests
from dotenv import load_dotenv

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
base_url = os.getenv("BASE_URL")


def get_cookie():
    response = requests.post(base_url + "/login", json={"Email": login, "Password": password}, allow_redirects=False)
    assert response.status_code == 302
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return cookie


def get_cookie_nop_customer():
    response_add = requests.post(
        base_url + "/addproducttocart/details/29/1",
        data={"addtocart_29.EnteredQuantity": 5}, cookies={"Nop.customer": get_cookie()})
    assert response_add.status_code == 200
    cookie_customer = response_add.cookies.get("Nop.customer")
    return cookie_customer
