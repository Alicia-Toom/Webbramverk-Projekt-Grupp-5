from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login(driver):
    driver.get('http://127.0.0.1:5000/login')
    username_field = driver.find_element_by_name('username')
    password_field = driver.find_element_by_name('password')
    submit = driver.find_element_by_name('submit')

    username_field.send_keys('test')
    password_field.send_keys('test')
    submit.send_keys(Keys.RETURN)


def change_name(driver):
    driver.get('http://127.0.0.1:5000/profile')
    first_name_field = driver.find_element_by_name('first_name')
    first_name_field.clear()
    first_name_field.send_keys('Selenium name change')
    submit = driver.find_element_by_id('submit-button')
    submit.send_keys(Keys.RETURN)


def main():
    driver = webdriver.Chrome('chromedriver.exe')
    login(driver)
    change_name(driver)
    time.sleep(5)
    driver.close()



if __name__ == '__main__':
    main()
