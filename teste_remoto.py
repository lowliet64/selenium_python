from selenium import webdriver
from selenium.webdriver import Remote

browser = Remote(
    command_executor='https://4756-177-37-202-204.ngrok.io',
    desired_capabilities={"browserName":"firefox"}
)

browser.get('https://www.youtube.com')
a = browser.find_element_by_tag_name("input")
a.click()
a.send_keys("flow podcast")
button_searcher = browser.find_element_by_id("search-icon-legacy")
button_searcher.click()
browser.implicitly_wait(10)
# browser.get(browser.current_url)
span = browser.find_element_by_id('title')
print(span.get_attribute('innerHTML'))
video=browser.find_elements_by_css_selector('a#thumbnail')
browser.execute_script("arguments[0][1].click();", video)