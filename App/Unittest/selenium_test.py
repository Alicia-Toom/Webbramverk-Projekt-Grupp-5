from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from Model.MySQL.Models.users import User
from Model.MySQL.Repository.users_repo import find_all


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


def sign_up(driver):
    password = "thisissecret"
    username = "selenium"
    email = "email@email.com"
    driver.get('http://127.0.0.1:5000/login/signup')
    username_field = driver.find_element_by_name('username')
    email_field = driver.find_element_by_name('email')
    password_field = driver.find_element_by_name('password')
    confirm_field = driver.find_element_by_name('confirm_password')
    submit = driver.find_element_by_id('submit')
    users = find_all()
    username_field.send_keys(username)
    email_field.send_keys(email)
    password_field.send_keys(password)
    confirm_field.send_keys(password)
    #submit.send_keys(Keys.RETURN)



def main():
    driver = webdriver.Chrome('chromedriver.exe')
    #login(driver)
    #change_name(driver)
    sign_up(driver)
    time.sleep(5)
    driver.close()



if __name__ == '__main__':
    main()
