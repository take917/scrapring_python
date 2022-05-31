
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options = Options()

driver = webdriver.Chrome(options=options)

url = "https://search.rakuten.co.jp/search/mall/ANKER/?f=0"
driver.get(url)
