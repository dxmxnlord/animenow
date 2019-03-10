# change episode number

import json
import os
import re
import displaycounter as dispctr
os.chdir("..")
import bars
from termcolor import colored
os.chdir("data")

def change_episode():
    bars.plain_bar()
    dispctr.display_counter()
    os.chdir("../data")
    print()
    with open('counter.json','r') as json_file:
        counter_json = json.load(json_file)
    for counter_data in counter_json:
        if counter_json[counter_data] == "empty":
            exit()
        else:
            bars.edit_bar_counter()
            print(colored('║ ','yellow'))
            to_change=input(colored('║ ','yellow')+'enter shows to change separated by spaces: ')
            show_list_change = to_change.split(' ')
            try:
                for error_item in show_list_change:
                    check_error = int(error_item)
            except:
                print(colored('║ ','yellow'))
                exit()
            show_list_change = list(map(int,show_list_change))
            json_object={}
            json_object[counter_data]=[]
            show_count=1
            for show in counter_json[counter_data]:
                if show_count not in show_list_change:
                    json_object[counter_data].append(show)
                else:
                    print(colored('║ ','yellow'))
                    new_episode = int(input(colored('║ ','yellow')+show["title"]+" ? > "))
                    while new_episode < 0:
                        print(colored('║ ','yellow'))
                        print(colored('║ ','yellow')+'Enter a valid episode number!')
                        new_episode = int(input(colored('║ ','yellow')+show["title"]+" ? > "))
                    json_object[counter_data].append({"title": show["title"],"episode": new_episode})
                show_count+=1
            with open('jtemp.json','w') as temp_json:
                json.dump(json_object,temp_json)
            os.remove("counter.json")
            os.rename("jtemp.json","counter.json")
    print(colored('║ ','yellow'))
    print()
    bars.plain_bar()
    dispctr.display_counter()
    os.chdir("..")
