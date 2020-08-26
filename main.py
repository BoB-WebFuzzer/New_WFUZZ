import getopt
import sys
import requests
from xss_main import XSS
from sqli_main import SQLi
from Dirtrav import Dirtrav


optlist = "g:p:a:"



def usage():
    print("directory traversal : python main.py -g <url+?+params> dirt <seed_path>")
    print("sql injection : python main.py -g <url+?+params> sqli <seed_path>")
    print("sql injection : python main.py -p <url> -a <params> sqli <seed_path>")
    print("xss : python main.py -g <url+?+params> xss <seed_path>")
    print("xss python main.py -p <url> -a <params> xss <seed_path>")

opts, args = getopt.getopt(sys.argv[1:], optlist)


url = ""

type = args[0]
path = args[1]

params = {}


for i, j in opts:

    if i == "-g":

        url, getParams = j.split('?',1)

        plist = getParams.split('&')

        for i in range(len(plist)):
            pm, vl = plist[i].split('=',1)
            params[pm] = vl

        if type == "xss":
            XSS("GET", url, params, path).StartFuzz()
        elif type == "sqli":
            SQLi("GET", url, params, path).StartFuzz()
        elif type == "dirt":
            Dirtrav("GET", url, params, path).StartFuzz()
        #get_xss = Dirtrav("GET", url, params, path)



    elif i == "-p":

        url = j

        plist =[]
        for a, postParams in opts:
            if a == "-a":
                plist = postParams.split('&')


        #print(plist)
        for i in range(len(plist)):
            pm, vl = plist[i].split('=',1)
            params[pm] = vl

        if type == "xss":
            XSS("POST", url, params, path).StartFuzz()
        elif type == "sqli":
            SQLi("POST", url, params, path).StartFuzz()


    else:
        usage()
