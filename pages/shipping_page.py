from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ShippingPage:
    def __init__(self,driver):
        self.driver = driver

        
        self.checkout_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
        self.shipping_address_text= (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
        self.full_name_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/fullNameTV")
        self.enter_full_name = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/fullNameET")
        self.address_line1_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address1RL")
        self.enter_address_line1 = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address1ET")
        self.address_line2_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address2TV")
        self.enter_address_line2 = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address2ET")
        self.city_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cityTV")
        self.enter_city_name = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cityET")
        self.state_and_region_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/stateTV")
        self.enter_state_name = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/stateET")
        self.Zip_code_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/zipTV")
        self.enter_zip_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/zipET")
        self.country_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/countryTV")
        self.enter_country_name = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/countryET")
        self.payment_btn = (AppiumBy.ACCESSIBILITY_ID,"Saves user info for checkout")
        

        
    def shipping_page_actions(self):

        wait = WebDriverWait(self.driver, 5)
        assert wait.until(EC.visibility_of_element_located(self.checkout_text)).is_displayed()
        # assert self.driver.find_element(*self.checkout_text).is_displayed()
        assert self.driver.find_element(*self.shipping_address_text).is_displayed()
        assert self.driver.find_element(*self.full_name_text).is_displayed()
        self.driver.find_element(*self.enter_full_name).send_keys("suresh")
        assert self.driver.find_element(*self.address_line1_text).is_displayed()
        self.driver.find_element(*self.enter_address_line1).send_keys("hyd")
        assert self.driver.find_element(*self.address_line2_text).is_displayed()
        self.driver.find_element(*self.enter_address_line2).send_keys("india")
        assert self.driver.find_element(*self.city_text).is_displayed()
        self.driver.find_element(*self.enter_city_name).send_keys("hyd2")
        assert self.driver.find_element(*self.state_and_region_text).is_displayed()
        self.driver.find_element(*self.enter_state_name).send_keys("TG")
        assert self.driver.find_element(*self.Zip_code_text).is_displayed()
        self.driver.find_element(*self.enter_zip_text).send_keys("500082")
        assert self.driver.find_element(*self.country_text).is_displayed()
        self.driver.find_element(*self.enter_country_name).send_keys("india")
        assert self.driver.find_element(*self.payment_btn).is_displayed()
        self.driver.find_element(*self.payment_btn).click()

        time.sleep(1)
        
        
