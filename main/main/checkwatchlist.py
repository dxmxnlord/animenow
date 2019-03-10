# check the watchlist

import re
import bs4
import urllib.request
import os
import json
import string
import updatewatchlist as updwl
os.chdir("..")
import bars
os.chdir("main")
from termcolor import colored
os.chdir("../data")

def convt_symbol(title):
    for letter in range(0,len(title)):
        if ord(title[letter]) == 8217:
            title = title[0:letter]+chr(39)+title[letter+1:]
        if ord(title[letter]) == 8211:
            title = title[0:letter]+chr(45)+title[letter+1:]
    return title

def filter_list(title_list):
    title_list = list(filter(lambda x: x != None,title_list)) 
    title_list = list(filter(lambda x: x != 'Anime - English-translated',title_list))
    title_list = list(filter(lambda x: x != 'Anime - Raw',title_list))
    title_list = list(filter(lambda x: x != 'Audio - Lossless',title_list))
    title_list = list(filter(lambda x: x != 'Anime - Non-English-translated',title_list))
    title_list = list(filter(lambda x: x != 'Anime - Anime Music Video',title_list))
    title_list = list(filter(lambda x: x != 'Literature - Raw',title_list))
    title_list = list(filter(lambda x: x != 'Audio - Lossy',title_list))
    for title in range(0,len(title_list)):
        if re.match(r'\d* comments*',str(title_list[title])):
            title_list[title] = 'blank'
    title_list = list(filter(lambda x: x != 'blank',title_list))
    #print(title_list)
    return title_list

def get_links(site_url):
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    site_html_request=urllib.request.Request(site_url,headers=head)
    site_html_object=urllib.request.urlopen(site_html_request)
    site_html=bs4.BeautifulSoup(site_html_object,features="lxml")
    anchor_list=site_html.find_all('a')
    title_list=[]
    for anchor in anchor_list:
        title_list.append(anchor.get('title'))
        for title in title_list:
            title = str(title)
    title_list = filter_list(title_list)
    return title_list

def parse_links(title_list,show_title,show_episode):
    horrible_show=[]
    reg_compile_obj=re.compile("\[HorribleSubs\] ([\w\W']*) - (\d\d) [\S\s]*")
    for title in title_list:
        reg_match_obj=re.match(reg_compile_obj,convt_symbol(str(title)))
        if reg_match_obj:
            if reg_match_obj.group(1) == show_title:
                horrible_show.append(reg_match_obj.group(1)+' '+str(reg_match_obj.group(2)))
    new_show = False
    reg_compile_obj = re.compile("[\w\W]* (\d\d)")
    for show in horrible_show:
        reg_match_obj = re.match(reg_compile_obj,show)
        if int(reg_match_obj.group(1)) > int(show_episode):
            if new_show:
                if int(reg_match_obj.group(1)) > int(re.match(reg_compile_obj,new_show).group(1)): 
                    new_show = show
                    continue
                continue
            new_show = show
    if new_show:
        return new_show
    return False

def check_watchlist():
    bars.check_bar()
    print(colored('║','yellow'))
    nyaa_base="https://nyaa.si/?f=0&c=0_0&q="
    new_shows=[]
    with open('shows.json','r') as json_file:
        shows_json=json.load(json_file)
        for shows_data in shows_json:
            if shows_json[shows_data] == "empty":
                print(colored('║ ','yellow')+"Add a show to check for new episodes!")
                print(colored('║ ','yellow'))
                os.chdir("../main")
                exit(0)
            else:
                for show in shows_json[shows_data]:
                    try:
                        show_return=get_links(nyaa_base+urllib.request.pathname2url(show["title"]))
                    except:
                        print(colored('║ ','yellow')+"Cannot access nyaa.si")
                        exit()
                    if show_return:
                        if parse_links(show_return,show["title"],show["episode"]):
                            new_shows.append(parse_links(show_return,show["title"],show["episode"]))
    if len(new_shows) is not 0:
        reg_compile_obj = re.compile("([\w\W]*) (\d\d)")
        for show in new_shows:
            reg_match_obj = re.match(reg_compile_obj,show)
            updwl.update_watchlist(reg_match_obj.group(1),int(reg_match_obj.group(2)))
            print(colored('║ ','yellow')+"New episodes found for " + reg_match_obj.group(1)+" !")
    else:
        print(colored('║ ','yellow')+"No new episodes found !")
    print(colored('║','yellow'))
    os.chdir("../main")

