from appium.webdriver.common.appiumby import AppiumBy
import time 

class ReviewOrder:
    def __init__(self,driver):
        self.driver = driver

        self.review_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
        self.item_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/titleTV")
        self.price_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/priceTV")
        self.rating_satr_1 = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/start1IV")
        self.color_title = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/colorTitleTV")
        self.display_color = (AppiumBy.ACCESSIBILITY_ID,"Displays color of selected product")
        self.product_img = (AppiumBy.ACCESSIBILITY_ID,"Displays selected product")
        self.deliver_address_title= (AppiumBy.XPATH,"//android.widget.TextView[@text='Deliver Address']")
        self.fullName = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/fullNameTV")
        self.address = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/addressTV")
        self.city = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cityTV")
        self.country = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/countryTV")
        self.Payment_method = (AppiumBy.XPATH,"//android.widget.TextView[@text='Payment Method']")
        self.total_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/totalTextTV")
        self.item_num = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/itemNumberTV")
        self.total_amount = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/totalAmountTV")
        self.Place_order_btn = (AppiumBy.ACCESSIBILITY_ID,"Completes the process of checkout")
        # self.review_text = (AppiumBy.ID,"")


    def review_page_actions(self):
        self.driver.find_element(*self.review_text).is_displayed()
        self.driver.find_element(*self.item_title).is_displayed()
        self.driver.find_element(*self.price_title).is_displayed()
        self.driver.find_element(*self.rating_satr_1).is_displayed()
        self.driver.find_element(*self.color_title).is_displayed()
        self.driver.find_element(*self.display_color).is_displayed()
        self.driver.find_element(*self.product_img).is_displayed()
        self.driver.find_element(*self.deliver_address_title).is_displayed()
        self.driver.find_element(*self.fullName).is_displayed()
        self.driver.find_element(*self.address).is_displayed()
        self.driver.find_element(*self.city).is_displayed()
        self.driver.find_element(*self.country).is_displayed()
        self.driver.find_element(*self.Payment_method).is_displayed()
        self.driver.find_element(*self.total_text).is_displayed()
        self.driver.find_element(*self.item_num).is_displayed()
        self.driver.find_element(*self.total_amount).is_displayed()
        self.driver.find_element(*self.Place_order_btn).click()
        time.sleep(1)
        # print("Review page done ")


                



