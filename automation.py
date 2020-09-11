from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://twitter.com/login')

email = "dummygithub619@gmail.com"
password = "babydinosaur"

loginField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')

passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

loginButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')

loginField.send_keys(email)

passwordField.send_keys(password)

loginButton.click()

tweet = "Hello Everyone! This is a tweet that I am sending from a selenium automated script written in Python ( It feels really awesome (: ) . \n If you too want to learn this supercool trick then visit Hack Club Workshops.\n https://workshops.hackclub.com"

tweetInputField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')

tweetInputField.send_keys(tweet)

tweetButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')

time.sleep(1)

tweetButton.click()
