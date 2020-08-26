# FileName: WAF_BYPASS.py
# Author: Seung Hun Han
#
# 기존 조사한 시드파일에 WAF우회기법을 적용해 WAF BYPASS를 시도하는 함수 집합이다.
# KEYWORD에 우회를 원하는 키워드를 사전 입력 할것.

import random

keyword = [
    "SELECT",
    "OR",
    "AND",
    "PRINT",
    "INSERT",
    "DELETE",
    "UPDATE",
    "REPLACE",
    "UNION",
    "FROM",
    "TRUE",
    "FALSE",
    "select",
    "or",
    "and",
    "print",
    "insert",
    "delete",
    "update",
    "replace",
    "union",
    "from",
    "true",
    "false",
    "script",
    "Script",
    "img",
    "iframe",
    "eval"
]

httpKwd =[
    "Script",
    "script",
    "Redirect"

]

class Bypass:
    # 주석처리기법
    def wafBypassComment(self,outputFile, inputFile):
        while True:
            line = inputFile.readline()
            if not line: break

            for k in keyword:
                while line.find(k) != -1 :
                    i = random.randint(0,len(k)-1)
                    nk = k[:i] + "/**/" + k[i:]
                    line = line.replace(k, nk)
            outputFile.write(line)



    # 대소문자 혼용 & 변경 기법
    def wafBypassCase(self,outputFile, inputFile):
        while True:
            line = inputFile.readline()
            if not line: break
            for k in keyword:
                nk1 =k
                if line.find(k) != -1:
                    for j in range(int(len(k)/2)):
                        i = random.randint(0, len(k)-1)
                        nk1 = nk1[:i]+k[i].upper()+nk1[i+1:]
                        i = random.randint(0, len(k)-1)
                        nk1 =nk1[:i]+k[i].lower()+nk1[i+1:]
                    line = line.replace(k, nk1)
            outputFile.write(line)

    def wafBypassCaseXSS(self,outputFile, inputFile):
        l=0
        while l < len(inputFile):
            #print(len(inputFile))
            line = inputFile[l]
            for k in httpKwd:
                nk1 =k
                for j in range(int(len(k)/2)):
                    i = random.randint(0, len(k)-1)
                    nk1 = nk1[:i]+k[i].upper()+nk1[i+1:]
                    i = random.randint(0, len(k)-1)
                    nk1 =nk1[:i]+k[i].lower()+nk1[i+1:]
                line = line.replace(k, nk1)
            #print(line)
            l+=1
            outputFile.write("\n"+line)

    def wafBypassBucket(self,outputFile, inputFile):
        l=0
        while l < len(inputFile):
            #print(len(inputFile))
            line = inputFile[l]
            for i in range(len(line)):
                if line[i] == "<":
                    line = line.replace("<", "&lt;")
                if line[i] == ">":
                    line = line.replace(">", "&gt;")
            #print(line)
            l+=1
            outputFile.write("\n"+line)



    # 키워드 대체기법
    def wafBypassKeyword(self,outputFile, inputFile):
        while True:
            line = inputFile.readline()
            if not line: break
            tempLine = line

            newKeyword = []
            for k in keyword:
                if line.find(k) != -1 and k == k.upper():
                    newKeyword.append(k)

            for k in newKeyword:
                nk = k[:1] + k.lower() + k[1:]
                tempLine = tempLine.replace(k, nk)
            if newKeyword != []: outputFile.write(tempLine)


    # 특수 키워드 대체 기법
    def wafBypassFilteringKey(self, outputFile, inputFile):
        keyword_local = ["and", "AND", "or", "OR", "union", "UNION"]
        while True:
            line = inputFile.readline()
            if not line: break
            newLine = line

            newKeyword = []
            for k in keyword_local:
                if line.find(k) != -1:
                    newKeyword.append(k)

            for k in newKeyword:
                sym = ""
                if k == "and" or k == "AND":
                    sym = "&&"
                else:
                    sym = "||"
                newLine = newLine.replace(k, sym)

            if newKeyword != []: outputFile.write(newLine)


#f = open("./xss/output.txt")
#f = open("SQL.txt", 'r')

# wafBypassComment("temp1.txt", f)
#b = Bypass()
#b.wafBypassCase("./xss/bypassout.txt", f)
# wafBypassKeyword("temp3.txt", f)
# afBypassFilteringKey("temp4.txt", f)