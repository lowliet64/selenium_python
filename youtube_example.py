from selenium.webdriver import Firefox
import time
browser = Firefox()
browser.get('https://www.youtube.com')

a = browser.find_element_by_tag_name("input")
a.click()
a.send_keys("flow podcast")

button_searcher = browser.find_element_by_id("search-icon-legacy")
button_searcher.click()

video= browser.find_elements_by_css_selector('a#thumbnail')
browser.execute_script("arguments[0][0].click();", video)





# browser.quit()