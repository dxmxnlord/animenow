# download next episode

import re
import bs4
import urllib.request
import os
import json
import string
os.chdir("../counter")
import displaycounter as dispctr
os.chdir("../main")
import subprocess
import sys
os.chdir("..")
import bars
os.chdir("main")
from termcolor import colored
os.chdir("../data")

def open_magnet(magnet):
        if sys.platform.startswith('linux'):
            subprocess.Popen(['xdg-open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif sys.platform.startswith('win32'):
            os.startfile(magnet)
        elif sys.platform.startswith('cygwin'):
            os.startfile(magnet)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.Popen(['xdg-open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def convt_symbol(title):
    for letter in range(0,len(title)):
        if ord(title[letter]) == 8217:
            title = title[0:letter]+chr(39)+title[letter+1:]
        if ord(title[letter]) == 8211:
            title = title[0:letter]+chr(45)+title[letter+1:]
    return title

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
    return anchor_list

def parse_links(anchor_list,show_title,show_episode,resolution):
    reg_compile_obj = re.compile("\[HorribleSubs\] ([\w\W]*) - (\d\d) \[([\w\W]*)\][\S\s]*")
    for anchor_pos in range(0,len(anchor_list)):
            title = str(anchor_list[anchor_pos].get('title'))
            if re.match(reg_compile_obj,convt_symbol(title)):
                reg_match_obj = re.match(reg_compile_obj,convt_symbol(title))
                if reg_match_obj.group(1) == show_title:
                    if int(reg_match_obj.group(2)) == show_episode:
                        if reg_match_obj.group(3) == resolution:
                            for magnet_pos in range(anchor_pos,len(anchor_list)):
                                magnet = str(anchor_list[magnet_pos].get('href'))
                                re_compile_obj_mag = re.compile("magnet:[\s\S]*")
                                if re.match(re_compile_obj_mag,magnet):
                                    return magnet
    return False

def get_next_link(site_url):
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    site_html_request=urllib.request.Request(site_url,headers=head)
    site_html_object=urllib.request.urlopen(site_html_request)
    site_html=bs4.BeautifulSoup(site_html_object,features="lxml")
    li_list = site_html.find_all('li')
    reg_compile_obj = re.compile("[\s\S]*(&p=\d*)")
    for li in li_list:
        try:
            if li['class'] == ["next"]:
                next_link = str(li.a.get('href'))
                reg_match_obj = re.match(reg_compile_obj,next_link)
                if reg_match_obj:
                    next_page = str(reg_match_obj.group(1))
                    return next_page
            if li['class'] == ['next', 'disabled']:
                return "END"
        except:
            continue
    return False

def download_episode():
    nyaa_base="https://nyaa.si/?f=0&c=0_0&q="
    with open('counter.json','r') as json_file:
        counter_json = json.load(json_file)
    bars.plain_bar()
    dispctr.display_counter()
    os.chdir("../data")
    print()
    for counter_data in counter_json:
        if counter_json[counter_data] == "empty":
            os.chdir("../main")
            exit()
    magnet_links=[]
    bars.download_bar()
    print(colored('║ ','yellow'))
    download_shows = input(colored('║ ','yellow')+'enter the show numbers separated by spaces: ')
    if not download_shows:
        print(colored('║ ','yellow'))
        os.chdir("../main")
        exit()
    resolution = input(colored('║ ','yellow')+'enter resolution [480p/720p/1080p]: ')
    while resolution != '480p' and resolution != '720p' and resolution != '1080p':
        print(colored('║ ','yellow')+'Enter a proper resolution!')
        resolution = input(colored('║ ','yellow')+'enter the resolution [480p/720p/1080p]: ')
    print(colored('║','yellow'))
    download_show_no = download_shows.split(' ')
    try:
        for error_item in download_show_no:
            check_error = int(error_item)
    except:
        os.chdir("../main")
        exit()
    download_show_no = list(map(int,download_show_no))
    show_number = 1
    for counter_data in counter_json:
        for show in counter_json[counter_data]:
            if show_number in download_show_no:
                next_page=""
                while(True):
                    try:
                        show_return=get_links(nyaa_base + urllib.request.pathname2url(show["title"])+next_page)
                    except:
                        print(colored('║ ','yellow')+"Cannot access nyaa.si")
                        exit()
                    if show_return:
                        if parse_links(show_return,show["title"],show["episode"]+1,resolution):
                            magnet_links.append(parse_links(show_return,show["title"],show["episode"]+1,resolution))
                            break
                        elif parse_links(show_return,show["title"],show["episode"]+1,resolution) == "END":
                            break
                        else:
                            next_page = get_next_link(nyaa_base + urllib.request.pathname2url(show["title"])+next_page)  
            show_number +=1
    if len(magnet_links) is not 0:
        for magnet in magnet_links:
            open_magnet(magnet)
        print(colored('║ ','yellow')+"Successfully started downloads!")
    print(colored('║ ','yellow'))
    os.chdir("../main")
