#twitterWriter.py
# bot to automate twitter functions
# written by Nathan Lauder

from selenium import webdriver
from time import sleep

class twitterPost:
    # initialize the user profile and login to the account
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
    # type a tweet and post it
    def tweet(self, tweet):
        self.driver.find_element_by_xpath('//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys(tweet)
        sleep(3)
        self.driver.find_element_by_xpath('//a[@role=""]').click()
    # log the user out of the account
    def logout(self):
        self.driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-1twgtwe r-sdzlij r-rs99b7 r-1p0dtai r-1mi75qu r-1d2f490 r-u8s1d r-zchlnj r-ipm5af"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/a[2]/div/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
# user = twitterPost("USERNAME", "PASSWORD")
user.tweet("checking bot")
user.logout()
