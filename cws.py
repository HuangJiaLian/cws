#!/usr/bin/python3
# coding=utf-8
import os
import re
import sys
import json
import optparse
import urllib3
import requests
import xmltodict
#from pyfiglet import Figlet
from prettytable import PrettyTable

def welcome():
    # f = Figlet(font='thin')
    # f = Figlet(font='soft')
    print("China Weather Station(CWS)")
# Create a interprater
parser = optparse.OptionParser() 
parser.add_option('-f', '--forecast',help='weather forecast',dest='forecast',default=False, action='store_true')
parser.add_option('-i', '--index',help='give you some indexes according to weather ',dest='index',default=False,action='store_true')
parser.add_option('-s', '--sun',help='get sunrise/sunset time',dest='sun',default=False, action='store_true')
parser.add_option('-v', '--version',help='get the version information',dest='version',default=False,action='store_true')
parser.add_option('-l', '--location',help='give your city\'s name  to get weather information',dest='city',action='store',default='')
# This will let the program surpport the arguments
(opts, args) = parser.parse_args()
if(opts.city==''):
    location = sys.argv[-1]
else:
    location=opts.city

url="http://wthrcdn.etouch.cn/WeatherApi?city=%s" %(location)
request = requests.get(url)

# convert xml format to json
convertedDict = xmltodict.parse(request.text)
jsonStr = json.dumps(convertedDict,indent=1)
weatherData=json.loads(jsonStr)
w=weatherData['resp']
#print(w['zhishus'])

def get_today():
    print(w['wendu']+"℃ " + w['fengxiang'] +' '+ w['fengli'])

def alarm():
    try:
        print(w['alarm']['alarm_details'])
        if(w['alarm']['suggest']!=None):
            print(w['alarm']['suggest'])
    except:
        pass

def get_basic():
    # print(w['forecast']['weather'][0])
    x = PrettyTable(["日期","%s   天气预报"%(location)])
    #x.align["日期"] = "l"# Left align
    x.align["%s   天气预报"%(location)] = "l"# Left align
    x.add_row([w['forecast']['weather'][0]['date'],w['forecast']['weather'][0]['low'][2:6].strip()+' ~' \
        + w['forecast']['weather'][0]['high'][2:6].strip() + '\n白天:' \
        + w['forecast']['weather'][0]['day']['fengli']+' ' + w['forecast']['weather'][0]['day']['fengxiang']+ ' ' \
        + w['forecast']['weather'][0]['day']['type']+'\n夜间:'\
        + w['forecast']['weather'][0]['night']['fengli']+' ' + w['forecast']['weather'][0]['night']['fengxiang']+ ' ' \
        + w['forecast']['weather'][0]['night']['type']+'\n'])

    x.add_row([w['forecast']['weather'][1]['date'],w['forecast']['weather'][1]['low'][2:6].strip()+' ~' \
        + w['forecast']['weather'][1]['high'][2:6].strip() + '\n白天:' \
        + w['forecast']['weather'][1]['day']['fengli']+' ' + w['forecast']['weather'][1]['day']['fengxiang']+ ' ' \
        + w['forecast']['weather'][1]['day']['type']+'\n夜间:'\
        + w['forecast']['weather'][1]['night']['fengli']+' ' + w['forecast']['weather'][1]['night']['fengxiang']+ ' ' \
        + w['forecast']['weather'][1]['night']['type']+'\n'])

    x.add_row([w['forecast']['weather'][2]['date'],w['forecast']['weather'][2]['low'][2:6].strip()+' ~' \
        + w['forecast']['weather'][2]['high'][2:6].strip() + '\n白天:' \
        + w['forecast']['weather'][2]['day']['fengli']+' ' + w['forecast']['weather'][2]['day']['fengxiang']+ ' ' \
        + w['forecast']['weather'][2]['day']['type']+'\n夜间:'\
        + w['forecast']['weather'][2]['night']['fengli']+' ' + w['forecast']['weather'][2]['night']['fengxiang']+ ' ' \
        + w['forecast']['weather'][2]['night']['type']+'\n'])

    x.add_row([w['forecast']['weather'][3]['date'],w['forecast']['weather'][3]['low'][2:6].strip()+' ~' \
        + w['forecast']['weather'][3]['high'][2:6].strip() + '\n白天:' \
        + w['forecast']['weather'][3]['day']['fengli']+' ' + w['forecast']['weather'][3]['day']['fengxiang']+ ' ' \
        + w['forecast']['weather'][3]['day']['type']+'\n夜间:'\
        + w['forecast']['weather'][3]['night']['fengli']+' ' + w['forecast']['weather'][3]['night']['fengxiang']+ ' ' \
        + w['forecast']['weather'][3]['night']['type']+'\n'])

    x.add_row([w['forecast']['weather'][4]['date'],w['forecast']['weather'][4]['low'][2:6].strip()+' ~' \
        + w['forecast']['weather'][4]['high'][2:6].strip() + '\n白天:' \
        + w['forecast']['weather'][4]['day']['fengli']+' ' + w['forecast']['weather'][4]['day']['fengxiang']+ ' ' \
        + w['forecast']['weather'][4]['day']['type']+'\n夜间:'\
        + w['forecast']['weather'][4]['night']['fengli']+' ' + w['forecast']['weather'][4]['night']['fengxiang']+ ' ' \
        + w['forecast']['weather'][4]['night']['type']+'\n'])
    print(x)


def get_index():
    index = PrettyTable(["指数","值","说明"])
    #index.align["今日指数"] = "l"
    index.align["说明"] = "l"
    index.add_row([w['zhishus']['zhishu'][0]['name'],w['zhishus']['zhishu'][0]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][0]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][1]['name'],w['zhishus']['zhishu'][1]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][1]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][2]['name'],w['zhishus']['zhishu'][2]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][2]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][3]['name'],w['zhishus']['zhishu'][3]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][3]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][4]['name'],w['zhishus']['zhishu'][4]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][4]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][5]['name'],w['zhishus']['zhishu'][5]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][5]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][6]['name'],w['zhishus']['zhishu'][6]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][6]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][7]['name'],w['zhishus']['zhishu'][7]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][7]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][8]['name'],w['zhishus']['zhishu'][8]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][8]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][9]['name'],w['zhishus']['zhishu'][9]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][9]['detail']+"\n") ])
    index.add_row([w['zhishus']['zhishu'][10]['name'],w['zhishus']['zhishu'][10]['value'],re.sub(r"(.{20})","\\1\\n",w['zhishus']['zhishu'][10]['detail']) ])
    print(index)

def get_sun():
    items=PrettyTable(["时刻","值"])
    items.add_row(["日出",w['sunrise_1']])
    items.add_row(["日落",w['sunset_1']])
#    items.add_row(["数据\n更新",w['updatetime']])
    print(items)

def get_version():
    print("China Weather Station")
    #f = Figlet(font='soft')
    #print(f.renderText('CWS'))
    print("cws:V1.0")


alarm()
if (opts.version==True):
    get_version()
    exit()

try:
    get_today()
    if (opts.forecast==True):
        get_basic()
    if (opts.index==True):
        get_index()
    if (opts.sun==True):
        get_sun()
    welcome()
except:
    print("Oops! \"Type %s -h\" for help!"%(sys.argv[0]))




