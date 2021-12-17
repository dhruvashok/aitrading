from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
import time

class TraderClient:
	def __init__(self, username, password):
		self.BASE_URL = "https://www.investopedia.com"
		self.options = Options()
		# self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(options=self.options)
		self.username = username
		self.password = password

	def login(self):
		self.driver.get(self.BASE_URL+"/simulator")
		time.sleep(0.7)
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[5]/div[2]/button").click()
		self.driver.find_element_by_id("username").send_keys(self.username)
		self.driver.find_element_by_id("password").send_keys(self.password)
		self.driver.find_element_by_id("login").click()
		time.sleep(2)

	def trade(self):
		trade_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div[1]/div/header/div[2]/div[1]/div/div[2]/div/a[2]")
		trade_button.click()

client = TraderClient(os.getenv("ita_username"), os.getenv("ita_pass"))
client.login()
client.trade()
