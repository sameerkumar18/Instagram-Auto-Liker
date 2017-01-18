from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    id = '__your-instagram-username__'
    passd = '__your-instagram-password__'
    try:
        url = 'https://www.instagram.com'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)

        #driver.set_window_size(1080,720)
        driver.maximize_window()


        assert "Instagram" in driver.title

        elem = driver.find_element_by_class_name('_fcn8k')
        elem.click()

        time.sleep(5)

        username = driver.find_element_by_name('username')
        username.send_keys(id)

        password = driver.find_element_by_name('password')
        password.send_keys(passd)

        password.send_keys(Keys.ENTER)

        time.sleep(2)

        like = driver.find_elements_by_link_text('Like')

        for i in range(0,10):
            #scrolling(driver)
            liker(like,driver)


        # Close the tab/browser when done
        driver.close()
    except:
        print "error"

def liker(like,driver):

        for like_link in like:
            like_link.click()
            time.sleep(6)

        driver.execute_script("document.body.scrollTop = document.body.scrollHeight - document.body.clientHeight;")
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # page_state = driver.execute_script('return document.readyState;')
        time.sleep(5)

def scrolling(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #page_state = driver.execute_script('return document.readyState;')
    time.sleep(4)

#known bug - It starts unliking pictures back again once-> the scrolling taken > time.sleep()
#basically user should close the browser, once this starts happening

main()