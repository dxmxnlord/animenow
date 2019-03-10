# subtract from the counter
  
import json
import os
import re
import displaycounter as dispctr
os.chdir("..")
import bars
os.chdir("counter")
from termcolor import colored
os.chdir("../data")
def subtract_episode():
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
            bars.subtract_bar_counter()
            print(colored('║ ','yellow'))
            subtract_from=input(colored('║ ','yellow')+'Enter shows to subtract from separated by spaces: ')
            show_list_subtract = subtract_from.split(' ')
            try:
                for error_item in show_list_subtract:
                    check_error = int(error_item)
            except:
                print(colored('║ ','yellow'))
                exit()
            show_list_subtract = list(map(int,show_list_subtract))
            json_object={}
            json_object[counter_data]=[]
            show_count=1
            for show in counter_json[counter_data]:
                if show_count not in show_list_subtract:
                    json_object[counter_data].append(show)
                else:
                    if show["episode"] is not 0:
                        json_object[counter_data].append({"title": show["title"],"episode": show["episode"]-1})
                    else:
                        print(colored('║ ','yellow'))
                        print(colored('║ ','yellow')+show["title"]+" is already at episode 0")
                        json_object[counter_data].append({"title": show["title"],"episode": show["episode"]})
                show_count+=1
            with open('jtemp.json','w') as temp_json:
                json.dump(json_object,temp_json)
            os.remove("counter.json")
            os.rename("jtemp.json","counter.json")
    print(colored('║ ','yellow'))
    print()
    bars.plain_bar()
    dispctr.display_counter()
    os.chdir("../counter")
