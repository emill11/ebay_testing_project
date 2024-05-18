from selene import command, have, browser


class HomePage:

    def open_home_page(self):
        browser.open('/')


home_page = HomePage()
