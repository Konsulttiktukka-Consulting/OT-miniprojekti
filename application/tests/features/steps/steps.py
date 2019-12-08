from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu");
driver = webdriver.Chrome(chrome_options=chrome_options)

@given('I am at the start page')
def step_impl(context):
    driver.get('http://localhost:5000/')

@given('I am at the add video page')
def step_impl(context):
    driver.get('http://localhost:5000/videos/new/')
    
@when('I enter a valid youtube url and submit the form')
def step_impl(context):
    driver.implicitly_wait(10)
    urlform = driver.find_element_by_id("url")
    urlform.send_keys("https://www.youtube.com/watch?v=5jKZ9KGtee0")  
    elem = driver.find_element_by_name("addButton")
    elem.click()

@when('I enter a valid twitch url and submit the form')
def step_impl(context):
    driver.implicitly_wait(10)
    urlform = driver.find_element_by_id("url")
    urlform.send_keys("https://www.twitch.tv/esl_csgo")  
    elem = driver.find_element_by_name("addButton")
    elem.click()
       
@when('I click the video list button')
def step_impl(context):
    driver.implicitly_wait(10)
    elem = driver.find_element_by_name("all videos")
    elem.click()

@when('I click the add video button')
def step_impl(context):
    driver.implicitly_wait(10)
    elem = driver.find_element_by_name("add video")
    elem.click()
       
@then('The video is added and shown in the video list')
def step_impl(context):
    driver.implicitly_wait(10)
    assert driver.current_url == 'http://localhost:5000/videos'
    assert ('SQUISH THAT CAT' in driver.page_source)

@then('The stream is added and shown in the video list')
def step_impl(context):
    driver.implicitly_wait(10)
    assert driver.current_url == 'http://localhost:5000/videos'
    assert ('ESL_CSGO' in driver.page_source)
    
@then('I am shown a form to add a video')
def step_impl(context):
    driver.implicitly_wait(10)
    assert driver.current_url == 'http://localhost:5000/videos/new/'
    assert ('Add a new video' in driver.page_source)
    assert ('Video URL' in driver.page_source)

@then('I am shown a list containing all videos')
def step_impl(context):
    driver.implicitly_wait(10)
    assert driver.current_url == 'http://localhost:5000/videos'

@then('I can see a button to remove a video from the list')
def step_impl(context):
    driver.implicitly_wait(10)
    assert ('remove video' in driver.page_source)

@then('I can see a added youtube video in embedded form')
def step_impl(context):
    driver.implicitly_wait(10)
    assert ('iframe' in driver.page_source)

@then('I can see a added twitch stream in embedded form')
def step_impl(context):
    driver.implicitly_wait(10)
    assert ('iframe' in driver.page_source)
