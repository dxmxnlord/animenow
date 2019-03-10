# add to the watchlist

import json 
import os
import horriblechecker as horrible
import re
os.chdir("..")
import bars
os.chdir("main")
from termcolor import colored
os.chdir("../data")

def unconvt_symbol(title):
    re.sub(u"(\u2018|\u2019|)","'", title)
    re.sub(u"(\u2013)","-",title)
    for letter in range(0,len(title)):
        if ord(title[letter]) == 8217:
            title = title[0:letter]+chr(39)+title[letter+1:]
        if ord(title[letter]) == 8211:
            title = title[0:letter]+chr(45)+title[letter+1:]    
    return title

def add_to_watchlist():
    bars.add_bar()
    print(colored('║ ','yellow'))
    with open('shows.json','r') as json_file:
        shows_json=json.load(json_file)
    for shows_data in shows_json:
        if shows_json[shows_data] == "empty":
            json_object={}
            json_object["shows"]=[]
            json_object_two={}
            json_object_two["shows"]=[]
            show_to_add=input(colored('║ ','yellow')+'Enter the show you wish to add: ')
            if not show_to_add:
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+'No shows added!')
                print(colored('║ ','yellow'))
                os.chdir("../main")
                exit()
            horrible_show=horrible.check_horriblesubs(show_to_add)
            while(not horrible_show):
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+'Please enter a show running as per https://horriblesubs.info/current-season/')
                show_to_add=input(colored('║ ','yellow')+'Enter the show you wish to add: ')
                if not show_to_add:
                    print(colored('║ ','yellow'))
                    print(colored('║ ','yellow')+'No shows added!')
                    print(colored('║ ','yellow'))
                    os.chdir("../main")
                    exit()
                horrible_show=horrible.check_horriblesubs(show_to_add)
            print(colored('║ ','yellow'))
            print(colored('║ ','yellow')+show_to_add+" has been added!")
            json_object["shows"].append( {"title":unconvt_symbol(show_to_add), "episode": 1})
            json_object_two["shows"].append( {"title":unconvt_symbol(show_to_add), "episode": 0})
            with open("jtemp.json",'w') as temp_json:
                json.dump(json_object,temp_json)
            os.remove("shows.json")
            os.rename("jtemp.json","shows.json")
            with open("jtemp.json",'w') as temp_json:
                json.dump(json_object_two,temp_json)
            os.remove("counter.json")
            os.rename("jtemp.json","counter.json")
        else:
            with open("jtemp.json",'w') as temp_json:
                show_to_add=input(colored('║ ','yellow')+'Enter the show you wish to add: ')
                horrible_show=horrible.check_horriblesubs(show_to_add)
                if not show_to_add:
                    print(colored('║ ','yellow'))
                    print(colored('║ ','yellow')+'No shows added!')
                    print(colored('║ ','yellow'))
                    os.chdir("../main")
                    exit()
                while(not horrible_show):
                    print(colored('║ ','yellow'))
                    print(colored('║ ','yellow')+'Please enter a show running as per https://horriblesubs.info/current-season/')
                    show_to_add=input(colored('║ ','yellow')+'Enter the show you wish to add: ')
                    horrible_show=horrible.check_horriblesubs(show_to_add)
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+show_to_add+" has been added!")
                shows_json[shows_data].append({"title":unconvt_symbol(show_to_add), "episode":1})
                json.dump(shows_json,temp_json)
            os.remove("shows.json")
            os.rename("jtemp.json","shows.json")
            with open("counter.json",'r') as json_file:
                counter_json = json.load(json_file)
            for counter_data in counter_json:
                with open("jtemp.json",'w') as temp_json:
                    counter_json[counter_data].append({"title":unconvt_symbol(show_to_add), "episode":0})
                    json.dump(counter_json,temp_json)
                os.remove("counter.json")
                os.rename("jtemp.json","counter.json")
    print(colored('║ ','yellow'))
    os.chdir("../main")
