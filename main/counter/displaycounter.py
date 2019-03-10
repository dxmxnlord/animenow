# display the counter

import json
from termcolor import colored
import os
os.chdir("../data")
def display_counter():
    with open('counter.json') as json_file:
        counter_json=json.load(json_file)
        for counter_data in counter_json:
            if(counter_json[counter_data]=="empty"):
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+"You haven't added any shows!")
                print(colored('║ ','yellow'))
            else:
                print(colored('║ ','yellow'))
                show_count_main=1
                for show in counter_json[counter_data]:
                    show_count_sub=1
                    for show_details in show:
                        if show_count_sub%2:
                            print(colored('║ ','yellow')+str(show_count_main),end="]  ")
                        if show_count_sub is 1:
                            print(show[show_details],end="  >  ")
                        else:
                            print(show[show_details])
                        show_count_sub+=1
                    show_count_main+=1
                    print(colored('║ ','yellow'))
    os.chdir("../counter")
