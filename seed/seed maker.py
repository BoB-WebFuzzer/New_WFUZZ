import random
import re
from waf_bypass import Bypass


def ReadFile(fd,ls):
    line = None
    while line != "":
        line = fd.readline()
        if line != "" and line[-1] == '\n':
            #line.strip('\n')
            line = re.sub('[\n]', '', line)
        ls.append(line)
    fd.close()

def RandomSeed(ls1,ls2,ls3,ou3tput, n):
    print(len(ls1), len(ls2), len(ls3))
    for i in range(n):
        seed = ls1[random.randint(0, len(ls1) -1)] + ls2[random.randint(0, len(ls2) -1)] +  ls3[random.randint(0, len(ls3) -1)]
        if len(seed) <3:
            continue
        #print("*New SEED: ", seed)
        seed = seed + '\n'
        output.writelines(seed)


first = open("./xss/first_gadget.txt", "r", encoding='UTF8')
second = open("./xss/second_gadget.txt", "r", encoding='UTF8')
third = open("./xss/third_gadget.txt", "r", encoding='UTF8')
output = open("./xss/output.txt","w", encoding='UTF-8')
ls1,ls2,ls3 = [],[],[]

ReadFile(first,ls1)
ReadFile(second,ls2)
ReadFile(third,ls3)



n = int(input("How many SEED do you need?: "))
RandomSeed(ls1,ls2,ls3,output, n)
output.close()

print("1")

outputForRead = open("./xss/output.txt","r", encoding='UTF-8')
outputfin = open("./xss/output.txt","a", encoding='UTF-8')

ls = []
ReadFile(outputForRead, ls)
Bypass.wafBypassBucket(Bypass,outputfin,ls)
print("2")
#Bypass.wafBypassCaseXSS(Bypass,outputfin,ls)
print("3")


outputForRead.close()

outputfin.close()








