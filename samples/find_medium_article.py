from selenium.webdriver import Firefox

browser = Firefox()
browser.get('https://google.com')
box_search = browser.find_element_by_tag_name("input")
box_search.send_keys("Medium Python")
button_searcher = browser.find_elements_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button_searcher.click()
first_link = browser.find_element_by_tag_name('a')
first_link.click()
