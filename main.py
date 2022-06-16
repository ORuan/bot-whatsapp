from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

DRIVER_PATH = chromedriver_autoinstaller.install()
BRAVE_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"


class Bot():

    def __init__(self, numbers=None, content=None):
        self.content = content
        self.numbers = numbers


    def setup(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--start-maximized')
        options.add_argument('lang=pt-br')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('disable-infobars')
        options.add_argument('--user-data-dir=C:/Users/Ruan Pablo/AppData/Local/Google/Chrome/User Data')
        options.add_argument('--profile-directory=Pessoa 1')

        options.binary_location = BRAVE_PATH
        #options.add_argument()
        return options
        

    def send_numbers(self):
        options = self.setup()
        browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

        browser.execute_script(
            "navigator.__defineGetter__('userAgent', function () {return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'});")
        browser.execute_script("return navigator.userAgent;")


        for _number in self.numbers:
            browser.get(f'https://web.whatsapp.com/send?phone={_number}')
            time.sleep(18)
            chat_box = browser.find_element(by=By.XPATH,
                value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            chat_box.send_keys(self.content)
            botao_enviar = browser.find_element(by=By.XPATH,
                value="//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(1)
            browser.close()
            

    
b = Bot(numbers=['5577998714634'], content="Oi, tudo bem?")
b.send_numbers()