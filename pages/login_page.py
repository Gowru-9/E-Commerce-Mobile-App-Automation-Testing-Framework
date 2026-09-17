
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        self.login_text = (AppiumBy.XPATH,"//android.widget.TextView[@text='Login']")
        self.para = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/selectTextTV")
        self.Username_text = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/usernameTV")
        self.enter_Username = (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/nameET")
        self.password_text= (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordTV")
        self.enter_password= (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordET")
        self.Login_btn = (AppiumBy.ACCESSIBILITY_ID,"Tap to login with given credentials")

        

    def login_page_actions(self):
        assert self.driver.find_element(*self.login_text).is_displayed()
        assert self.driver.find_element(*self.para).is_displayed()
        assert self.driver.find_element(*self.Username_text).is_displayed()
        self.driver.find_element(*self.enter_Username).send_keys("bod@example.com")
        assert self.driver.find_element(*self.password_text).is_displayed()
        self.driver.find_element(*self.enter_password).send_keys("10203040")
        self.driver.find_element(*self.Login_btn).click()
