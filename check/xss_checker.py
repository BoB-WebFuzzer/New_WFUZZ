from selenium import webdriver
import os


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
# webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

class Checkseed():
    def __init__(self):
        self.chrome_opt = webdriver.ChromeOptions()
        self.chrome_opt.add_argument("--incognito")
        #self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=self.chrome_opt)

    def checking(self):
        self.driver.get("file://"+os.getcwd()+'/'+"test.html")
        tes = self.driver.execute_script("return typeof conf =='undefined'")
        print(tes)
ch = Checkseed()
ch.checking()

