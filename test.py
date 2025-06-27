from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s= Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
page = driver.get("https://google.com")
print(page)