# check in horriblesubs list

import bs4
import urllib.request
import re
import json

def check_horriblesubs(show_name):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    site_request=urllib.request.Request("https://horriblesubs.info/current-season/",headers=hdr)
    site_object=urllib.request.urlopen(site_request)
    site_html=bs4.BeautifulSoup(site_object,features="lxml")
    div_all=site_html.find_all('div')
    shows_running=[]
    for div in div_all:
        try:
            if div['class'] == ["shows-wrapper"]:
                for show in div.contents:
                    shows_running.append(show.string)
        except:
            continue
    shows_running = list(filter(lambda x: x != '\n', shows_running))
    flag = False
    for show in shows_running:
        if show == show_name:
            flag = True
            return show_name
    if flag == False:
        return False

