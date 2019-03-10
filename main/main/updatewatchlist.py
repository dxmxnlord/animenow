# update the watchlist
import json
import os

def update_watchlist(show_title,episode_number):
    with open('shows.json','r') as json_file:
        shows_json = json.load(json_file)
    with open('jtemp.json','w') as json_temp:
        for shows_data in shows_json:
            json_object={}
            json_object[shows_data]=[]
            for show in shows_json[shows_data]:
                if not show["title"] == show_title:
                    json_object[shows_data].append(show)
                if show["title"] == show_title:
                    json_object[shows_data].append({"title":show["title"],"episode":episode_number})
            json.dump(json_object,json_temp)
    os.remove('shows.json')
    os.rename('jtemp.json','shows.json')
