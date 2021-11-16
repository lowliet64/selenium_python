from selenium.webdriver import Firefox


browser = Firefox()
browser.get('http://127.0.0.1:5500/screens/index.html')

chooseFile = browser.find_element_by_id("upload-file")
chooseFile.send_keys(r"C:\\Users\\20182014040035\\develop\\Python\\selenium_teste\\samples\\geckodriver.log")