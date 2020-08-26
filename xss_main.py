import os
#import requests
import pycurl
from io import BytesIO
import copy
import urllib.parse
import time
from check.xss_checker import Checkseed


class XSS:
    count = 0

    def __init__(self, method, attack_url, params, path):

        loginfo = {"login": "bee", "password": "bug", "security_level": "0", "form": "submit"}
        loginUrl = "http://172.30.1.21:8080/bWAPP/login.php"
        self.C = pycurl.Curl()
        self.C.setopt(self.C.COOKIEJAR, 'cookie.txt')
        self.C.setopt(self.C.POST,True)
        self.C.setopt(self.C.FOLLOWLOCATION, 1)
        buf = BytesIO()
        self.C.setopt(self.C.WRITEDATA, buf)
        self.C.setopt(self.C.POSTFIELDS, urllib.parse.urlencode(loginfo))
        self.C.setopt(self.C.URL,loginUrl )
        self.C.perform()

        time.sleep(1)

        self.temp = {}
        self.mut = {}
        self.url = attack_url  # 공격 대상
        self.method = method  # HTTP METHOD
        self.par = params  # 파라미터
        self.c = pycurl.Curl()
        self.c.setopt(self.c.FOLLOWLOCATION, 1)
        self.c.setopt(self.c.COOKIEFILE, 'cookie.txt')
        self.c.setopt(self.c.COOKIEJAR, 'cookie.txt')
        self.buffer = BytesIO()
        self.c.setopt(self.c.WRITEDATA, self.buffer)
        if method == "GET":
            self.c.setopt(self.c.HTTPGET, True)
            self.c.setopt(self.c.POST, False)
        else:
            self.c.setopt(self.c.URL, attack_url)
            self.c.setopt(self.c.POST, True)
            self.c.setopt(self.c.HTTPGET, False)


        self.seed = open(path, "r")  # 시드파일 경로

        tmp = self.seed.readlines()
        self.seed.close()
        self.seed = tmp




    def StartFuzz(self):
        self.Fuzz(self.seed[0].replace('\n', ''))
        #for i in self.seed:
        #    if Checkseed(i).checking() :
        #        self.Fuzz(i)        

    def Fuzz(self, vector):

        self.mut = self.InsertSeed(vector)
        #print(param)
        if (self.method == "GET"):
            gurl = self.url + '?' + urllib.parse.urlencode(self.mut)
            print(gurl)
            self.c.setopt(self.c.URL, gurl)
        #    res = requests.get(self.url, params=self.InsertSeed(vector))  # @ --> 공격 시드로 변경


        else:  # (self.method == "POST"):
            #print(self.url)
            self.c.setopt(self.c.POSTFIELDS, urllib.parse.urlencode(self.mut))
        #    res = requests.post(self.url, data=self.InsertSeed(vector))  # @ --> 공격 시드로 변경
        self.c.perform()
        self.res = self.buffer.getvalue()
        self.ResultProcess(self.res.decode('euc-kr'))

    def InsertSeed(self, vector):
        # 파라미터마다 다른 시드 삽입
        temp = copy.deepcopy(self.par)
        for i in temp.keys():
            if (temp[i] == '$'):
                temp[i] = vector[:-1]
        self.temp = temp
        return temp

    def Check(self, res):
        idx = 0
        for i, j in self.par.items():
            if j == "$":
                idx = i
                break

        #print(res)
        #print(self.mut[i])
        if res.find(self.mut[i])!=-1 :
            return 1
        else:
            return 0
    def ResultProcess(self, res):
        # 결과 정리
        # format: "TYPE, #         Code            Success         Payload"
        #self.c.close()
        XSS.count += 1
        #time.sleep(3)
        r = self.c.getinfo(pycurl.HTTP_CODE)
        result_string = "{:<16}{:<16}{:<16}{}".format("xss#" + str(XSS.count), r,
                                                      self.Check(res), self.temp)
        print(result_string)