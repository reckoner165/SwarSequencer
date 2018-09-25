__author__ = ' Sumanth Srinivasan'


import json

with open('data/ragasPitchClasses.json') as f:
    data = json.load(f)

def get_raag(raag):
    return data[raag]


def get_raag_list():
    raag_list = []

    for key, value in data.items():
        raag_list.append(key)

    return raag_list
