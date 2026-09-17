from pages.home_page import Homepage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.shipping_page import ShippingPage
from pages.payment_page import PaymentPage
from pages.review_order_page import ReviewOrder
from pages.checkout_complete_page import CheckoutComplete



def test_login(driver):

    home_page = Homepage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    shipping_page = ShippingPage(driver)
    payment_page = PaymentPage(driver)
    review_order_page = ReviewOrder (driver)
    checkout_complete_page = CheckoutComplete(driver)



    # methods calling 
    home_page.home_page_actions()
    cart_page.cart_page_actions()
    login_page.login_page_actions()
    shipping_page.shipping_page_actions()
    payment_page.payment_page_actions()
    review_order_page.review_page_actions()
    checkout_complete_page.checkout_complete_actions()


    


 