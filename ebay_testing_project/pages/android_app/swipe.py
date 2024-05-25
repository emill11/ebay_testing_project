import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SwipeUp():
    def swipe_up(self):
        screen_size = browser.driver.get_window_size()
        start_x = screen_size['width'] // 2
        start_y = screen_size['height'] * 3 // 4
        end_x = start_x
        end_y = screen_size['height'] // 4
        browser.driver.swipe(start_x, start_y, end_x, end_y, 500)

    def swipe_to_element(self, resource_id, max_swipes=1):
        for _ in range(max_swipes):
            try:
                if browser.element((AppiumBy.ID, resource_id)).is_displayed():
                    return
            except:
                pass

    def swipe_q(self):
        with allure.step('Прокрутка'):
            self.swipe_to_element('com.ebay.mobile:id/cta_button_plus')


swipe_up = SwipeUp()
