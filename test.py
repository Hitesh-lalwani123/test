from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-extensions')
# options.add_argument('--disable-gpu')
# options.add_argument('--user-agent={}'.format(random.choice(list(self.user_agents))))

options.add_argument('--headless=new')  # Better headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

def scraper():
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)
    url = "https://google.com"
    # Load the URL and get the page source
    driver.implicitly_wait(6)
    page = driver.get(url)
    print(driver.title)
    return driver.title
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # page = driver.get()
    # print(page)