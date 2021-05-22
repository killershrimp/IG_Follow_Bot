from time import sleep
from selenium import webdriver, common


def alr_req(status):
    return status == 'Following' or status == 'Message' or status == 'Requested' or status == 'Unfollow'


def should_follow(status):
    return status == 'Follow'


browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/accounts/login/')

try:
    # login
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    with open("login_info.txt") as login_info:
        username_input.send_keys(login_info.readline())
        password_input.send_keys(login_info.readline())

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
    sleep(5)

    # follow users
    unsuccessful = []
    with open("want_to_follow.txt") as follow_list:
        for username in follow_list:
            username = username.rstrip()
            if username != "":
                browser.get('https://www.instagram.com/' + username + '/')
                sleep(1)
                try:
                    follow_button = browser.find_elements_by_css_selector('button')
                    for i in range(2):
                        status = follow_button[i].text.rstrip()
                        if should_follow(status):
                            follow_button[i].click()
                            break
                except common.exceptions.NoSuchElementException:
                    # if user not found
                    unsuccessful.append(username)
                except IndexError:
                    unsuccessful.append(username)

    print("These users couldn't be found: " + str(unsuccessful))
    browser.close()
except common.exceptions.ElementClickInterceptedException:
    print("Add your username and password to login_info.txt and run again!")
