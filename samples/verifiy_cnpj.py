from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

browser = Firefox()

browser.get("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp")

search_field = browser.find_element_by_xpath('//*[@id="cnpj"]')
search_field.send_keys("42163015000110")

time.sleep(5)

iframe = browser.find_element_by_tag_name('iframe')
print(iframe.get_attribute('src'))
print(iframe.get_attribute('innerHTML'))
# WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe")))
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']"))).click()

search_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/form/div[3]/div/button[1]")
search_button.click()