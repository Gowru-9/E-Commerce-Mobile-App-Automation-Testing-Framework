from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Homepage:

    def __init__(self, driver):

        self.driver = driver
        #locators
        self.product_img_1 = (AppiumBy.XPATH,"(//android.widget.ImageView[@content-desc='Product Image'])[1]")
        self.price = (AppiumBy.XPATH,"//android.widget.TextView[@text='$ 29.99']")
        # self.price = ( AppiumBy.XPATH,"//android.widget.TextView[@text='$ 29.99']")
        self.black_color = (AppiumBy.ACCESSIBILITY_ID,"Black color")
        self.blue_color = (AppiumBy.ACCESSIBILITY_ID,"Blue color")
        self.gray_color = (AppiumBy.ACCESSIBILITY_ID,"Gray color")
        self.green_color = (AppiumBy.ACCESSIBILITY_ID,"Green color")
        self.decrease_item = (AppiumBy.ACCESSIBILITY_ID,"Decrease item quantity")
        self.increase_item  = (AppiumBy.ACCESSIBILITY_ID,"Increase item quantity")
        self.addToCart = (AppiumBy.ACCESSIBILITY_ID,"Tap to add product to cart")
        self.review_stars = (AppiumBy.XPATH,"(//android.widget.ImageView)[6]")
        self.review_dialog= (AppiumBy.ACCESSIBILITY_ID,"Closes review dialog")
        self.review_dialog= (AppiumBy.ID,"android:id/content")




    # Actions
    def home_page_actions(self):
        self.driver.find_element(*self.product_img_1).click()
        time.sleep(1)
        self.driver.find_element(*self.price).click()
        self.driver.find_element(*self.black_color).click()
        self.driver.find_element(*self.blue_color).click()
        self.driver.find_element(*self.gray_color).click()
        self.driver.find_element(*self.green_color).click()
        self.driver.find_element(*self.decrease_item).click()
        self.driver.find_element(*self.increase_item).click()
        self.driver.find_element(*self.addToCart).click()
        self.driver.find_element(*self.review_stars).click()
        time.sleep(1)
        self.driver.find_element(*self.review_dialog).click()
       
        # print("home page  done")

