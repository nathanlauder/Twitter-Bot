#twitterWriter.py
# bot to automate twitter functions
# written by Nathan Lauder

from selenium import webdriver
from time import sleep

class twitterPost:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path='/Users/nathanlauder/Desktop/chromedriver')
        site = self.driver.get("https://twitter.com/login")
        sleep(4)
        # x path for username and type in
        self.driver.find_element_by_xpath('//input[@name="session[username_or_email]"]').send_keys(username)
        # x path for password and type in
        self.driver.find_element_by_xpath('//input[@name="session[password]"]').send_keys(password)
        # click the login button
        self.driver.find_element_by_xpath('//div[@class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-vw2c0b r-1777fci r-eljoum r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0"]').click()
        sleep(3)
    def tweet(self, tweet):
        # type the tweet then hit the tweet button
        self.driver.find_element_by_xpath('//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys(tweet)
        sleep(3)
        self.driver.find_element_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1n0xq6e r-1vuscfd r-1dhvaqw r-1fneopy r-o7ynqc r-6416eg r-lrvibr"]').click()
#post = twitterPost("YOUR_USERNAME", "YOUR_PASSWORD")
user = twitterPost("USERNAME", "PASSWORD")
user.tweet("checking bot")

