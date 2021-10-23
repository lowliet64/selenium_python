from selenium.webdriver import Firefox

browser = Firefox()
browser.get('http://localhost:5500')
first_link = browser.find_element_by_tag_name('a')
first_link.click()
