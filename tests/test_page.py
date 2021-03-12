from selenium import webdriver
from Utils import OpenPage
import time


class TestPage01:

    baseURL = 'https://www.onliner.by'
    username = 'fediaaa.m@gmail.com'
    password = 'first_test'
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    op = OpenPage(driver)

    def test_open_page(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        act_title = self.driver.title

        if act_title == 'Onliner':
            assert True
        else:
            self.driver.save_screenshot(
                'Screenshots/test_open_page %s.png' % time.time())
            self.op.teardown()
            assert False, 'Открыта  неверная страница'

    def test_open_login_page(self):
        self.op.click_login_page()
        self.op.set_username(self.username)

    def test_set_password(self):

        self.op.set_password(self.password)
        self.op.click_login()

    def test_skip_password(self):
        self.driver.set_page_load_timeout(10)
        self.op.skip_advertisement()

    def test_open_catalog(self):
        self.op.click_catalog()
        self.op.click_headphone()

    def test_check(self):
        assert 'Наушники и гарнитуры' in self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div/div/div[2]/div[2]/div[3]/h1')\
            .text
        self.op.teardown()
