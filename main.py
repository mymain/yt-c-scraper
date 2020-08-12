from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


def run():
    """
    selenium install > pip install selenium
    chrome driver download > https://sites.google.com/a/chromium.org/chromedriver/downloads
    """
    # YT video url to scrape comments
    url = 'https://www.youtube.com/watch?v=sMIMn9_nFpo'

    print('Pulling comments list from: ' + url)

    # fill path to the chrome web driver on your local PC
    driver = webdriver.Chrome(r'C:\Users\Maciek\Downloads\chromedriver_win32\chromedriver.exe')

    driver.get(url)
    driver.maximize_window()

    while True:
        while not page_is_loaded(driver):
            continue

        driver.execute_script('alert("Page is ready")')
        # prevent alert exception
        Alert(driver).accept()
        # ok we are ready for scrolling

        # find comments section
        comments_section = driver.find_element_by_id('comments')
        # scroll to it
        driver.execute_script('arguments[0].scrollIntoView();', comments_section)

        # TODO change for loader ready state
        time.sleep(10)  # not nice but working

        # get comments contents these are arrays
        users = driver.find_elements_by_id('author-text')
        comments = driver.find_elements_by_id('content-text')

        for user, comment in zip(users, comments):
            print(user.text + ':')
            print(comment.text + '\n')

        time.sleep(60)  # one min break before exit
        # close browser window once we are done
        driver.close()

        print('Ok all done')

        exit(0)


def page_is_loaded(driver):
    while True:
        # https://developer.mozilla.org/en-US/docs/Web/API/Document/readyState
        state = driver.execute_script('return document.readyState')
        if state == 'complete':
            return True
        else:
            yield False


if __name__ == '__main__':
    run()
