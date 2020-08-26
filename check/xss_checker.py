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
        self.driver = webdriver.Chrome('./check/chromedriver', chrome_options=self.chrome_opt)
    def preprocess(self,seed):
        fp = open("./check/test2.html", "w")
        string = "<script>location.reload = () => {}; window.testSuccess = false; window.test = () => testSuccess = true;</script>" + "\n" + seed
        fp.writelines(string)

    def checking(self,seed):
        self.preprocess(seed)
        try:
            self.driver.get("file://"+os.getcwd()+'/'+ 'check/'+"test2.html")
            tes = self.driver.execute_script("return window.testSuccess")
        except:
            tes = self.driver.execute_script("return window.testSuccess")
        return tes

# fd = open("test.html","r")
# fp = open("test2.html","w")
# string = fd.readline()
# string =  "<script>location.reload = () => {}; window.testSuccess = false; window.test = () => testSuccess = true;</script>" + "\n" +string
# fp.writelines(string)
# ch = Checkseed()
# ch.checking("<script>eval(test())</script>")

