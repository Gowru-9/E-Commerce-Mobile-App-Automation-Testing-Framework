from appium.webdriver.common.appiumby import AppiumBy
import time 

class PaymentPage:
    def __init__(self,driver):
        self.driver = driver

        self.checkout_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/enterPaymentTitleTV")
        self.payment_method_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
        self.payment_detalis_para = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/paymentDetailsTV")
        self.payment_card_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cardTV")
        self.Visa_card_logo = (AppiumBy.ACCESSIBILITY_ID,"Visa card")
        self.Mastercard_logo = (AppiumBy.ACCESSIBILITY_ID,"Mastercard")
        self.fullName_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/nameTV")
        self.enter_fullName = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/nameET")
        self.card_number_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cardNumberTV")
        self.enter_card_num = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cardNumberET")
        self.card_expiry_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/expirationDateTV")
        self.enter_card_expiry = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/expirationDateET")
        self.card_security_code_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/securityCodeTV")
        self.enter_security_code = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/securityCodeET")
        self.bill_address_checkBox_text = (AppiumBy.ACCESSIBILITY_ID,"Select if User billing address and shipping address are same")
        self.review_order_btn = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/paymentBtn")



    def payment_page_actions(self):
        assert self.driver.find_element(*self.checkout_title).is_displayed()
        assert self.driver.find_element(*self.payment_method_title).is_displayed()
        assert self.driver.find_element(*self.payment_detalis_para ).is_displayed()
        assert self.driver.find_element(*self.payment_card_title).is_displayed()
        assert self.driver.find_element( *self.Visa_card_logo).is_displayed()
        assert self.driver.find_element(*self.Mastercard_logo).is_displayed()
        assert self.driver.find_element(*self.fullName_title).is_displayed()
        self.driver.find_element(*self.enter_fullName).send_keys("suresh")
        assert self.driver.find_element(*self.card_number_title).is_displayed()
        self.driver.find_element(*self.enter_card_num  ).send_keys("12345678901234567890")
        assert self.driver.find_element(*self.card_expiry_title).is_displayed()
        self.driver.find_element(*self.enter_card_expiry).send_keys("10/26")
        assert self.driver.find_element(*self.card_security_code_title).is_displayed()
        self.driver.find_element(*self.enter_security_code ).send_keys("333")
        assert self.driver.find_element(*self.bill_address_checkBox_text).is_displayed()
        self.driver.find_element(*self.review_order_btn).click()
        time.sleep(1)

        
        # print("payment page done ")

