class OpenPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_page(self):
        """Заходит на вкладку для авторизации"""
        self.driver.find_element_by_xpath(
            '//*[@id="userbar"]/div[2]/div/div/div[1]'
                                          ).click()

    def set_username(self, username):
        """Вводит логин"""
        e_mail = self.driver.find_element_by_xpath(
            '//*[@id="auth-container"]/div/div[2]/div/form/div[1]'
            '/div/div[2]/div/div/div/div/input')
        e_mail.send_keys(username)

    def set_password(self, password):
        """Вводит пароль"""
        path_to_password = self.driver.find_element_by_xpath(
            '//*[@id="auth-container"]/div/div[2]/div/form/div[2]'
            '/div/div/div/div/input')
        path_to_password.send_keys(password)

    def click_login(self):
        """Кликает на кнопку авторизоваться"""
        self.driver.find_element_by_xpath(
            '//*[@id="auth-container"]/div/div[2]/div/form/div[3]/button'
        ).click()

    def skip_advertisement(self):
        """Отказывается от прохождения Captcha,
         с кототким XPath не работает почему-то"""
        self.driver.find_element_by_xpath(
            '/html/body/div[7]/div/div/div/div/div/div/div/div[1]/div[2]'
                                          ).click()

    def click_catalog(self):
        """Открывает каталог"""
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div/div/div[4]/header/h2/a')\
            .click()

    def click_headphone(self):
        """Открывает раздел с наушниками"""
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div/div/div[2]/'
            'div[1]/div/ul/li[2]/a').click()

    def teardown(self):
        """Закрытие браузера"""
        self.driver.close()
        self.driver.quit()
