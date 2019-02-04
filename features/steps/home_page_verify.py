import sys

from behave import *
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')


@given('I visit url "{url}"')
def step_impl(context, url):
   context.browser.get(url)

@then('title be "{title}"')
def step_impl(context, title):
   assert title in context.browser.title

@then('search button text should be "{text}"')
def step_impl(context, text):
    assert text in context.browser.find_element(By.CLASS_NAME, value='btn-orange').text

@then('tagline should be "{tagl}"')
def step_impl(context, tagl):
    assert tagl in context.browser.find_element(By.CLASS_NAME, value='jumbotron__title').text

@then('I should see navigation bar')
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME, value='navbar-collapse')

@then('I should see footer')
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME, value='footer-dark')
