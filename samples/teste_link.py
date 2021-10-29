from selenium.webdriver import Firefox

browser = Firefox()
browser.get('http://localhost:5500/screens/index.html')

browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
first_link = browser.find_element_by_tag_name('button')
first_link.click()
