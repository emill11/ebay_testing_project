from selene import browser


def swipe_up(swipe_count):
    for _ in range(swipe_count):
        screen_size = browser.driver.get_window_size()
        start_x = screen_size['width'] // 2
        start_y = screen_size['height'] * 3 // 4
        end_x = start_x
        end_y = screen_size['height'] // 4
        browser.driver.swipe(start_x, start_y, end_x, end_y, 500)


def swipe_down(swipe_count):
    for _ in range(swipe_count):
        screen_size = browser.driver.get_window_size()
        start_x = screen_size['width'] // 2
        start_y = screen_size['height'] // 4
        end_x = start_x
        end_y = screen_size['height'] * 3 // 4
        browser.driver.swipe(start_x, start_y, end_x, end_y, 500)
