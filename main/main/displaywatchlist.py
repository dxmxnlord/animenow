# display the watchlist

import json
from termcolor import colored
import os
os.chdir("../data")

def display_watchlist():
    with open('shows.json') as json_file:
        shows_json=json.load(json_file)
        for shows_data in shows_json:
            if(shows_json[shows_data]=="empty"):
                print(colored('║ ','yellow'))
                print(colored('║ ','yellow')+"You haven't added any shows!")
            else:
                print(colored('║ ','yellow'))
                show_count_main=1
                for show in shows_json[shows_data]:
                    show_count_sub=1
                    for show_details in show:
                        if show_count_sub%2:
                            print(colored('║ ','yellow')+str(show_count_main),end="]  ")
                        show_count_sub+=1
                        if not show_count_sub-1 is 2:
                            print(show[show_details],end="  >  ")
                        else:
                            print(show[show_details])
                    show_count_main+=1
            print(colored('║','yellow'))
    os.chdir("../main")

