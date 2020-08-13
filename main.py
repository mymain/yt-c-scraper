from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time


def run():
    """
    selenium install > pip install selenium
    chrome driver download > https://sites.google.com/a/chromium.org/chromedriver/downloads
    """
    # YT video url to scrape comments
    url = 'https://www.youtube.com/watch?v=psjtvrQJ20I'

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

        while True:
            try:
                comments_section_end = driver\
                    .find_element_by_css_selector('#continuations .ytd-item-section-renderer:last-child')
                driver.execute_script('arguments[0].scrollIntoView();', comments_section_end)

                # todo remove sleep
                time.sleep(5)

            # when there is no more comments #continuations container is removed
            # and we are getting NoSuchElementException so we know that
            # we are at the end of comments list so we can break the while loop
            except NoSuchElementException:
                print('Comments end')
                break

        print('Ok we are ready - all comments are loaded')

        # get all comments contents these are arrays
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
        # test document state
        # https://developer.mozilla.org/en-US/docs/Web/API/Document/readyState
        if driver.execute_script('return document.readyState') == 'complete':
            return True
        else:
            yield False


if __name__ == '__main__':
    run()
