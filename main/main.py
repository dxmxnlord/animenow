# main program for anime checker

from termcolor import colored
import os
import bars

def disp_options():
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    bars.main_menu_bar()
    print(colored('║ ','yellow'))
    print(colored('║','yellow')+' 1. Add to watchlist\n'+colored('║','yellow')+' 2. Delete from watchlist\n'+colored('║','yellow')+' 3. Clear watchlist\n'+colored('║','yellow')+' 4. Check for new episodes\n'+colored('║','yellow')+' 5. Display watchlist\n'+colored('║','yellow')+' 6. Show counter menu\n'+colored('║','yellow')+' 7. Download episodes\n'+colored('║','yellow')+' 8. Exit\n'+colored('║','yellow'))
    return

