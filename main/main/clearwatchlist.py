# clear the watchlist

import os
import json
os.chdir("..")
import bars
os.chdir("main")
from termcolor import colored
os.chdir("../data")

def clear_watchlist():
    bars.clear_bar()
    print(colored('║ ','yellow'))
    choice = input(colored('║ ','yellow')+"Do you really want to clear your watchlist [Y/n]: ")
    if choice == 'Y' or choice == 'y':
        choice = input(colored('║ ','yellow')+"Are you sure [Y/n]: ")
        if choice == 'Y' or choice == 'y':
            json_object = {}
            json_object["shows"] = "empty"
            with open('temp.json','w') as temp_json:
                json.dump(json_object,temp_json)
            os.remove('shows.json')
            os.rename('temp.json','shows.json')
            with open('temp.json','w') as temp_json:
                json.dump(json_object,temp_json)
            os.remove('counter.json')
            os.rename('temp.json','counter.json')
            print(colored('║ ','yellow'))
            print(colored('║ ','yellow')+"Watchlist cleared!")
            print(colored('║ ','yellow'))
        else:
            print(colored('║ ','yellow'))
            os.chdir("../main")
            exit()
    else:
        print(colored('║ ','yellow'))
        os.chdir("../main")
        exit()

