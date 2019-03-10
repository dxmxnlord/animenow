# delete from watchlist

import json
import os
import displaywatchlist as dispwl
os.chdir("..")
import bars
from termcolor import colored
os.chdir("data")

def delete_from_watchlist():
    with open('shows.json','r') as json_file:
        shows_json=json.load(json_file)
    with open('counter.json','r') as json_file_two:
        counter_json = json.load(json_file_two)
    for shows_data in shows_json:
        if shows_json[shows_data] == "empty":
            bars.delete_bar()
            print(colored('║ ','yellow'))
            print(colored('║ ','yellow')+'Add Something to your watchlist first!')
            print(colored('║ ','yellow'))
        else: 
            bars.plain_bar()
            dispwl.display_watchlist()
            os.chdir("../data")
            print()
            bars.delete_bar()
            print(colored('║ ','yellow'))
            print(colored('║ ','yellow')+'Enter the show number to be removed: ',end="")
            show_number=input()
            try:
                check_error = int(show_number)
            except:
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+"No shows deleted!")
                print(colored('║ ','yellow'))
                os.chdir("../main")
                exit(0)
            if not show_number or int(show_number) < 0 :
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+"No shows deleted! ")
                print(colored('║ ','yellow'))
                os.chdir("../main")
                exit(0)
            print(colored('║ ','yellow'))
            show_count=1  
            json_object={}
            json_object[shows_data]=[]
            json_object_two={}
            json_object_two[shows_data]=[]
            deleted_flag = False
            for show in shows_json[shows_data]:
                if show_count == int(show_number):
                    print(colored('║ ','yellow'),end="")
                    for show_details in show:
                        print(str(show[show_details]),end=" ")
                    print("\n"+colored('║ ','yellow'))
                    print(colored('║ ','yellow')+"Are you sure you want to remove [Y/n]: ",end="")
                    choice=input()
                    print(colored('║ ','yellow'))
                    if choice == 'Y' or choice == 'y':
                        deleted_flag = True
                        with open('jtemp.json','w') as temp_json:
                            show_count_sub=1
                            json_object={}
                            json_object[shows_data]=[]
                            for show in shows_json[shows_data]:
                                if not show_count_sub == int(show_number):
                                    json_object[shows_data].append(show)
                                show_count_sub+=1
                            json.dump(json_object,temp_json)
                        os.remove("shows.json")
                        os.rename("jtemp.json","shows.json")
                        for counter_data in counter_json:
                            with open('jtemp.json','w') as temp_json:
                                show_count_sub=1
                                json_object_two={}
                                json_object_two[shows_data]=[]
                                for show in counter_json[counter_data]:
                                    if not show_count_sub == int(show_number):
                                        json_object_two[counter_data].append(show)
                                    show_count_sub+=1
                                json.dump(json_object_two,temp_json)
                            os.remove("counter.json")
                            os.rename("jtemp.json","counter.json")
                    else:
                        os.chdir("../main")
                        exit()
                show_count+=1
            if not len(json_object["shows"]) and deleted_flag:
                json_object[shows_data] = "empty"
                with open('jtemp.json','w') as temp_json:
                    json.dump(json_object,temp_json)
                os.remove("shows.json")
                os.rename("jtemp.json","shows.json")
            for counter_data in counter_json:
                if not len(json_object_two["shows"]) and deleted_flag:
                    json_object_two[counter_data] = "empty"
                    with open('jtemp.json','w') as temp_json:
                        json.dump(json_object_two,temp_json)
                    os.remove("counter.json")
                    os.rename("jtemp.json","counter.json")
            if(json_object[shows_data] != "empty" and deleted_flag):
                print()
                bars.plain_bar()
                dispwl.display_watchlist()
    os.chdir("../main")

