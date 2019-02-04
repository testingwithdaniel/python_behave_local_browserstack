import sys
import time

from behave import *
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')


@given('I open url "{url}"')
def step_impl(context, url):
   context.browser.get(url)

@when('I enter "{text}"')
def step_impl(context, text):
    context.browser.find_elements(By.ID, value='q')[1].send_keys(text)

@when('Click Search button')
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME, value='btn-orange').click()

@then('I should see result for invalid city "{result}"')
def step_impl(context, result):
    assert result in context.browser.find_element(By.CLASS_NAME, value='alert-warning').text.split('\n')[1]

@then('I should see result for valid city "{city}"')
def step_impl(context, city):
   assert city in context.browser.find_element(By.PARTIAL_LINK_TEXT, value=city).text
   context.browser.find_element(By.PARTIAL_LINK_TEXT, value=city).click()
   time.sleep(5)
   assert city in context.browser.find_element_by_class_name("weather-widget__city-name").text.replace("Weather in ", '')
