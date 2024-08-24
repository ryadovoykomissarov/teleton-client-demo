# -*- coding: cp1251 -*-
import json
import os

dir = os.path.abspath(os.getcwd())
filename = dir + '/bulkdata.json'


def get_categories():
    categories = []
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
        categories = data['categories']
    return categories

def get_channels_by_cat(category):
    channels = []
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
        channels = data['publics'][category]
    return channels