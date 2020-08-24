import os
import requests
import copy


class XSS:
    count = 0

    def __init__(self, method, attack_url, params, path):
        self.method = method  # HTTP METHOD
        self.url = attack_url  # 공격 대상
        self.par = params  # 파라미터
        self.seed = open(path, "r")  # 시드파일 경로

        tmp = self.seed.readlines()
        self.seed.close()
        self.seed = tmp

    def StartFuzz(self):
        for i in self.seed:
            self.Fuzz(i)

    def Fuzz(self, vector):
        if (self.method == "GET"):
            res = requests.get(self.url, params=self.InsertSeed(vector))  # @ --> 공격 시드로 변경
        else:  # (self.method == "POST"):
            res = requests.post(self.url, data=self.InsertSeed(vector))  # @ --> 공격 시드로 변경

        self.ResultProcess(res)

    def InsertSeed(self, vector):
        # 파라미터마다 다른 시드 삽입
        temp = copy.deepcopy(self.par)
        for i in temp.keys():
            if (temp[i] == '@'):
                temp[i] = vector
        return temp

    def Check(self, res):
        key_tmp = self.par.keys
        if((res.text.find(self.par[key_tmp[0]]))+1):
            return 1
        else:
            return 0
    def ResultProcess(self, res):
        # 결과 정리
        # format: "TYPE, #         Code            Success         Payload"
        XSS.count += 1
        result_string = "{:<16}{:<16}{:<16}{}".format("xss#" + str(XSS.count), res['http'].status_code,
                                                      self.Check(res), res['xss'])
        print(result_string)
