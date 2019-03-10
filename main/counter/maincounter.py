# main program for the checker
import os
from termcolor import colored

def counter_menu():
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    print(colored('╔','yellow')+colored('═'*(columns-17),'yellow')+colored(' Counter Menu ','yellow')+colored('═','yellow')+'\n'+colored('║ ','yellow')+'\n'+colored('║ ','yellow')+"1. Display the show counter\n"+colored('║ ','yellow')+"2. Add one episode\n"+colored('║ ','yellow')+"3. Subtract one episode\n"+colored('║ ','yellow')+"4. Edit episode number\n"+colored('║ ','yellow')+"5. Exit\n"+colored('║ ','yellow'))
    return
