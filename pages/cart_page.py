from appium.webdriver.common.appiumby  import AppiumBy
import time

class CartPage:
    def __init__(self,driver):
        self.driver = driver

        self.open_cart_page = (AppiumBy.ACCESSIBILITY_ID,"View cart")
        # self.open_cart_page = (AppiumBy.ACCESSIBILITY_ID,"Displays number of items in your cart")
        self.cart_name = (AppiumBy.XPATH,"//android.widget.TextView[@text='My Cart']")
        self.item_name = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/titleTV")
        self.item_price = (AppiumBy.XPATH,"(//android.widget.TextView[@text='$ 29.99'])[1]")
        self.item_dicrease = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/minusIV")
        self.item_increase = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/plusIV")
        self.item_remove= (AppiumBy.ACCESSIBILITY_ID,"Removes product from cart")
        self.go_shopping_btn = (AppiumBy.CLASS_NAME,"android.widget.Button")
        self.item_confirms = (AppiumBy.ACCESSIBILITY_ID,"Confirms products for checkout")
        # self.item_increase = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/plusIV")


    def cart_page_actions(self):
        self.driver.find_element(*self.open_cart_page).click()
        print("cart page starting...")
        time.sleep(1)
        assert self.driver.find_element(*self.cart_name).is_displayed()
        assert self.driver.find_element(*self.item_name).is_displayed()
        assert self.driver.find_element(*self.item_price).is_displayed()
        self.driver.find_element(*self.item_increase).click()
        # time.sleep(4)
        self.driver.find_element(*self.item_dicrease).click()
        # time.sleep(5)
    
        # self.driver.find_element(*self.item_remove).click()
        # print("item removed")
        # self.driver.find_element(*self,self.go_shopping_btn).click()
        # self.driver.home_page.product_page_actions()
        self.driver.find_element(*self.item_confirms).click()
    
        # print("cart page done ")
        time.sleep(1)


