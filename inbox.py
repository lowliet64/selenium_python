from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from decouple import config
import time

# opts = Options()
# # opts.headless=True
browser = Firefox()

email=config('ROBOT_EMAIL')
password=config('ROBOT_PASS')
browser.get("https://dev-edp.mapia.ai/login")

'''
        ROBÔ PARA PREENCHER UM FORMULARIO
'''

def login(browser,email,password):
    email_input= browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("userpassword")
    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_button=browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()

def open_input_box(browser):
    browser.find_elements_by_xpath('/html/body/div[2]/div[3]/ul/li[2]/a')

def open_workitem(browser):
    table = browser.find_element_by_tag_name('table')
    print(table)


login(browser,email,password)
# switch_to_iframe(browser)


browser.get("https://dev-edp.mapia.ai/nova_esteira")
print(browser.page_source.encode("utf-8"))
# print("showing element=====")
# iframe =browser.find_element_by_xpath('//iframe[@id="internaliFrame"]')
# print(iframe.get_attribute('src'))
# browser.get(iframe.get_attribute('src'))

# time.sleep(4)
# workitems_row=browser.find_elements_by_css_selector("tr")
# print(workitems_row)
# print(workitems_row[1].get_attribute('innerHTML'))

# browser.execute_script("arguments[0].click();", workitems_row[1])
# time.sleep(5)
# dynamic_form = browser.find_element_by_id("dynamic-form")
# yes_field=browser.find_element_by_id("estacao_integrar_folha_concluida_1")
# browser.execute_script("arguments[0].click();",yes_field)

# save_button = browser.find_element_by_css_selector('button.btn-dark')
# save_button.click()
# print(dynamic_form)


