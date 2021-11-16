from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList","")
profile.set_preference("browser.download.manager.showWhenStarting","")
profile.set_preference("browser.download.dir","")
#Example:profile.set_preference("browser.download.dir", "C:\Tutorial\down")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","")
browser = Firefox()

browser.get("https://www.whatsapp.com/download")
browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/a')[0].click()

