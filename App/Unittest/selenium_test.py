from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from Model.MongoDB.Models.authors import Author
from Model.MongoDB.Models.books import Book

from Model.MySQL.Repository.users_repo import find_all, delete_user
from Viewer.app import app


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
    email = "mail@email.com"
    driver.get('http://127.0.0.1:5000/login/signup')
    username_field = driver.find_element_by_name('username')
    email_field = driver.find_element_by_name('email')
    password_field = driver.find_element_by_name('password')
    confirm_field = driver.find_element_by_name('confirm_password')
    submit = driver.find_element_by_id('submit')
    with app.app_context():
        users = find_all()
    username_field.send_keys(username)
    email_field.send_keys(email)
    password_field.send_keys(password)
    confirm_field.send_keys(password)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)
    with app.app_context():
        user_control = find_all()
        if len(users) == len(user_control):
            print("Unsuccessfully added user")
        else:
            print("Successfully added user")
        print("Removing test user")
        delete_user(username)


def load_author_pages(driver):
    driver.get('http://127.0.0.1:5000/authors')
    authors = Author.all()
    for author in authors:
        author_name = author.name
        print(f'Opening Author page for {author_name}.')
        author_link = driver.find_elements_by_xpath(f"//*[contains(text(), \"{author_name}\")]")[0]
        driver.execute_script("arguments[0].click();", author_link)
        print(f'Testing carousel buttons.')
        carousel_next_button = driver.find_element_by_class_name('carousel-control-next-icon')
        driver.execute_script("arguments[0].click();", carousel_next_button)
        carousel_prev_button = driver.find_element_by_class_name('carousel-control-prev-icon')
        driver.execute_script("arguments[0].click();", carousel_prev_button)
        print(f"Opening page for {driver.find_element_by_id('book-caption').text} by the link in the book carousel.")
        book_caption = driver.find_element_by_id('book-caption')
        driver.execute_script("arguments[0].click();", book_caption)
        print('Returning to index page.')
        driver.back()
        driver.back()
        print('-----'*20)


def load_book_pages(driver):
    driver.get('http://127.0.0.1:5000/books')
    books = Book.all()
    for book in books:
        book_title = book.title
        print(f'Opening Author page for {book_title}.')
        book_link = driver.find_elements_by_xpath(f"//*[contains(text(), \"{book_title}\")]")[0]
        driver.execute_script("arguments[0].click();", book_link)
        print(f'Testing each recommended book.')
        for option in ['left', 'middle', 'right']:
            book_image = driver.find_element_by_id(f'rec-books-{option}')
            driver.execute_script("arguments[0].click();", book_image)
            driver.back()
            if driver.current_url == 'http://127.0.0.1:5000/books':
                driver.forward()
        print('Returning to index page.')
        driver.back()
        print('-----' * 20)


def main():
    driver = webdriver.Chrome('chromedriver.exe')
    time.sleep(2)
    login(driver)
    change_name(driver)
    sign_up(driver)
    load_author_pages(driver)
    load_book_pages(driver)
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    main()
