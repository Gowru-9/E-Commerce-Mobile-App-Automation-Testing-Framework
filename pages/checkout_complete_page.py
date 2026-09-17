from appium.webdriver.common.appiumby import AppiumBy

class CheckoutComplete:
    def __init__(self,driver):
        self.driver = driver

        self.checkout_complete_title = (AppiumBy.XPATH,"//android.widget.TextView[@text='Checkout Complete']")
        self.thank_you_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/thankYouTV")
        self.swag_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/swagTV")
        self.about_order_para = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/orderTV")
        self.continue_shopping_btn = (AppiumBy.ACCESSIBILITY_ID,"Tap to open catalog")

    def checkout_complete_actions(self):
        self.driver.find_element(*self.checkout_complete_title).is_displayed()
        self.driver.find_element(*self.thank_you_title).is_displayed()
        self.driver.find_element(*self.swag_title).is_displayed()
        self.driver.find_element(*self.about_order_para).is_displayed()
        self.driver.find_element(*self.continue_shopping_btn).click()

        # print("ckeckout complete page done ")