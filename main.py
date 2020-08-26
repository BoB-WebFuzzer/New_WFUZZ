import getopt
import sys
import requests
from xss_main import XSS
from Dirtrav import Dirtrav
from Oscinjec import Oscinjec


optlist = "g:p:a:"



def usage():
    print()

opts, args = getopt.getopt(sys.argv[1:], optlist)


url = ""
path = args[0]

params = {}


for i, j in opts:

    if i == "-g": 
        url, getParams = j.split('?',1)

        plist = getParams.split('&')

        for i in range(len(plist)):
            pm, vl = plist[i].split('=',1)
            params[pm] = vl

        #get_xss = XSS("GET", url, params, path)
        print('main_url : ', url)
        print('main_params : ', params)
        print('main_path : ', path)
        get_xss = Dirtrav("GET", url, params, path)
        get_xss.StartFuzz()


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

        #get_xss = XSS("POST", url, params, path)
        get_xss = Oscinjec("POST", url, params, path)
        get_xss.StartFuzz()


    else:
        usage()
