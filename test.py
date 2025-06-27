from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
# options.add_argument('--user-agent={}'.format(random.choice(list(self.user_agents))))

def scraper():
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)
    url = "https://google.com"
    # Load the URL and get the page source
    driver.implicitly_wait(6)
    driver.get(url)
    return "scrper ran"
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # page = driver.get()
    # print(page)