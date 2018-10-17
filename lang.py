#!/usr/bin/python
## -*- coding: utf-8 -*-

import os, sys, json
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.append(parent)

def dictionary(lang='en'):
    try:
        path_for_translation_json = "/lang/json/"+lang+'.json'
        with open(path_for_translation_json) as json_file:
            data = json.load(json_file)
            return data
    except:
        return dictionary('en') #fallback to english
