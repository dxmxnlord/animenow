#  bars for different modes

import os
from termcolor import colored

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)

def main_menu_bar():
    print(colored('╔','yellow')+colored('═'*(columns-13),'yellow')+colored(' Animenow ','yellow')+colored('═','yellow'))

def display_watchlist_bar():
    print(colored('╔','yellow')+colored('═'*(columns-14),'yellow')+colored(' Watchlist ','yellow')+colored('═','yellow'))

def plain_bar():
    print(colored('╔','yellow')+colored('═'*(columns-1),'yellow'))

def display_counter_bar():
    print(colored('╔','yellow')+colored('═'*(columns-16),'yellow')+colored(' Show Counter ','yellow')+colored('═','yellow'))

def clear_bar():
    print(colored('╔','yellow')+colored('═'*(columns-19),'yellow')+colored(' Clear Watchlist ','yellow')+colored('═','yellow'))

def delete_bar():
    print(colored('╔','yellow')+colored('═'*(columns-15),'yellow')+colored(' Delete Show ','yellow')+colored('═','yellow'))

def download_bar():
    print(colored('╔','yellow')+colored('═'*(columns-17),'yellow')+colored(' Download Show ','yellow')+colored('═','yellow'))

def add_bar():
    print(colored('╔','yellow')+colored('═'*(columns-12),'yellow')+colored(' Add Show ','yellow')+colored('═','yellow'))

def check_bar():
    print(colored('╔','yellow')+colored('═'*(columns-22),'yellow')+colored(' Check For Episodes ','yellow')+colored('═','yellow'))

def add_bar_counter():
    print(colored('╔','yellow')+colored('═'*(columns-19),'yellow')+colored(' Add One Episode ','yellow')+colored('═','yellow'))

def subtract_bar_counter():
    print(colored('╔','yellow')+colored('═'*(columns-24),'yellow')+colored(' Subtract One Episode ','yellow')+colored('═','yellow'))

def edit_bar_counter():
    print(colored('╔','yellow')+colored('═'*(columns-23),'yellow')+colored(' Edit Episode Number ','yellow')+colored('═','yellow'))
