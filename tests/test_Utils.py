import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_page(test_setup):

    driver.get('https://www.onliner.by/')
    assert driver.title == 'Onliner'

    driver.find_element_by_xpath('//*[@id="userbar"]/div[2]/div/div/div[1]').click()

    e_mail = driver.find_element_by_xpath('//*[@id="auth-container"]/div/div[2]/div/form/div[1]/div/div[2]/div/div/div/div/input')
    e_mail.send_keys('fediaaa.m@gmail.com')

    password = driver.find_element_by_xpath('//*[@id="auth-container"]/div/div[2]/div/form/div[2]/div/div/div/div/input')
    password.send_keys('first_test')

    driver.find_element_by_xpath('//*[@id="auth-container"]/div/div[2]/div/form/div[3]/button').click()

 #   driver.find_element_by_xpath('//*[@id="auth-container"]/div/div[1]/div[2]').click()

    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div/div[4]/header/h2/a').click()
    assert driver.title == 'Каталог Onliner'

    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/ul/li[2]/a').click()
    assert 'Наушники и гарнитуры' in driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div/div[2]/div[2]/div[3]/h1').text
